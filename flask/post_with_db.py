from flask import Flask, request
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(dbname='users', user='postgres', password = 'Mariwa3886920')

POSTS = [
    {
	'text' : 'Text 1',
	'name' : 'User 1',
    'data' : '11-01-2023'	
    }, 
	{
    'text' : 'Text 2',
	'name' : 'User 2',
    'data' : '12-01-2023'	
    }, 
	{
	'text' : 'Text 3',
	'name' : 'User 3',
    'data' : '13-01-2023'	
    }] 

# Запись поста в таблицу posts БД
@app.post('/posts')
def create_posts ():
    cursor = conn.cursor()
    name = request.form.get('name')
    text = request.form.get('text')
    user_id = request.form.get('user_id')
    sql_create_database = f"insert into posts (name,text,user_id) values ('{name}','{text}',{user_id})"
    cursor.execute (sql_create_database)
    conn.commit()
    return 'Posted'

# Вывод всех постов из таблицы posts БД
@app.get('/posts')
def get_posts():
    cursor = conn.cursor()
    sql_create_database = "select * from posts"
    cursor.execute (sql_create_database)
    result = cursor.fetchall()
    return result

# Вывод юзера по id из таблицы users БД
@app.route('/users/<int:user_id>')
def get_users(user_id):
    cursor = conn.cursor()
    sql_create_database = f"select * from users where id = {user_id}"
    cursor.execute (sql_create_database)
    result = cursor.fetchall()
    return result

# Запись юзеров в таблицу users БД
@app.post('/users')
def create_users ():
    cursor = conn.cursor()
    name = request.form.get('name')
    age = request.form.get('age')
    sql_create_database = f"insert into users (name,age) values ('{name}',{age})"
    cursor.execute (sql_create_database)
    conn.commit()
    return 'User Created'

# Вывод всех юзеров из таблицы users БД
@app.get('/users')
def viev_users ():
    cursor = conn.cursor()
    sql_create_database = "select * from users"
    cursor.execute (sql_create_database)
    conn.commit()
    result = cursor.fetchall()
    return result

#Изменение данных пользователей
@app.put('/users/<int:_id>')
def update_user(_id):
    cursor = conn.cursor()
    name = request.form.get('name')
    age = request.form.get('age')
    sql_create_database = f"update users set age = {age}, name = '{name}' where id = {_id}"
    cursor.execute (sql_create_database)
    conn.commit()
    return 'Update'

#Удалить пользователя
@app.delete('/users/<int:_id>')
def delete_user(_id):
    cursor = conn.cursor()
    sql_create_database = f"delete from users where id = {_id}"
    cursor.execute (sql_create_database)
    conn.commit()
    return 'Deleted'