from mysql.connector.connection import MySQLConnection
from GraduateProject.config import (
    MYSQL_USER,
    MYSQL_PWD,
    MYSQL_HOST,
    MYSQL_DATABASE,
)

class MySQLConnectionWrap(MySQLConnection):

    """A wrap for MySQLConnection class. Add with statement support."""

    def __init__(self, **kwargs):
        """Init a new connection instance """
        MySQLConnection.__init__(self)
        self.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DATABASE,
            **kwargs
        )

    def __enter__(self):
        return self

    def __exit__(self, type, value, trace):
        self.close()