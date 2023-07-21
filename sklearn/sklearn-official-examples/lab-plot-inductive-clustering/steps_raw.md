# Inductive Clustering

## Introduction

In this lab, we will learn about inductive clustering, a method that extends clustering by inducing a classifier from the cluster labels. We will use scikit-learn library in Python to implement a meta-estimator which extends clustering.

## Steps

### Step 1: Generate Training Data

In this step, we will generate some training data from clustering. We will use the `make_blobs` function from scikit-learn to generate 5000 samples with 3 clusters having different standard deviations and centers.

```python
X, y = make_blobs(
    n_samples=5000,
    cluster_std=[1.0, 1.0, 0.5],
    centers=[(-5, -5), (0, 0), (5, 5)],
    random_state=42,
)
```

### Step 2: Train Clustering Algorithm

In this step, we will train a clustering algorithm on the generated training data and get the cluster labels. We will use `AgglomerativeClustering` from scikit-learn to train the algorithm with 3 clusters.

```python
clusterer = AgglomerativeClustering(n_clusters=3)
cluster_labels = clusterer.fit_predict(X)
```

### Step 3: Generate New Samples

In this step, we will generate new samples and plot them along with the original dataset. We will use the `make_blobs` function again to generate 10 new samples.

```python
X_new, y_new = make_blobs(
    n_samples=10, centers=[(-7, -1), (-2, 4), (3, 6)], random_state=42
)
```

### Step 4: Declare Inductive Learning Model

In this step, we will declare the inductive learning model that will be used to predict cluster membership for unknown instances. We will use `RandomForestClassifier` from scikit-learn as the classifier.

```python
classifier = RandomForestClassifier(random_state=42)
inductive_learner = InductiveClusterer(clusterer, classifier).fit(X)
```

### Step 5: Predict Cluster Membership for Unknown Instances

In this step, we will use the inductive learning model to predict the cluster membership for the generated new samples. We will use the `predict` function from the `InductiveClusterer` class and plot the new samples with their probable clusters.

```python
probable_clusters = inductive_learner.predict(X_new)

plt.subplot(133)
plot_scatter(X, cluster_labels)
plot_scatter(X_new, probable_clusters)
plt.title("Classify unknown instances")
```

## Summary

In this lab, we learned about inductive clustering, a method that extends clustering by inducing a classifier from the cluster labels. We used scikit-learn library in Python to implement a meta-estimator which extends clustering and trained a clustering algorithm on the generated training data. We also generated new samples and used the inductive learning model to predict the cluster membership for the new samples.
