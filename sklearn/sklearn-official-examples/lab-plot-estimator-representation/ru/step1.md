# Сжатая текстовая репрезентация

Первый способ отображения оценщиков - это сжатая текстовая репрезентация. При отображении в виде строки оценщики показывают только те параметры, которые были установлены в нестандартные значения. Это уменьшает визуальный шум и делает легче заметить различия при сравнении экземпляров.

```python
from sklearn.linear_model import LogisticRegression

# Создайте экземпляр логистической регрессии с штрафом l1
lr = LogisticRegression(penalty="l1")

# Отобразите оценщик
print(lr)
```
