Kutubxona Boshqaruv Tizimi
Bu loyiha FastAPI va SQLAlchemy yordamida yaratilgan kutubxona boshqaruv tizimi uchun API.
Texnologiyalar

Python 3.11
FastAPI
SQLAlchemy
PostgreSQL

O'rnatish

Repositoriyani klonlang:
Copygit clone https://github.com/sizning-username/kutubxona-boshqaruv-tizimi.git
cd kutubxona-boshqaruv-tizimi

Virtual muhit yarating va faollashtiring:
Copypython -m venv venv
source venv/bin/activate  # Linux/Mac uchun
venv\Scripts\activate  # Windows uchun

Kerakli paketlarni o'rnating:
Copypip install -r requirements.txt

.env faylini yarating va to'ldiring:
CopyDATABASE_URL=postgresql://username:password@localhost/dbname
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

PostgreSQL ma'lumotlar bazasini yarating.

Ishga tushirish
Loyihani ishga tushirish uchun quyidagi buyruqni bajaring:
Copypython main.py
API http://localhost:8000 manzilida ishlaydi.
API Hujjatlari
API hujjatlarini ko'rish uchun brauzeringizda http://localhost:8000/docs manziliga kiring.
Asosiy Funksiyalar

Kitoblarni qo'shish, o'qish, yangilash va o'chirish
Foydalanuvchilarni ro'yxatdan o'tkazish va autentifikatsiya
Kitoblarga izohlar qoldirish
Kitoblarni olish va qaytarish
Ko'p o'qilgan kitoblar ro'yxatini ko'rish
