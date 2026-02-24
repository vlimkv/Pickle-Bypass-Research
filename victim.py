import pickle

print("Загрузка модели для инференса...")
with open('model_v1.pkl', 'rb') as f:
    # Тот самый опасный момент
    model = pickle.load(f)

print("Модель успешно загружена (на самом деле нет).")
