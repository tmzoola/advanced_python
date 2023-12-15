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
    cursor.execute(""" select * from market where id between 390 and 400 order by date desc""")
    with open('file.text','w') as file:
        for i in cursor.fetchall():
            file.writelines(str(i)+"\n")
        
        
except Exception as ex:
    print("Salom",ex)
