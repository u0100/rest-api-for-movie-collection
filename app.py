from flask import Flask, jsonify, request
from supabase import create_client, Client
import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Инициализация приложения Flask
app = Flask(__name__)

# Настройка Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/movies', methods=['GET'])
def get_movies():
    """Получить список лучших фильмов"""
    data = supabase.table('movies').select('*').execute()
    return jsonify(data.data)

@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    """Получить информацию о конкретном фильме"""
    data = supabase.table('movies').select('*').eq('id', movie_id).execute()
    if data.data:
        return jsonify(data.data[0])
    else:
        return jsonify({"message": "Film not found"}), 404

@app.route('/movies', methods=['POST'])
def create_movie():
    """Создать новый фильм"""
    new_movie = request.json
    data = supabase.table('movies').insert(new_movie).execute()
    return jsonify(data.data), 201

@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    """Обновить информацию о конкретном фильме"""
    updated_movie = request.json
    data = supabase.table('movies').update(updated_movie).eq('id', movie_id).execute()
    return jsonify(data.data), 200

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    """Удалить фильм"""
    data = supabase.table('movies').delete().eq('id', movie_id).execute()
    return jsonify({"message": "Film deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True)


