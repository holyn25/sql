import pymssql

host_yy = '60.205.143.156'
user_yy = 'sa'
pw_yy = '123456.com'
name_yy = 'QPTreasureDB'

user_id = 6619

conn = pymssql.connect(
    host=host_yy,
    user=user_yy,
    password=pw_yy,
    database=name_yy
)  # type: pymssql.Connection

cursor = conn.cursor()  # type: cursor
cursor.execute('SELECT Score, UserID FROM GameScoreInfo WHERE UserID={}'.format(user_id))  # type: cursor
for row in cursor.fetchall():
    print("ID=%d, Score=%s" % (row[1], row[0]))
conn.close()
