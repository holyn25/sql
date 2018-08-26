import pymssql

host_yy = '60.205.143.156'
user_yy = 'sa'
pw_yy = '123456.com'
name_yy = 'QPTreasureDB'


conn = pymssql.connect(
    host=host_yy,
    user=user_yy,
    password=pw_yy,
    database=name_yy
)  # type: pymssql.Connection

cursor = conn.cursor()  # type: pymssql.Cursor
cursor.execute('update GameScoreInfo set Score = {} WHERE UserID = {}'.format(654123, 6541))  # type: cursor
conn.commit()
conn.close()
