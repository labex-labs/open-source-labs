# Предварительная обработка текстовых данных

Прежде чем использовать текстовые данные для машинного обучения, их необходимо предварительно обработать. Это включает несколько шагов, таких как удаление знаков препинания, перевод всего текста в нижний регистр и токенизация текста на отдельные слова. Мы можем выполнить эти шаги предварительной обработки с использованием `CountVectorizer` и `TfidfTransformer` из scikit - learn.

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# Preprocess the text data
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
```

Теперь наша текстовая информация предварительно обработана и готова к извлечению признаков.
