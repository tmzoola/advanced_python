import psycopg2

try:
    connection = psycopg2.connect(host = "localhost",
                                  dbname = "fn7",
                                  user = "postgres",
                                  password = "admin",
                                  port  = 5432
    )
    
    connection.autocommit = True

    cursor = connection.cursor()
    cursor.execute(""" select * from market where first_name like 'B%' and date between '2017-01-01' and '2020-12-31'""")
    with open('file.csv','w') as file:
        for i in cursor.fetchall():
            file.writelines(str(i)+"\n")
        
        
except Exception as ex:
    print("Salom",ex)
