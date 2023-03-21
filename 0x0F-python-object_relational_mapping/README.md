# 0x0F. Python - Object-relational mapping

**Please make sure your MySQL server is in 8.0** -> [How to install MySQL 8.0 in Ubuntu 20.04](https://intranet.alxswe.com/rltoken/paGukker_0KoG3D9FqymNQ "How to install MySQL 8.0 in Ubuntu 20.04")

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

##  Without ORM: 

```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```


## With an ORM:

```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

## Resources

**Read or watch**:

- [Object-relational mappers](https://intranet.alxswe.com/rltoken/a8DUOWhXpNX3TEwgyT-U8A "Object-relational mappers")
- [mysqlclient/MySQLdb documentation](https://intranet.alxswe.com/rltoken/JtFaKjnqxudr6Hi05Us1Lw "mysqlclient/MySQLdb documentation") (_please don’t pay attention to `_mysql`_)
- [MySQLdb tutorial](https://intranet.alxswe.com/rltoken/TdUSYFNGbXJG1WjCEoq5FA "MySQLdb tutorial")
- [SQLAlchemy tutorial](https://intranet.alxswe.com/rltoken/YyL5hsscviNH04XGW-XpfA "SQLAlchemy tutorial")
- [SQLAlchemy](https://intranet.alxswe.com/rltoken/j9azWF2Db_2rNolTxOF3SA "SQLAlchemy")
- [mysqlclient/MySQLdb](https://intranet.alxswe.com/rltoken/0zLhY9KqKjn-zmdb7X598Q "mysqlclient/MySQLdb")
- [Introduction to SQLAlchemy](https://intranet.alxswe.com/rltoken/pw50Bl1Bj84wksxm018dwA "Introduction to SQLAlchemy")
- [Flask SQLAlchemy](https://intranet.alxswe.com/rltoken/B-xIdMtGvpus8vHxAIRrPg "Flask SQLAlchemy")
- [10 common stumbling blocks for SQLAlchemy newbies](https://intranet.alxswe.com/rltoken/deIzPMrfK8Ixqm-AboFHWg "10 common stumbling blocks for SQLAlchemy newbies")
- [Python SQLAlchemy Cheatsheet](https://intranet.alxswe.com/rltoken/dZfUNK3lJicGMK5PU0bE7Q "Python SQLAlchemy Cheatsheet")
- [SQLAlchemy ORM Tutorial for Python Developers](https://intranet.alxswe.com/rltoken/hNxBKC8lHge5XjsRO8ksHQ "SQLAlchemy ORM Tutorial for Python Developers") (_**Warning:** This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL_)
- [SQLAlchemy Tutorial](https://intranet.alxswe.com/rltoken/5G_R2NmQRFqiZb84qxYERQ "SQLAlchemy Tutorial")

## Learning Objectives

In this project I learnt:

- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to `SELECT` rows in a MySQL table from a Python script
- How to `INSERT` rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

### Install `MySQLdb` module version `2.0.x`

For installing `MySQLdb`, you need to have `MySQL` installed: [How to install MySQL 8.0 in Ubuntu 20.04](https://intranet.alxswe.com/rltoken/paGukker_0KoG3D9FqymNQ "How to install MySQL 8.0 in Ubuntu 20.04")

```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

### Install `SQLAlchemy` module version `1.4.x`

```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```


