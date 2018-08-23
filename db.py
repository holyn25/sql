import pymssql

host_yy = '60.205.143.156'
user_yy = 'sa'
pw_yy = '123456.com'
name_yy = 'QPAccountsDB'

conn = pymssql.connect(
    host=host_yy,
    user=user_yy,
    password=pw_yy,
    database=name_yy
)
cursor = conn.cursor()
if not cursor:
    print('error')
else:
    print('ok')
cursor.execute("select * from AccountsInfo where UserID = 40")
rslt = cursor.fetchall()
for a in rslt:
    print(len(a))
conn.close()


