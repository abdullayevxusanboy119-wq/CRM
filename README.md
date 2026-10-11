# EduCRM Backend

O'quv markazlari uchun CRM tizimining backend qismi (REST API).

**Frontend:** [educrm-frontend](https://github.com/abdullayevxusanboy119-wq/educrm-frontend)
**Demo (frontend):** https://xusanboy-crm-edu.netlify.app

## Imkoniyatlar
- Talabalar, o'qituvchilar, kurslar va guruhlar boshqaruvi
- Davomat (attendance) hisobi
- To'lovlar va o'qituvchilar oyligi
- JWT orqali autentifikatsiya
- REST API

## Texnologiyalar
Django, Django REST Framework, JWT (SimpleJWT), PostgreSQL

## O'rnatish
```
cd backend
pip install -r requirements.txt
```
`.env` faylini yarating va qiymatlarini to'ldiring (`SECRET_KEY`, baza sozlamalari), so'ng:
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
API `http://127.0.0.1:8000/` manzilida ishga tushadi.

## Muallif
Xusanboy: [GitHub](https://github.com/abdullayevxusanboy119-wq)
