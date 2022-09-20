import pymysql

conn = pymysql.connect(
    host = 'hr-db1.cwrevot9vajh.us-east-1.rds.amazonaws.com',
    port = 3306,
    user = 'admin',
    password = 'hrdb12345',
    db = 'hr-db1'
)

