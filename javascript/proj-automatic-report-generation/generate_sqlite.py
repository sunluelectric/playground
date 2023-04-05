import os
import datetime, time
import sqlite3
from sqlite3 import Error
import random

DIR = 'c:/Users/H286302/Dropbox/Community Projects/playground/javascript/proj-automatic-report-generation'
DB_FILE = "./source.db"

class SqliteManager:
    """
    SqliteManager is a wizard program to generate an SQLite database.
    """
    def __init__(self):
        self.conn = None
    def create_db(self, db):
        """
        create_db creates an SQLite database file in the drive
        """
        try:
            self.conn = sqlite3.connect(db)
        except Error as e:
            print(e)
    def create_table(self, table_name: str, table_field: dict):
        cmd = "CREATE TABLE IF NOT EXISTS {table_name} (".format(table_name = table_name)
        for i in table_field.keys():
            cmd = cmd + i + " " + table_field[i] + ","
        cmd = cmd[:-1] + ");"
        self.execute_sql_command(cmd)
    def insert_table(self, table_name: str, row_field: dict):
        cmd = "INSERT INTO {table_name} (".format(table_name = table_name)
        row_field_list = row_field.keys()
        for i in row_field_list:
            cmd = cmd + i + ","
        cmd = cmd[:-1] + ") VALUES ("
        for i in row_field_list:
            cmd = cmd + row_field[i] + ","
        cmd = cmd[:-1] + ");"
        self.execute_sql_command(cmd)
    def commit_sqlite(self):
        self.conn.commit()
    def execute_sql_command(self, cmd):
        try:
            c = self.conn.cursor()
            c.execute(cmd)
        except Error as e:
            print(e)
    def generate_test_database(self):
        if os.path.exists(DB_FILE):
            os.remove(DB_FILE)
        self.create_db(DB_FILE)
        # create table
        # constants
        self.create_table('constants', {
            "field": "CHAR(16) PRIMARY KEY",
            "tag": "CHAR(16)",
            "update_timestamp": "TIMESTAMP",
            "unit_type": "CHAR(16)",
            "unit": "CHAR(16)",
            "val": "DECIMAL(10) NOT NULL"
        })
        # trends
        self.create_table('trends', {
            "field": "CHAR(16) PRIMARY KEY",
            "tag": "CHAR(16)",
            "update_timestamp": "TIMESTAMP",
            "unit_type": "CHAR(16)",
            "unit": "CHAR(16)",
            "num_of_samples": "INTEGER",
            "sampling_frequency": "DECIMAL(10)"
        })
        self.create_table('trends_trend_1', {
            "ind": "INTEGER PRIMARY KEY AUTOINCREMENT" ,
            "trend_timestamp": "TIMESTAMP",
            "val": "DECIMAL(10)"
        })
        self.create_table('trends_trend_2', {
            "ind": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "trend_timestamp": "TIMESTAMP",
            "val": "DECIMAL(10)"
        })
        self.create_table('trends_trend_3', {
            "ind": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "trend_timestamp": "TIMESTAMP",
            "val": "DECIMAL(10)"
        })
        # events
        self.create_table('events', {
            "field": "CHAR(16) PRIMARY KEY",
            "tag": "CHAR(16)",
            "update_timestamp": "TIMESTAMP",
            "num_of_events": "INTEGER"
        })
        self.create_table('events_event_1', {
            "ind": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "start_timestamp": "TIMESTAMP",
            "stop_timestamp": "TIMESTAMP",
            "likelihood_overflow": "DECIMAL(3)"
        })
        self.create_table('events_event_2', {
            "ind": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "start_timestamp": "TIMESTAMP",
            "stop_timestamp": "TIMESTAMP"
        })
        # insert items
        self.insert_table('constants', {
            "field": "'length'",
            "tag": "'LENGTH_METER'",
            "update_timestamp": "'2023-04-04 15:50:00'",
            "unit_type": "'length'",
            "unit": "'meter'",
            "val": "100"
        })
        self.insert_table('constants', {
            "field": "'width'",
            "tag": "'WIDTH_METER'",
            "update_timestamp": "'2023-04-04 15:50:00'",
            "unit_type": "'length'",
            "unit": "'meter'",
            "val": "80"
        })
        self.insert_table('constants', {
            "field": "'area'",
            "tag": "'AREA_M2'",
            "update_timestamp": "'2023-04-04 15:50:00'",
            "unit_type": "'area'",
            "unit": "'meter square'",
            "val": "8000"
        })
        self.commit_sqlite()
        self.insert_table('trends', {
            "field": "'trend_1'",
            "tag": "'POSITION'",
            "update_timestamp": "'2023-04-04 15:50:00'",
            "unit_type": "'length'",
            "unit": "'meter'",
            "num_of_samples": "86400",
            "sampling_frequency": "1"
        })
        self.insert_table('trends', {
            "field": "'trend_2'",
            "tag": "'SPEED'",
            "update_timestamp": "'2023-04-04 15:50:00'",
            "unit_type": "'velocity'",
            "unit": "'meter per second'",
            "num_of_samples": "86400",
            "sampling_frequency": "1"
        })
        self.insert_table('trends', {
            "field": "'trend_3'",
            "tag": "'ACCELERATION'",
            "update_timestamp": "'2023-04-04 15:50:00'",
            "unit_type": "'acceleration'",
            "unit": "'meter per second2'",
            "num_of_samples": "86400",
            "sampling_frequency": "1"
        })
        dt = datetime.datetime(2023, 4, 1, 0, 0, 0)
        s = time.mktime(dt.timetuple())
        for i in range(86400):
            ct = datetime.datetime.fromtimestamp(s+i)
            cts = ct.strftime("%Y-%m-%d %H:%M:%S")
            self.insert_table('trends_trend_1', {
                "trend_timestamp": "'" + cts + "'",
                "val": str(200+15*random.random())
            })
        for i in range(86400):
            ct = datetime.datetime.fromtimestamp(s+i)
            cts = ct.strftime("%Y-%m-%d %H:%M:%S")
            self.insert_table('trends_trend_2', {
                "trend_timestamp": "'" + cts + "'",
                "val": str(10+random.random())
            })
        for i in range(86400):
            ct = datetime.datetime.fromtimestamp(s+i)
            cts = ct.strftime("%Y-%m-%d %H:%M:%S")
            self.insert_table('trends_trend_3', {
                "trend_timestamp": "'" + cts + "'",
                "val": str(2*random.random())
            })
        self.commit_sqlite()
        self.insert_table('events', {
            "field": "'event_1'",
            "tag": "'OVERSPEED'",
            "update_timestamp": "'2023-04-04 15:50:00'",
            "num_of_events": "24"
        })
        self.insert_table('events', {
            "field": "'event_2'",
            "tag": "'OVERACCELERATION'",
            "update_timestamp": "'2023-04-04 15:50:00'",
            "num_of_events": "12"
        })
        for i in range(24):
            ct1 = datetime.datetime.fromtimestamp(s+i*3600+random.randint(600, 1200))
            cts1 = ct1.strftime("%Y-%m-%d %H:%M:%S")
            ct2 = datetime.datetime.fromtimestamp(s+i*3600+random.randint(1260, 1800))
            cts2 = ct2.strftime("%Y-%m-%d %H:%M:%S")
            self.insert_table('events_event_1', {
                "start_timestamp": "'" + cts1 + "'",
                "stop_timestamp": "'" + cts2 + "'",
                "likelihood_overflow": "{0:.2f}".format(random.random())
            })
        for i in range(12):
            ct1 = datetime.datetime.fromtimestamp(s+2*i*3600+random.randint(2100, 2400))
            cts1 = ct1.strftime("%Y-%m-%d %H:%M:%S")
            ct2 = datetime.datetime.fromtimestamp(s+2*i*3600+random.randint(2700, 3000))
            cts2 = ct2.strftime("%Y-%m-%d %H:%M:%S")
            self.insert_table('events_event_2', {
                "start_timestamp": "'" + cts1 + "'",
                "stop_timestamp": "'" + cts2 + "'"
            })
        self.commit_sqlite()
if __name__ == '__main__':
    os.chdir(DIR)
    sqlite_manager = SqliteManager()
    sqlite_manager.generate_test_database()