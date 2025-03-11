## RU
# Flask API для работы с базой данных фильмов
![Screenshot 2025-03-11 211838](https://github.com/user-attachments/assets/fc88d353-c278-473e-80c7-0ad9913c127e)

## Описание
Этот проект представляет собой серверную часть на Flask с подключением к базе данных Supabase. API предоставляет CRUD-функциональность для управления списком фильмов.

## Стек технологий
- **Python** (Flask, Flask-CORS)
- **Supabase** (в качестве базы данных)
- **Vercel** (для хостинга)
- **Dotenv** (для работы с переменными окружения)

## Установка и настройка

### 1. Клонирование репозитория
```sh
git clone https://github.com/your-repo.git
cd your-repo
```

### 2. Установка зависимостей
Убедитесь, что у вас установлен Python 3. Затем установите зависимости:
```sh
pip install -r requirements.txt
```

### 3. Настройка переменных окружения
Создайте файл `.env` в корневой директории проекта и добавьте в него:
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

### 4. Запуск сервера
```sh
python app.py
```

Сервер запустится на `http://127.0.0.1:5000/`.

## API Эндпоинты

### Получить список фильмов
```http
GET /movies
```
Возвращает список фильмов из базы данных.
Пример:
![Screenshot 2025-03-11 211930](https://github.com/user-attachments/assets/0afc544f-4aa8-4a13-b8dc-46cdeeaaef8f)


### Получить информацию о конкретном фильме
```http
GET /movies/{id}
```
Возвращает данные о фильме по его `id`.

### Добавить новый фильм
```http
POST /movies
```
Тело запроса (JSON):
```json
{
  "title": "Название фильма",
  "year": 2024
}
```

### Обновить данные фильма
```http
PUT /movies/{id}
```
Тело запроса (JSON):
```json
{
  "title": "Новое название",
  "year": 2025
}
```

### Удалить фильм
```http
DELETE /movies/{id}
```

## Развертывание
Для развертывания сервера можно использовать любой хостинг, поддерживающий Python. Содержимое .env необходимо перенести в Environment Variables.


## ENG
# Flask API for Movie Database

## Description
This project is a Flask-based backend connected to a Supabase database. The API provides CRUD functionality for managing a list of movies.

## Tech Stack
- **Python** (Flask, Flask-CORS)
- **Supabase** (as the database)
- **Vercel** (for hosting)
- **Dotenv** (for environment variable management)

## Installation and Setup

### 1. Clone the Repository
```sh
git clone https://github.com/your-repo.git
cd your-repo
```

### 2. Install Dependencies
Ensure you have Python 3 installed. Then, install the required dependencies:
```sh
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the project's root directory and add:
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

### 4. Run the Server
```sh
python app.py
```

The server will start at `http://127.0.0.1:5000/`.

## API Endpoints

### Get List of Movies
```http
GET /movies
```
Returns a list of movies from the database.

### Get a Specific Movie
```http
GET /movies/{id}
```
Returns details about a movie by its `id`.

### Add a New Movie
```http
POST /movies
```
Request Body (JSON):
```json
{
  "title": "Movie Title",
  "year": 2024
}
```

### Update a Movie
```http
PUT /movies/{id}
```
Request Body (JSON):
```json
{
  "title": "New Title",
  "year": 2025
}
```

### Delete a Movie
```http
DELETE /movies/{id}
```

## Deployment
You can deploy the server on any Python-compatible hosting platform. The contents of .env need to be moved to Environment Variables.

