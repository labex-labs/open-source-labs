# Document Biclustering using Spectral Co-clustering Algorithm

## Introduction

In this lab, we will use the Spectral Co-clustering algorithm on the twenty newsgroups dataset to bicluster the documents. The dataset has 20 categories of documents and we will exclude the "comp.os.ms-windows.misc" category as it contains posts with no data. The TF-IDF vectorized posts form a word frequency matrix which is then biclustered using Dhillon's Spectral Co-Clustering algorithm. The resulting document-word biclusters indicate subsets of words used more often in those subsets of documents. We will also cluster the documents using MiniBatchKMeans for comparison.

## Steps

### Step 1: Import Libraries

We will import the necessary libraries for this lab.

```python
from collections import defaultdict
import operator
from time import time
import numpy as np
from sklearn.cluster import SpectralCoclustering
from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.cluster import v_measure_score
```

### Step 2: Define Number Normalizer

We will define a function `number_normalizer()` to map all numeric tokens to a placeholder. This is used for dimensionality reduction.

```python
def number_normalizer(tokens):
    """Map all numeric tokens to a placeholder.

    For many applications, tokens that begin with a number are not directly
    useful, but the fact that such a token exists can be relevant.  By applying
    this form of dimensionality reduction, some methods may perform better.
    """
    return ("#NUMBER" if token[0].isdigit() else token for token in tokens)
```

### Step 3: Define NumberNormalizingVectorizer

We will define a class `NumberNormalizingVectorizer()` that inherits from `TfidfVectorizer()` to build a tokenizer that uses the `number_normalizer()` function we defined earlier.

```python
class NumberNormalizingVectorizer(TfidfVectorizer):
    def build_tokenizer(self):
        tokenize = super().build_tokenizer()
        return lambda doc: list(number_normalizer(tokenize(doc)))
```

### Step 4: Load and Prepare Data

We will load the twenty newsgroups dataset and exclude the "comp.os.ms-windows.misc" category. We will also define the vectorizer.

```python
categories = [
    "alt.atheism",
    "comp.graphics",
    "comp.sys.ibm.pc.hardware",
    "comp.sys.mac.hardware",
    "comp.windows.x",
    "misc.forsale",
    "rec.autos",
    "rec.motorcycles",
    "rec.sport.baseball",
    "rec.sport.hockey",
    "sci.crypt",
    "sci.electronics",
    "sci.med",
    "sci.space",
    "soc.religion.christian",
    "talk.politics.guns",
    "talk.politics.mideast",
    "talk.politics.misc",
    "talk.religion.misc",
]
newsgroups = fetch_20newsgroups(categories=categories)
y_true = newsgroups.target

vectorizer = NumberNormalizingVectorizer(stop_words="english", min_df=5)
```

### Step 5: Vectorize Data

We will vectorize the data using the vectorizer we defined earlier.

```python
X = vectorizer.fit_transform(newsgroups.data)
```

### Step 6: Biclustering using Spectral Co-clustering Algorithm

We will perform biclustering using Spectral Co-clustering algorithm by defining the cocluster and fitting it to the data.

```python
cocluster = SpectralCoclustering(
    n_clusters=len(categories), svd_method="arpack", random_state=0
)
cocluster.fit(X)
y_cocluster = cocluster.row_labels_
```

### Step 7: Cluster using MiniBatchKMeans

We will cluster the data using MiniBatchKMeans.

```python
kmeans = MiniBatchKMeans(
    n_clusters=len(categories), batch_size=20000, random_state=0, n_init=3
)
y_kmeans = kmeans.fit_predict(X)
```

### Step 8: Find Best Biclusters

We will find the best biclusters by calculating their normalized cut and selecting the top five.

```python
feature_names = vectorizer.get_feature_names_out()
document_names = list(newsgroups.target_names[i] for i in newsgroups.target)

def bicluster_ncut(i):
    rows, cols = cocluster.get_indices(i)
    if not (np.any(rows) and np.any(cols)):
        import sys
        return sys.float_info.max
    row_complement = np.nonzero(np.logical_not(cocluster.rows_[i]))[0]
    col_complement = np.nonzero(np.logical_not(cocluster.columns_[i]))[0]
    weight = X[rows][:, cols].sum()
    cut = X[row_complement][:, cols].sum() + X[rows][:, col_complement].sum()
    return cut / weight

bicluster_ncuts = list(bicluster_ncut(i) for i in range(len(newsgroups.target_names)))
best_idx = np.argsort(bicluster_ncuts)[:5]
```

### Step 9: Print Results

We will print the results of the best biclusters found in step 8.

```python
for idx, cluster in enumerate(best_idx):
    n_rows, n_cols = cocluster.get_shape(cluster)
    cluster_docs, cluster_words = cocluster.get_indices(cluster)
    if not len(cluster_docs) or not len(cluster_words):
        continue

    # categories
    counter = defaultdict(int)
    for i in cluster_docs:
        counter[document_names[i]] += 1
    cat_string = ", ".join(
        "{:.0f}% {}".format(float(c) / n_rows * 100, name)
        for name, c in most_common(counter)[:3]
    )

    # words
    out_of_cluster_docs = cocluster.row_labels_ != cluster
    out_of_cluster_docs = np.where(out_of_cluster_docs)[0]
    word_col = X[:, cluster_words]
    word_scores = np.array(
        word_col[cluster_docs, :].sum(axis=0)
        - word_col[out_of_cluster_docs, :].sum(axis=0)
    )
    word_scores = word_scores.ravel()
    important_words = list(
        feature_names[cluster_words[i]] for i in word_scores.argsort()[:-11:-1]
    )

    print("bicluster {} : {} documents, {} words".format(idx, n_rows, n_cols))
    print("categories   : {}".format(cat_string))
    print("words        : {}\n".format(", ".join(important_words)))
```

## Summary

In this lab, we learned how to perform biclustering using the Spectral Co-clustering algorithm on the twenty newsgroups dataset. We also learned how to cluster the data using MiniBatchKMeans for comparison. Finally, we found the best biclusters by calculating their normalized cut and selecting the top five.
