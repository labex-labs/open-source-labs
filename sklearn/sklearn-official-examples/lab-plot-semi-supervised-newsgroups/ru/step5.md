# Обучение и оценка модели Self-Training

На этом шаге мы применим метод Self-Training к 20% размеченных данных. Мы случайным образом выберем 20% размеченных данных, обучим модель на этих данных, а затем используем модель для предсказания меток для оставшихся неразмеченных данных.

```python
import numpy as np

# Выбор 20% обучающих данных
y_mask = np.random.rand(len(y_train)) < 0.2
X_20, y_20 = map(
    list, zip(*((x, y) for x, y, m in zip(X_train, y_train, y_mask) if m))
)

# Установка невыбранной части данных как неразмеченных
y_train[~y_mask] = -1

# Обучение и оценка конвейера (pipeline) Self-Training
st_pipeline.fit(X_train, y_train)
y_pred = st_pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
