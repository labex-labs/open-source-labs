# Бинаризация многофакторных меток

Бинаризация многофакторных меток - это процесс преобразования коллекции коллекций меток в индикаторный формат. Это можно сделать с использованием класса `MultiLabelBinarizer`.

```python
from sklearn.preprocessing import MultiLabelBinarizer

# Определяем список коллекций меток
y = [[2, 3, 4], [2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2]]

# Создаем экземпляр MultiLabelBinarizer и применяем fit_transform к списку коллекций
MultiLabelBinarizer().fit_transform(y)
```
