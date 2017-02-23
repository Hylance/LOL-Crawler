import MySQLdb

class DatabaseOutputer(object):
    def connectDB(self):
        host="127.0.0.1"
        dbName="LOL_Crawler"
        user="root"
        password=""
        db=MySQLdb.connect(host,user,password,dbName,charset='utf8')
        return db

    def creatTable(self, createTableName):
        createTableSql="CREATE TABLE IF NOT EXISTS "+ createTableName+"(url VARCHAR(100),champion_name VARCHAR(50),nick_name VARCHAR(50),abilities  VARCHAR(500))"
        database=self.connectDB()
        cursor=database.cursor()
        cursor.execute(createTableSql)
        cursor.close()
        database.close()
        print 'creat table '+createTableName+' successfully'
        return createTableName

    def inserttable(self, insertTable, insertUrl, insertChampionName, insertNickName, insertAbilities):
        insertContentSql = "INSERT INTO " + insertTable + "(url,champion_name,nick_name,abilities)VALUES(%s,%s,%s,%s)"
        database = self.connectDB()
        cursor = database.cursor()
        cursor.execute(insertContentSql, (insertUrl, insertChampionName, insertNickName, insertAbilities))
        database.commit()
        database.close()
        # print 'inert contents to  ' + insertTable + ' successfully'



