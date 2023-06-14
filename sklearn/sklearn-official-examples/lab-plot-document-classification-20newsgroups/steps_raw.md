# Text Document Classification

## Introduction

This lab demonstrates how to use scikit-learn to classify text documents into different categories. We will use the 20 newsgroups dataset, which contains around 18,000 newsgroup posts on 20 topics. We will use a bag of words approach and a Tf-idf-weighted document-term sparse matrix to encode the features. The lab will also demonstrate various classifiers that can efficiently handle sparse matrices.

## Steps

### Step 1: Loading and Vectorizing the 20 Newsgroups Text Dataset

We define a function to load data from 20newsgroups_dataset, which comprises around 18,000 newsgroups posts on 20 topics split into two subsets: one for training and the other one for testing. We will load and vectorize the dataset without metadata stripping.

```python
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

categories = [
    "alt.atheism",
    "talk.religion.misc",
    "comp.graphics",
    "sci.space",
]

def load_dataset(verbose=False, remove=()):
    """Load and vectorize the 20 newsgroups dataset."""
    data_train = fetch_20newsgroups(
        subset="train",
        categories=categories,
        shuffle=True,
        random_state=42,
        remove=remove,
    )

    data_test = fetch_20newsgroups(
        subset="test",
        categories=categories,
        shuffle=True,
        random_state=42,
        remove=remove,
    )

    # order of labels in `target_names` can be different from `categories`
    target_names = data_train.target_names

    # split target in a training set and a test set
    y_train, y_test = data_train.target, data_test.target

    # Extracting features from the training data using a sparse vectorizer
    vectorizer = TfidfVectorizer(
        sublinear_tf=True, max_df=0.5, min_df=5, stop_words="english"
    )
    X_train = vectorizer.fit_transform(data_train.data)

    # Extracting features from the test data using the same vectorizer
    X_test = vectorizer.transform(data_test.data)

    feature_names = vectorizer.get_feature_names_out()

    if verbose:
        print(f"{len(data_train.data)} documents")
        print(f"{len(data_test.data)} documents")
        print(f"{len(target_names)} categories")
        print(f"n_samples: {X_train.shape[0]}, n_features: {X_train.shape[1]}")
        print(f"n_samples: {X_test.shape[0]}, n_features: {X_test.shape[1]}")

    return X_train, X_test, y_train, y_test, feature_names, target_names

X_train, X_test, y_train, y_test, feature_names, target_names = load_dataset(verbose=True)
```

### Step 2: Analysis of a Bag-of-Words Document Classifier

We will now train a classifier twice, once on the text samples including metadata and once after stripping the metadata. We will analyze the classification errors on a test set using a confusion matrix and inspect the coefficients that define the classification function of the trained models.

```python
from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

clf = RidgeClassifier(tol=1e-2, solver="sparse_cg")
clf.fit(X_train, y_train)
pred = clf.predict(X_test)

fig, ax = plt.subplots(figsize=(10, 5))
ConfusionMatrixDisplay.from_predictions(y_test, pred, ax=ax)
ax.xaxis.set_ticklabels(target_names)
ax.yaxis.set_ticklabels(target_names)
_ = ax.set_title(
    f"Confusion Matrix for {clf.__class__.__name__}\non the original documents"
)

def plot_feature_effects():
    # learned coefficients weighted by frequency of appearance
    average_feature_effects = clf.coef_ * np.asarray(X_train.mean(axis=0)).ravel()

    for i, label in enumerate(target_names):
        top5 = np.argsort(average_feature_effects[i])[-5:][::-1]
        if i == 0:
            top = pd.DataFrame(feature_names[top5], columns=[label])
            top_indices = top5
        else:
            top[label] = feature_names[top5]
            top_indices = np.concatenate((top_indices, top5), axis=None)
    top_indices = np.unique(top_indices)
    predictive_words = feature_names[top_indices]

    # plot feature effects
    bar_size = 0.25
    padding = 0.75
    y_locs = np.arange(len(top_indices)) * (4 * bar_size + padding)

    fig, ax = plt.subplots(figsize=(10, 8))
    for i, label in enumerate(target_names):
        ax.barh(
            y_locs + (i - 2) * bar_size,
            average_feature_effects[i, top_indices],
            height=bar_size,
            label=label,
        )
    ax.set(
        yticks=y_locs,
        yticklabels=predictive_words,
        ylim=[
            0 - 4 * bar_size,
            len(top_indices) * (4 * bar_size + padding) - 4 * bar_size,
        ],
    )
    ax.legend(loc="lower right")

    print("top 5 keywords per class:")
    print(top)

    return ax

_ = plot_feature_effects().set_title("Average feature effect on the original data")
```

### Step 3: Model with Metadata Stripping

We will now use the `remove` option of the 20 newsgroups dataset loader in scikit-learn to train a text classifier that does not rely too much on metadata to make its decisions. We will also analyze the classification errors on a test set using a confusion matrix and inspect the coefficients that define the classification function of the trained models.

```python
(
    X_train,
    X_test,
    y_train,
    y_test,
    feature_names,
    target_names,
) = load_dataset(remove=("headers", "footers", "quotes"))

clf = RidgeClassifier(tol=1e-2, solver="sparse_cg")
clf.fit(X_train, y_train)
pred = clf.predict(X_test)

fig, ax = plt.subplots(figsize=(10, 5))
ConfusionMatrixDisplay.from_predictions(y_test, pred, ax=ax)
ax.xaxis.set_ticklabels(target_names)
ax.yaxis.set_ticklabels(target_names)
_ = ax.set_title(
    f"Confusion Matrix for {clf.__class__.__name__}\non filtered documents"
)

_ = plot_feature_effects().set_title("Average feature effects on filtered documents")
```

### Step 4: Benchmarking Classifiers

We will now train and test the datasets with eight different classification models and get performance results for each model. The goal of this study is to highlight the computation/accuracy tradeoffs of different types of classifiers for such a multi-class text classification problem.

```python
from sklearn.utils.extmath import density
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import ComplementNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.ensemble import RandomForestClassifier

results = []
for clf, name in (
    (LogisticRegression(C=5, max_iter=1000), "Logistic Regression"),
    (RidgeClassifier(alpha=1.0, solver="sparse_cg"), "Ridge Classifier"),
    (KNeighborsClassifier(n_neighbors=100), "kNN"),
    (RandomForestClassifier(), "Random Forest"),
    # L2 penalty Linear SVC
    (LinearSVC(C=0.1, dual=False, max_iter=1000), "Linear SVC"),
    # L2 penalty Linear SGD
    (
        SGDClassifier(
            loss="log_loss", alpha=1e-4, n_iter_no_change=3, early_stopping=True
        ),
        "log-loss SGD",
    ),
    # NearestCentroid (aka Rocchio classifier)
    (NearestCentroid(), "NearestCentroid"),
    # Sparse naive Bayes classifier
    (ComplementNB(alpha=0.1), "Complement naive Bayes"),
):
    print("=" * 80)
    print(name)
    results.append(benchmark(clf, name))

indices = np.arange(len(results))

results = [[x[i] for x in results] for i in range(4)]

clf_names, score, training_time, test_time = results
training_time = np.array(training_time)
test_time = np.array(test_time)

fig, ax1 = plt.subplots(figsize=(10, 8))
ax1.scatter(score, training_time, s=60)
ax1.set(
    title="Score-training time trade-off",
    yscale="log",
    xlabel="test accuracy",
    ylabel="training time (s)",
)
fig, ax2 = plt.subplots(figsize=(10, 8))
ax2.scatter(score, test_time, s=60)
ax2.set(
    title="Score-test time trade-off",
    yscale="log",
    xlabel="test accuracy",
    ylabel="test time (s)",
)

for i, txt in enumerate(clf_names):
    ax1.annotate(txt, (score[i], training_time[i]))
    ax2.annotate(txt, (score[i], test_time[i]))
```

## Summary

This lab demonstrated how to use scikit-learn to classify text documents into different categories. We loaded the 20 newsgroups dataset and used a bag of words approach and a Tf-idf-weighted document-term sparse matrix to encode the features. We trained a classifier twice, once on the text samples including metadata and once after stripping the metadata. We analyzed the classification errors on a test set using a confusion matrix and inspected the coefficients that define the classification function of the trained models. We also trained and tested the datasets with eight different classification models and got performance results for each model. The goal of this study was to highlight the computation/accuracy tradeoffs of different types of classifiers for such a multi-class text classification problem.
