📘 README.md

# 📝 Blog API

REST API для блога с пользователями, постами и комментариями. Реализована аутентификация по JWT. Документация доступна через Swagger.

---

## 🚀 Возможности

- Регистрация и авторизация пользователей (JWT)
- CRUD для постов (только автор может редактировать и удалять)
- Комментирование постов
- Swagger-документация (по адресу `/swagger/`)
- PostgreSQL (через Docker или локально)
- Полноценная настройка CORS, прав доступа, сериализаторов и моделей

---

## 🐳 Запуск с помощью Docker

1. Убедитесь, что у вас установлены `Docker` и `Docker Compose`.
2. Создайте файл `.env` (можно скопировать `.env.example`, если он есть).
3. Выполните команду:

``bash
docker-compose up --build

    После запуска API будет доступно на:
    http://localhost:8000/api/

    Документация (Swagger):
    http://localhost:8000/swagger/

---

## ⚙️ Альтернативный запуск без Docker

``bash
    Клонируйте репозиторий:

git clone https://github.com/mavlidin-creator/month5_test.git
cd month5_test

### Создайте и активируйте виртуальное окружение:

``bash
python3 -m venv venv
source venv/bin/activate

### Установите зависимости:

``bash
pip install -r requirements.txt

### Настройте PostgreSQL и переменные окружения в .env, например:

``bash
DB_NAME=blogdb
DB_USER=bloguser
DB_PASSWORD=blogpass
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your-secret-key

### Примените миграции и запустите сервер:

``bash
python manage.py migrate
python manage.py runserver

    Перейдите в браузер:
    http://127.0.0.1:8000/api/
    Документация Swagger: http://127.0.0.1:8000/swagger/

---


## 📁 Структура проекта

``bash
blog_api/
├── blog/                
├── main/                 
├── manage.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── .env

### 🧪 Примеры запросов
``bash
Регистрация пользователя

POST /api/register/
{
    "username": "user1",
    "password": "your_password"
}

### Получение JWT-токена
``bash
POST /api/token/
{
    "username": "user1",
    "password": "your_password"
}

## 📄 Лицензия

Проект разработан в рамках тестового задания. Используйте как основу для своих проектов или учебы.

---

