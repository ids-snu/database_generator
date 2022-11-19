import pymysql

databaseServerIP = "astronaut.snu.ac.kr"        # IP address of the MySQL database server
databaseUserName = "root"                       # User name of the database server
databaseUserPassword = ""            # Password for the database user
charSet = "utf8mb4"                             # Character set
cusrorType = pymysql.cursors.DictCursor

connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,
                                     charset=charSet,cursorclass=cusrorType, port=7000)
def createUser(cursor, userName, password):
    try:
        sqlCreateUser = f"CREATE USER {userName}@'%' IDENTIFIED BY '{password}';"
        print(sqlCreateUser)
        cursor.execute(sqlCreateUser)
    except Exception as Ex:
        print("Error creating MySQL User: %s"%(Ex))


def main():
    st_list = []
    f = open('user.txt','r')
    f_done = open('done_user.txt','w')
    for i in f.readlines():
        i = i.strip()
        st_list.append(f'DB{i}')
    try:
        # Create a cursor object
        cursorInsatnce = connectionInstance.cursor()

        # Get list of all database 
        sql = 'SHOW DATABASES;'
        print(sql)
        cursorInsatnce.execute(sql)
        database_dict = cursorInsatnce.fetchall()
        database_list = [database.get('Database') for database in database_dict]
        print(f'Current databases : {database_list}')

        # Get list of all users
        sql = 'SELECT user FROM mysql.user;'
        print(sql)
        cursorInsatnce.execute(sql)
        user_dict = cursorInsatnce.fetchall()
        user_list = [user.get('user') for user in user_dict]
        print(f'Current users : {user_list}')

        for st in st_list:
            print(f'===== {st} =====')
            
            # drop database if it already exists.
            if st in database_list:
                print(f'Database {st} already exists. Drop database.')
                sql = f'DROP DATABASE {st}'
                print(sql)
                cursorInsatnce.execute(sql)

            # create table
            sql = f'CREATE DATABASE {st}'
            print(sql)
            cursorInsatnce.execute(sql)
            
            if st in user_list:
                print(f'User {st} already exists. Drop user.')
                sql = f"DROP USER {st}@'%';"
                print(sql)
                cursorInsatnce.execute(sql)
                
            # create used
            createUser(cursor=cursorInsatnce, userName=st, password=st)

            # grant privileges
            sql = f"GRANT ALL PRIVILEGES ON {st}.* TO {st};"
            print(sql)
            cursorInsatnce.execute(sql)

            sql = "FLUSH PRIVILEGES;"
            print(sql)
            cursorInsatnce.execute(sql)

            f_done.write(f'{st}\n')

    except Exception as e:
        print("Exeception occured:{}".format(e))
    finally:
        connectionInstance.close()

if __name__ == "__main__":
    main()
