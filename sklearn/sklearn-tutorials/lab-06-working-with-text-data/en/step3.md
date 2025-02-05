# Feature Extraction

To represent the text data as feature vectors, we can use the bags of words representation. This representation assigns a fixed integer id to each word in the training set and counts the number of occurrences of each word in each document. We can extract these feature vectors using scikit-learn's `CountVectorizer`.

```python
from sklearn.feature_extraction.text import CountVectorizer

# Extract feature vectors
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
```

Now we have extracted the feature vectors, and we can use them for training our model.
