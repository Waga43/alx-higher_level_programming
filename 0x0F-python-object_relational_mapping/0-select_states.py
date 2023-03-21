#!/usr/bin/python3
'''import required modules'''

import MySQLdb
import sys

'''
    Command line arguments for MySQL username,
    MySQL password, and database name
'''
_args = sys.argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host = 'localhost', port = 3306, user = _argv[1], passwd = _argv[2], db = _argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
