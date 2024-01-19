import sqlite3

db = sqlite3.connect('my_data_base.db') # подключение к бд, если его нет он создается

cursor = db.cursor()

# создание таблицы
cursor.execute("""
  CREATE TABLE articles(
    title text,
    full_text text,
    views integer,
    avtor text
  )
""")

# добавление записей
cursor.execute("""
  INSERT INTO articles VALUES('Google is cool', 'Google is realy cool', 100, 'admin')
""")

cursor.execute("""
  INSERT INTO articles VALUES('Facebook is cool', 'Facebook is realy cool', 100, 'modest')
""")

# выборка данных
cursor.execute("SELECT * FROM articles")
print(cursor.fetchall()) # позволяет получить все записи из выборки выше в виде списка
cursor.execute("SELECT * FROM articles")
print(cursor.fetchmany(2)) # позволяет получить определенное количество записей из выборки выше в виде списка
cursor.execute("SELECT * FROM articles")
print(cursor.fetchone()) # позволяет получить первое значение в виде кортежа

# Удаление данных
# cursor.execute("DELETE FROM articles WHERE avtor = 'admin'")

# Обновление данных
cursor.execute("UPDATE articles SET avtor = 'Admin' WHERE avtor = 'admin'")

# обновление таблицы
db.commit()

# закрытие базы данных
db.close()