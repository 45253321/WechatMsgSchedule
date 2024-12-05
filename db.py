"""微信数据消息
"""
import os
import sqlite3


class WechatDB(object):

    def __init__(self, db_name: str, table_name: str) -> None:
        self._db_name = db_name
        self._table_name = table_name
        if not os.path.exists(self._db_name):
            self.create_db()

    def create_db(self):
        with sqlite3.connect(self._db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS %s (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        topic TEXT,
                        person1 TEXT,
                        person2 TEXT,
                        content TEXT,
                        day_of_week INT,
                        time TEXT
                    )""" % self._table_name)

    def query_all(self):
        with sqlite3.connect(self._db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT topic, person1, person2, content, day_of_week, time FROM {0}".format(
                self._table_name))
            rows = cursor.fetchall()
            return rows

    def del_data(self, topic):
        with sqlite3.connect(self._db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                           DELETE FROM {0} WHERE topic = "{1}"
                           """.format(self._table_name, topic))

    def update_data(self, data):
        """更新表数据"""
        with sqlite3.connect(self._db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                           UPDATE {0} set person1 ="{1}", person2="{2}", content="{3}", day_of_week={4}, time="{5}"
                           WHERE topic="{6}"
                           """.format(self._table_name,
                           data["person1"], data["person2"], data["content"],
                data["day_of_week"], data["time"], data["topic"]))

    def insert_data(self, data):
        with sqlite3.connect(self._db_name) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                           INSERT INTO {0} (topic, person1, person2, content, day_of_week, time)
                           VALUES (?, ?, ?, ?, ?, ?)
                           """.format(self._table_name),
                           (data["topic"], data["person1"], data["person2"], data["content"],
                            data["day_of_week"], data["time"]))

    def query_count_data(self, topic):
        rows = []
        with sqlite3.connect(self._db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                           select count(*) from {0} where topic = "{1}"
                           """.format(self._table_name, topic))
            rows = cursor.fetchone()

        return rows[0]


def getWechatDb():
    return WechatDB("wechat.db", "messages")


if __name__ == "__main__":
    wc = WechatDB("wechat.db", "messages")
    v = wc.query_count_data("32")
    print(v)
