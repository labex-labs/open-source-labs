# Semi-Supervised Text Classification

## Introduction

In this lab, you will learn how to perform semi-supervised classification on a text dataset using scikit-learn. Semi-supervised learning is a type of machine learning where a model is trained on both labeled and unlabeled data. This lab will cover how to use Self-Training and LabelSpreading algorithms for semi-supervised text classification. We will be using the 20 newsgroups dataset to train and test our models.

## Steps

### Step 1: Load the Dataset

We will be using the 20 newsgroups dataset, which contains around 18,000 newsgroup posts on 20 topics. In this step, we will load the dataset and print out some basic information about it.

```python
import numpy as np
from sklearn.datasets import fetch_20newsgroups

# Load the dataset with the first five categories
data = fetch_20newsgroups(
    subset="train",
    categories=[
        "alt.atheism",
        "comp.graphics",
        "comp.os.ms-windows.misc",
        "comp.sys.ibm.pc.hardware",
        "comp.sys.mac.hardware",
    ],
)

# Print out information about the dataset
print("%d documents" % len(data.filenames))
print("%d categories" % len(data.target_names))
```

### Step 2: Create the Pipeline for Supervised Learning

In this step, we will create a pipeline for supervised learning. The pipeline will consist of a CountVectorizer to convert the text data into a matrix of token counts, a TfidfTransformer to apply term frequency-inverse document frequency normalization to the count matrix, and an SGDClassifier to train the model.

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

# Parameters for the SGDClassifier
sdg_params = dict(alpha=1e-5, penalty="l2", loss="log_loss")

# Parameters for the CountVectorizer
vectorizer_params = dict(ngram_range=(1, 2), min_df=5, max_df=0.8)

# Create the pipeline
pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SGDClassifier(**sdg_params)),
    ]
)
```

### Step 3: Train and Evaluate the Supervised Model

In this step, we will split the dataset into training and testing sets, and then train and evaluate the supervised model pipeline we created in Step 2.

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

# Split the dataset into training and testing sets
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Train and evaluate the supervised model pipeline
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```

### Step 4: Create the Pipeline for Self-Training

In this step, we will create a pipeline for semi-supervised learning using Self-Training. The pipeline will be similar to the supervised pipeline, but we will use the SelfTrainingClassifier instead of the SGDClassifier.

```python
from sklearn.semi_supervised import SelfTrainingClassifier

# Create the Self-Training pipeline
st_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SelfTrainingClassifier(SGDClassifier(**sdg_params), verbose=True)),
    ]
)
```

### Step 5: Train and Evaluate the Self-Training Model

In this step, we will use Self-Training on 20% of the labeled data. We will randomly select 20% of the labeled data, train the model on that data, and then use the model to predict labels for the remaining unlabeled data.

```python
import numpy as np

# Select 20% of the training data
y_mask = np.random.rand(len(y_train)) < 0.2
X_20, y_20 = map(
    list, zip(*((x, y) for x, y, m in zip(X_train, y_train, y_mask) if m))
)

# Set the non-masked subset to be unlabeled
y_train[~y_mask] = -1

# Train and evaluate the Self-Training pipeline
st_pipeline.fit(X_train, y_train)
y_pred = st_pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```

### Step 6: Create the Pipeline for LabelSpreading

In this step, we will create a pipeline for semi-supervised learning using LabelSpreading. The pipeline will be similar to the supervised pipeline, but we will use the LabelSpreading algorithm instead of the SGDClassifier.

```python
from sklearn.semi_supervised import LabelSpreading
from sklearn.preprocessing import FunctionTransformer

# Create the LabelSpreading pipeline
ls_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("toarray", FunctionTransformer(lambda x: x.toarray())),
        ("clf", LabelSpreading()),
    ]
)
```

### Step 7: Train and Evaluate the LabelSpreading Model

In this step, we will use LabelSpreading on 20% of the labeled data. We will randomly select 20% of the labeled data, train the model on that data, and then use the model to predict labels for the remaining unlabeled data.

```python
# Train and evaluate the LabelSpreading pipeline
ls_pipeline.fit(X_train, y_train)
y_pred = ls_pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```

## Summary

In this lab, we learned how to perform semi-supervised classification on a text dataset using scikit-learn. We used Self-Training and LabelSpreading algorithms to train and test our models. Semi-supervised learning can be useful when there is a limited amount of labeled data available, and it can help improve the performance of a model by incorporating unlabeled data.
