# Feature Extraction

## Introduction

In this lab, we will learn how to perform feature extraction using the scikit-learn library. Feature extraction is the process of transforming raw data into numerical features that can be used by machine learning algorithms. It involves extracting relevant information from different types of data such as text and images.

## Steps

### Step 1: Loading features from dicts

In this step, we will learn how to load features from dictionaries using the `DictVectorizer` class in scikit-learn.

```python
from sklearn.feature_extraction import DictVectorizer

measurements = [
    {'city': 'Dubai', 'temperature': 33.},
    {'city': 'London', 'temperature': 12.},
    {'city': 'San Francisco', 'temperature': 18.},
]

vec = DictVectorizer()
features = vec.fit_transform(measurements).toarray()
feature_names = vec.get_feature_names_out()

print(features)
print(feature_names)
```

### Step 2: Feature hashing

In this step, we will learn how to perform feature hashing using the `FeatureHasher` class in scikit-learn. Feature hashing is a technique that maps features to a fixed-length vector using a hash function.

```python
from sklearn.feature_extraction import FeatureHasher

movies = [
    {'category': ['thriller', 'drama'], 'year': 2003},
    {'category': ['animation', 'family'], 'year': 2011},
    {'year': 1974},
]

hasher = FeatureHasher(input_type='string')
hashed_features = hasher.transform(movies).toarray()

print(hashed_features)
```

### Step 3: Text feature extraction

In this step, we will learn how to perform text feature extraction using the `CountVectorizer` and `TfidfVectorizer` classes in scikit-learn. These classes can be used to convert text data into numerical features.

```python
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]

vectorizer = CountVectorizer()
features = vectorizer.fit_transform(corpus).toarray()
feature_names = vectorizer.get_feature_names_out()

print(features)
print(feature_names)
```

### Step 4: Customizing the vectorizer classes

In this step, we will learn how to customize the behavior of vectorizer classes by passing callable functions to them.

```python
def my_tokenizer(s):
    return s.split()

vectorizer = CountVectorizer(tokenizer=my_tokenizer)
features = vectorizer.fit_transform(corpus).toarray()

print(features)
```

## Summary

In this lab, we learned how to perform feature extraction using the scikit-learn library. We explored various techniques such as loading features from dicts, feature hashing, and text feature extraction. We also learned how to customize the behavior of vectorizer classes to suit our specific needs. Feature extraction is an important step in machine learning as it helps transform raw data into a format that can be used by algorithms to make predictions or classify data.
