import MySQLdb

from GraduateProject.config import (
    MYSQL_USER,
    MYSQL_PWD,
    MYSQL_HOST,
    MYSQL_DATABASE,
    MYSQL_CHARSET，
)

class MySQLConnectionWrap:

    conn = ''
    cursor = ''

    def __init__(self, host = MYSQL_HOST, user = MYSQL_USER, password = MYSQL_PWD, db = MYSQL_DATABASE, charset = MYSQL_CHARSET):
        self.conn = MySQLdb.connect(host = host, user = user, passwd = password, db = db, charset = charset)
        self.cursor = self.conn.cursor()
        self.cursor.execute("SET NAMES utf8")
        self.cursor.execute("set character_set_database = 'utf8'")
        self.cursor.execute("set character_set_server = 'utf8'")

    def exect(self, sql):
        """
        执行对应的sql语句
        :return:执行操作后的结果
        """
        return self.cursor.execute(sql)

    def exectMany(self, sql, values):
        """
        sql:MySql执行的语句
        values:插入的数据组成的元组
        return:返回操作的影响的记录的条数
        """
        return self.cursor.executemany(sql, values)

    def getAllRecords(self):
        """
        获取数据库中所有的记录
        :return:数据库中所有的记录
        """
        return self.cursor.fetchall()

    def getOneRecord(self):
        """
        获取当前游标指向的一条记录
        :return:数据库的某一条记录
        """
        return self.cursor.fetchone()

    def closeCursor(self):
        """
        关闭cursor
        :return:null
        """
        self.cursor.close()

    def confirm(self):
        """
        提交执行的操作
        :return:null
        """
        self.conn.commit()

    def closeDB(self):
        """
        关闭数据库
        :return:null
        """
        self.conn.close()