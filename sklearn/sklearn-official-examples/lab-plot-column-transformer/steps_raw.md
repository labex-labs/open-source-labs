# Scikit-Learn Column Transformer

## Introduction

In this lab, we will learn how to use Scikit-Learn's `ColumnTransformer` on a dataset that contains different types of features. This technique is useful when a dataset contains components that require different feature extraction and processing pipelines.

## Steps

### Step 1: Dataset

We will use the 20 newsgroups dataset, which consists of posts from newsgroups on 20 topics. The dataset is split into train and test subsets based on messages posted before and after a specific date. We will only use posts from 2 categories to speed up running time.

```python
categories = ["sci.med", "sci.space"]
X_train, y_train = fetch_20newsgroups(
    random_state=1,
    subset="train",
    categories=categories,
    remove=("footers", "quotes"),
    return_X_y=True,
)
X_test, y_test = fetch_20newsgroups(
    random_state=1,
    subset="test",
    categories=categories,
    remove=("footers", "quotes"),
    return_X_y=True,
)
```

### Step 2: Creating Transformers

We will create transformers that extract features from the dataset. We will define two functions that perform the data transformation then use Scikit-Learn's `FunctionTransformer` to create transformers.

```python
def subject_body_extractor(posts):
    # construct object dtype array with two columns
    # first column = 'subject' and second column = 'body'
    features = np.empty(shape=(len(posts), 2), dtype=object)
    for i, text in enumerate(posts):
        # temporary variable `_` stores '\n\n'
        headers, _, body = text.partition("\n\n")
        # store body text in second column
        features[i, 1] = body

        prefix = "Subject:"
        sub = ""
        # save text after 'Subject:' in first column
        for line in headers.split("\n"):
            if line.startswith(prefix):
                sub = line[len(prefix) :]
                break
        features[i, 0] = sub

    return features

subject_body_transformer = FunctionTransformer(subject_body_extractor)

def text_stats(posts):
    return [{"length": len(text), "num_sentences": text.count(".")} for text in posts]

text_stats_transformer = FunctionTransformer(text_stats)
```

### Step 3: Classification Pipeline

We will create a pipeline that extracts features from the dataset, combines them, and trains a classifier on the combined set of features. We will use Scikit-Learn's `Pipeline` and `ColumnTransformer` to achieve this.

```python
pipeline = Pipeline(
    [
        # Extract subject & body
        ("subjectbody", subject_body_transformer),
        # Use ColumnTransformer to combine the subject and body features
        (
            "union",
            ColumnTransformer(
                [
                    # bag-of-words for subject (col 0)
                    ("subject", TfidfVectorizer(min_df=50), 0),
                    # bag-of-words with decomposition for body (col 1)
                    (
                        "body_bow",
                        Pipeline(
                            [
                                ("tfidf", TfidfVectorizer()),
                                ("best", TruncatedSVD(n_components=50)),
                            ]
                        ),
                        1,
                    ),
                    # Pipeline for pulling text stats from post's body
                    (
                        "body_stats",
                        Pipeline(
                            [
                                (
                                    "stats",
                                    text_stats_transformer,
                                ),  # returns a list of dicts
                                (
                                    "vect",
                                    DictVectorizer(),
                                ),  # list of dicts -> feature matrix
                            ]
                        ),
                        1,
                    ),
                ],
                # weight above ColumnTransformer features
                transformer_weights={
                    "subject": 0.8,
                    "body_bow": 0.5,
                    "body_stats": 1.0,
                },
            ),
        ),
        # Use a SVC classifier on the combined features
        ("svc", LinearSVC(dual=False)),
    ],
    verbose=True,
)
```

### Step 4: Training and Testing

We will fit our pipeline on the training data and use it to predict topics for `X_test`. Performance metrics of our pipeline are then printed.

```python
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print("Classification report:\n\n{}".format(classification_report(y_test, y_pred)))
```

## Summary

In this lab, we learned how to use Scikit-Learn's `ColumnTransformer` on a dataset containing different types of features. We created transformers that extracted features from the dataset and used them to train a classifier on the combined set of features. The `ColumnTransformer` allowed us to process the different types of features in a single pipeline.
