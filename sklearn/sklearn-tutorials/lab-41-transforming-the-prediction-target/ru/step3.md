# Кодирование меток

Кодирование меток - это процесс преобразования нечисловых меток в числовые метки. Это можно сделать с использованием класса `LabelEncoder`.

```python
from sklearn import preprocessing

# Создаем экземпляр LabelEncoder
le = preprocessing.LabelEncoder()

# Настраиваем LabelEncoder на списке нечисловых меток
le.fit(["paris", "paris", "tokyo", "amsterdam"])

# Получаем классы, изученные LabelEncoder
list(le.classes_)

# Преобразуем список нечисловых меток в числовые метки
le.transform(["tokyo", "tokyo", "paris"])

# Обратное преобразование числовых меток в нечисловые метки
list(le.inverse_transform([2, 2, 1]))
```
