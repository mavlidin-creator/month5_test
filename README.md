```bash
# Без Docker:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# Через Docker:
docker-compose up --build
```# month5_test
