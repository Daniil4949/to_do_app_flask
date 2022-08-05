import sqlite3


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_tasks(self):
        sql = '''SELECT * from tasks ORDER BY id DESC'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res

        except:
            print('Error during processing database')
        return []

    def delete_task(self, id):
        try:
            self.__cur.execute("DELETE FROM tasks WHERE id=?", (id,))
            self.__cur.commit()
        except:
            print('Error during processing database')
