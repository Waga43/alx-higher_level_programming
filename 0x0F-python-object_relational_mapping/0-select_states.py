#!/usr/bin/python3
'''import required modules'''

import MySQLdb
import sys

'''
    Command line arguments for MySQL username,
    MySQL password, and database name
'''

if __name__ == "__main__":
    conn = MySQLdb.connect(host = 'localhost', port = 3306, user = sys.argv[1], passwd = sys.argv[2], db = sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
