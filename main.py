import mmap
import os

def mmap_file(file_path):
    # Faylni ochish
    with open(file_path, 'r+b') as file:
        # Faylni xotiraga yuklash
        with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as mmap_file:
            # Faylni qidiruv qilish
            search_term = input("Qidiruv qilib olish uchun so'z kiriting: ")
            if search_term in mmap_file:
                print("Qidiruv qilingan so'z topildi.")
            else:
                print("Qidiruv qilingan so'z topilmadi.")

# Fayl yo'nalishini kiritish
file_path = input("Fayl yo'nalishini kiriting: ")
mmap_file(file_path)
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. Faylni ochish uchun `file_path` ni kiritishingiz kerak.
2. Faylni xotiraga yuklash uchun `mmap` kutubxonasidan foydalanadi.
3. Faylni qidiruv qilish uchun `input` funksiyasidan foydalanadi.
4. Faylni qidiruv qilish uchun `in` operatoridan foydalanadi.
5. Faylni qidiruv qilish natijasini chiqaradi.
