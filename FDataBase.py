import sqlite3


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_completed_tasks(self):
        """Getting all the completed tasks from the database"""
        sql = '''SELECT * from tasks WHERE is_done = 1 ORDER BY id DESC'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res

        except Exception as e:
            print(f'Error during processing database {e}')
        return []

    def get_uncompleted_tasks(self):
        """Getting all the uncompleted tasks from database"""
        sql = '''SELECT * from tasks WHERE is_done = 0 ORDER BY id DESC'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res

        except Exception as e:
            print(f'Error during processing database {e}')
        return []

    def make_complete(self, id):
        """Mark a definite task as a completed one"""
        sql = f"UPDATE tasks SET is_done = 1 WHERE id = {id}"
        try:
            self.__cur.execute(sql)
            self.__db.commit()
        except Exception as e:
            print(f'Error during processing database {e}')

    def delete_task(self, id):
        """Deleting definite task from the database"""
        sql = f'DELETE FROM tasks WHERE id = {id}'
        try:
            self.__cur.execute(sql)
            self.__db.commit()
        except Exception as e:
            print(f'Error during processing database {e}')

    def delete_all(self):
        """Deleting all the tasks from database"""
        sql = f'DELETE FROM tasks'
        try:
            self.__cur.execute(sql)
            self.__db.commit()
        except Exception as e:
            print(f'Error during processing database {e}')

    def add_task(self, title, info):
        """Add new task to the database"""
        try:
            self.__cur.execute("INSERT INTO tasks VALUES(NULL, ?, ?, 0)", (title, info))
            self.__db.commit()
        except Exception as e:
            print(f'Error during processing database {e}')


