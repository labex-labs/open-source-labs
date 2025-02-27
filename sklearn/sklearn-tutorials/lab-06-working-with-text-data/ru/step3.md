# Извлечение признаков

Чтобы представить текстовые данные в виде векторов признаков, мы можем использовать представление "сумок слов" (bags of words). В этом представлении каждому слову в наборе обучающих данных присваивается фиксированный целый идентификатор, и подсчитывается количество вхождений каждого слова в каждом документе. Мы можем извлечь эти векторы признаков с использованием `CountVectorizer` из scikit - learn.

```python
from sklearn.feature_extraction.text import CountVectorizer

# Extract feature vectors
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
```

Теперь мы извлекли векторы признаков, и можем использовать их для обучения нашей модели.
