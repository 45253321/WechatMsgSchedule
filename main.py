import sys
import threading
import schedule
import pytz
import time
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QAbstractItemView
from PyQt6.QtGui import QCloseEvent, QStandardItemModel, QStandardItem, QIcon
from daydayup import Ui_MainWindow
from datetime import datetime
from wxauto import WeChat
from db import getWechatDb

def time_now(): return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_wc_handle():
    """获取微信操作句柄"""
    wc = WeChat()
    return wc


def warningHtml(msg: str) -> str:
    """警告消息"""
    return f"""
    <p class="warning">
        {time_now()} {msg}
    </p>
    """


def successHtml(msg: str) -> str:
    """成功消息"""
    return f"""
    <p class="success">
        {time_now()} {msg}
    </p>
"""


def textFormat(msg: str) -> str:
    return f"""{time_now()} {msg}"""


def send_msg_with_weixin(content, to_person, topic,  text_browser) -> bool:
    try:
        wc = get_wc_handle()
        wc.SendMsg(content, to_person)
        text_browser.append(textFormat(f"发送 主题:{topic} 到接收人:{to_person} 成功!"))

        return True
    except Exception as e:
        print("send Failed!! {0}".format(str(e)))
        text_browser.append(textFormat(f"发送 主题:{topic} 到接收人:{to_person}  失败!"))

        return False


def run_continuesly(interval=1):
    """子线程处理"""
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run


class Window(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("微信提醒工具")
        self.setFixedSize(self.size())
        # self.setWindowIcon(QIcon('./logo.jpg'))
        self.build_connect()
        self.build_style()
        self.build_table()
        self.schedule = run_continuesly()
        self.build_plan()

    def build_plan(self):
        """从数据库读取计划，启动计划任务监听"""
        rows = getWechatDb().query_all()
        for row in rows:
            topic, person1, person2, content, day_of_week, time = row[:6]
            if person1:
                self.create_schedule_plan(
                    topic, person1, content, time, day_of_week)
            if person2:
                self.create_schedule_plan(
                    topic, person2, content, time, day_of_week)
        if rows:
            self.tb_left.append(textFormat(f"录入{len(rows)}条定时计划任务成功!"))

    def create_schedule_plan(self, topic, to_person, content, time,  day_of_week):
        """创建调度计划"""
        day_handle = None
        if (day_of_week == 1):
            day_handle = schedule.every().monday
        elif (day_of_week == 2):
            day_handle = schedule.every().tuesday
        elif (day_of_week == 3):
            day_handle = schedule.every().wednesday
        elif (day_of_week == 4):
            day_handle = schedule.every().thursday
        elif (day_of_week == 5):
            day_handle = schedule.every().friday
        elif (day_of_week == 6):
            day_handle = schedule.every().saturday
        elif (day_of_week == 7):
            day_handle = schedule.every().sunday

        if day_handle is None:
            return

        day_handle.at(time, pytz.timezone('Asia/Shanghai')).do(send_msg_with_weixin,
                                                               content=content,
                                                               to_person=to_person,
                                                               topic=topic,
                                                               text_browser=self.tb_right
                                                               ).tag(topic)

    def _update_table_data(self):
        datas = getWechatDb().query_all()
        self.model.setRowCount(len(datas))
        self.tableView.setSortingEnabled(True)
        for row, items in enumerate(datas):
            for col, item in enumerate(items):
                item_model = QStandardItem(str(item))
                item_model.setToolTip(str(item))
                item_model.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                font = item_model.font()
                font.setPointSize(10)  # 设置字体大小
                item_model.setFont(font)

                self.model.setItem(row, col, item_model)

    def build_table(self):
        """填充表格数据"""
        headers = ["主题", "接收者1", "接收者2", "内容", "星期几", "时间"]

        self.model = QStandardItemModel(5, len(headers))  # 五行三列
        for i, header in enumerate(headers):
            self.model.setHorizontalHeaderItem(i, QStandardItem(header))

        self._update_table_data()
        # 隐藏左侧的序号
        vh = self.tableView.verticalHeader()
        vh.setVisible(False)
        self.tableView.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection)
        self.tableView.setModel(self.model)

    def build_connect(self):
        """建立信号和槽连接"""
        self.bt_wx.clicked.connect(self.check_weixin)
        self.bt_clear.clicked.connect(self.clear_textBrowser)
        self.bt_exec.clicked.connect(self.exec_now)
        self.bt_save.clicked.connect(self.save)
        self.bt_del.clicked.connect(self.del_item)
        self.bt_modify.clicked.connect(self.modify_item)

    def modify_item(self):
        """修改item数据"""
        selectedIndexes = self.tableView.selectedIndexes()
        if selectedIndexes:
            self.edit_topic.setText(selectedIndexes[0].data())
            self.person1.setText(selectedIndexes[1].data())
            self.person2.setText(selectedIndexes[2].data())
            self.edit_content.setText(selectedIndexes[3].data())
            self.edit_time.setText(selectedIndexes[5].data())
            self.edit_day.setValue(int(selectedIndexes[4].data()))

    def del_item(self):
        """删除条数据"""
        # 选择行数据
        selectedIndexes = self.tableView.selectedIndexes()
        if selectedIndexes:
            # topic
            topic = selectedIndexes[0].data()
            rowToDelete = selectedIndexes[0].row()
            # 软件删除,不显示当前行
            self.model.removeRow(rowToDelete)
            # 物理删除
            getWechatDb().del_data(topic)
            self.tb_right.append(textFormat(f"删除 主题:{topic} 成功!!!"))
            # 删除tag为topic的计划事件
            schedule.clear(topic)

    def get_form_data(self):
        data = {
            "topic": self.edit_topic.text(),
            "person1": self.person1.text(),
            "person2": self.person2.text(),
            "content": self.edit_content.toPlainText(),
            "time": self.edit_time.text(),
            "day_of_week": self.edit_day.value(),
        }
        time = data["time"]
        head, tail = time.split(":")
        time = "%.2d:%.2d" % (int(head.strip()), int(tail.strip()))
        data["time"] = time
        return data

    def save(self):
        """保存数据"""
        data = self.get_form_data()
        if not (data["topic"] and (data["person1"] or data["person2"]) and data["content"] and data["time"] and data["day_of_week"]):
            self.tb_left.insertHtml(warningHtml("数据未填充完全，请检查必填数据"))
            return
        wd = getWechatDb()
        if wd.query_count_data(data["topic"]) > 0:
            getWechatDb().update_data(data)
        else:
            getWechatDb().insert_data(data)

        self._update_table_data()
        self.clear_form()
        schedule.clear(data["topic"])
        if data["person1"]:
            self.create_schedule_plan(
                data["topic"], data["person1"], data["content"], data["time"], data["day_of_week"])
        if data["person2"]:
            self.create_schedule_plan(
                data["topic"], data["person2"], data["content"], data["time"], data["day_of_week"])

        self.tb_right.append(textFormat("保存 主题:{0} 成功!".format(data["topic"])))

    def build_style(self):
        """构建stylesheet样式"""
        doc = self.tb_left.document()
        doc.setDefaultStyleSheet("""
        .warning {
            color: red;
            font-weight: bold;
        }
        .success {
            color: green;
            font-weight: bold;
        }
                                 """)
        doc_two = self.tb_right.document()
        doc_two.setDefaultStyleSheet("""
        .warning {
            color: red;
            font-weight: bold;
        }
        .success {
            color: green;
            font-weight: bold;
        }
                                 """)

    def clear_form(self):
        """清除表单数据"""
        self.edit_topic.clear()
        self.edit_content.clear()
        self.person1.clear()
        self.person2.clear()
        self.edit_time.clear()

    def exec_now(self):
        """立即执行"""
        topic = self.edit_topic.text()
        person1 = self.person1.text()
        person2 = self.person2.text()
        content = self.edit_content.toPlainText()
        if not (topic and content):
            self.tb_left.insertHtml(warningHtml("请输入主题和内容!!!"))
            return

        if not (person1 or person2):
            self.tb_left.insertHtml(warningHtml("请输入接收人信息!!!"))
            return

        for p in [person1, person2]:
            if not p:
                continue
            try:
                send_msg_with_weixin(content, p, topic, self.tb_right)
            except Exception as e:
                print(e)
                self.tb_right.insertHtml(
                    warningHtml(f"发送  主题:{topic}  到接收人:{p} 失败!"))
                continue

            self.tb_right.insertHtml(
                successHtml(f"发送 主题:{topic} 到接收人:{p} 成功!"))

        self.clear_form()

    def clear_textBrowser(self):
        """清理系统日志显示"""
        self.tb_left.clear()
        self.tb_right.clear()
        self.clear_form()

    def check_weixin(self):
        """检查微信是否存活，并输出一些信息"""
        try:
            wc = get_wc_handle()
            members = wc.GetGroupMembers()
            self.tb_left.append(textFormat("获取微信应用成功!"))
            if members:
                self.tb_left.append(textFormat(
                    "检测到用户列表:" + ",".join(members[:5])))
        except Exception as e:
            self.tb_left.append(warningHtml(
                "获取微信应用失败!!!\r\n请检查微信应用是否打开!!!"))

    def closeEvent(self, a0: QCloseEvent | None) -> None:
        self.on_before_close()
        return super().closeEvent(a0)

    def on_before_close(self):
        """退出之前执行相应的处理"""
        self.schedule.set()


def main():
    app = QApplication(sys.argv)
    Form = Window()
    Form.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
