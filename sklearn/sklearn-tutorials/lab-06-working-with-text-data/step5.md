# Evaluating the Model

To evaluate the performance of our model, we can use a held-out test set. We can load the test set using the same process as the training set.

```python
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)
```

Now we can preprocess the test set and extract the feature vectors.

```python
X_test_counts = count_vect.transform(twenty_test.data)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)
```

Finally, we can use our trained model to make predictions on the test set and calculate the accuracy.

```python
predicted = clf.predict(X_test_tfidf)
accuracy = np.mean(predicted == twenty_test.target)
```
