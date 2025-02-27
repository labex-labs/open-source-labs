# Бинаризация меток

Бинаризация меток - это процесс преобразования многоклассовых меток в бинарную индикаторную матрицу. Это можно сделать с использованием класса `LabelBinarizer`.

```python
from sklearn import preprocessing

# Создаем экземпляр LabelBinarizer
lb = preprocessing.LabelBinarizer()

# Настраиваем LabelBinarizer на списке многоклассовых меток
lb.fit([1, 2, 6, 4, 2])

# Получаем классы, изученные LabelBinarizer
lb.classes_

# Преобразуем список многоклассовых меток в бинарную индикаторную матрицу
lb.transform([1, 6])
```
