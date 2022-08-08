import sqlite3


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_completed_tasks(self):
        sql = '''SELECT * from tasks WHERE is_done = 1 ORDER BY id DESC'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res

        except:
            print('Error during processing database')
        return []

    def get_uncompleted_tasks(self):
        sql = '''SELECT * from tasks WHERE is_done = 0 ORDER BY id DESC'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res

        except:
            print('Error during processing database')
        return []

    def make_complete(self, id):
        sql = f"UPDATE tasks SET is_done = 1 WHERE id = {id}"
        try:
            self.__cur.execute(sql)
            self.__db.commit()
        except:
            print('Error during processing database')

    def delete_task(self, id):
        sql = f'DELETE FROM tasks WHERE id = {id}'
        try:
            self.__cur.execute(sql)
            self.__db.commit()
        except:
            print('Error during processing database')

    def delete_all(self):
        sql = f'DELETE FROM tasks'
        try:
            self.__cur.execute(sql)
            self.__db.commit()
        except:
            print('Error during processing database')

    def add_task(self, title, info):
        try:
            self.__cur.execute("INSERT INTO tasks VALUES(NULL, ?, ?, 0)", (title, info))
            self.__db.commit()
        except:
            print('Error during processing database')


