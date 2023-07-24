# Load the Dataset

We will load the 20 newsgroups dataset and vectorize it. We use a few heuristics to filter out useless terms early on: the posts are stripped of headers, footers and quoted replies, and common English words, words occurring in only one document, or in at least 95% of the documents are removed.

```python
from sklearn.datasets import fetch_20newsgroups

n_samples = 2000
n_features = 1000

print("Loading dataset...")
data, _ = fetch_20newsgroups(
    shuffle=True,
    random_state=1,
    remove=("headers", "footers", "quotes"),
    return_X_y=True,
)
data_samples = data[:n_samples]
```
