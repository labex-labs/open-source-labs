# Обучение и оценка модели LabelSpreading

На этом шаге мы применим алгоритм LabelSpreading к 20% размеченных данных. Мы случайным образом выберем 20% размеченных данных, обучим модель на этих данных, а затем используем модель для предсказания меток для оставшихся неразмеченных данных.

```python
# Обучение и оценка конвейера (pipeline) LabelSpreading
ls_pipeline.fit(X_train, y_train)
y_pred = ls_pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
