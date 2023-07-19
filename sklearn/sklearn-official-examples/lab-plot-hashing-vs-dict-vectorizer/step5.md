# Comparison with special purpose text vectorizers

We will compare the previous methods with the `CountVectorizer` and `HashingVectorizer`.

```python
from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfVectorizer

t0 = time()
vectorizer = CountVectorizer()
vectorizer.fit_transform(raw_data)
duration = time() - t0
print(f"done in {duration:.3f} s")
print(f"Found {len(vectorizer.get_feature_names_out())} unique terms")

t0 = time()
vectorizer = HashingVectorizer(n_features=2**18)
vectorizer.fit_transform(raw_data)
duration = time() - t0
print(f"done in {duration:.3f} s")

t0 = time()
vectorizer = TfidfVectorizer()
vectorizer.fit_transform(raw_data)
duration = time() - t0
print(f"done in {duration:.3f} s")
print(f"Found {len(vectorizer.get_feature_names_out())} unique terms")
```
