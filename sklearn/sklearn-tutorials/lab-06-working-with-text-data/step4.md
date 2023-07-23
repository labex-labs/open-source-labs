# Training the Model

Now that we have our feature vectors, we can train a model to classify the text data. In this example, we will use the Multinomial Naive Bayes algorithm, which is a popular algorithm for text classification.

```python
from sklearn.naive_bayes import MultinomialNB

# Train the model
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
```

Now our model is trained and ready for prediction.
