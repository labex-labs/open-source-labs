# Adjusting for Chance in Clustering Performance Evaluation

## Introduction

This lab explores the impact of uniformly-distributed random labeling on the behavior of some clustering evaluation metrics. Clustering algorithms are fundamentally unsupervised learning methods and evaluation metrics that leverage "supervised" ground truth information to quantify the quality of the resulting clusters. However, non-adjusted clustering evaluation metrics can be misleading as they output large values for fine-grained labelings, which can be totally random. Therefore, only adjusted measures can be safely used as a consensus index to evaluate the average stability of clustering algorithms for a given value of k on various overlapping sub-samples of the dataset.

## Steps

### Step 1: Defining the List of Metrics to Evaluate

We first define a list of metrics to be used to evaluate clustering algorithms. Examples of such metrics are V-measure, Rand index, Adjusted Rand index (ARI), Mutual Information (MI), Normalized Mutual Information (NMI), and Adjusted Mutual Information (AMI).

```python
from sklearn import metrics

score_funcs = [
    ("V-measure", metrics.v_measure_score),
    ("Rand index", metrics.rand_score),
    ("ARI", metrics.adjusted_rand_score),
    ("MI", metrics.mutual_info_score),
    ("NMI", metrics.normalized_mutual_info_score),
    ("AMI", metrics.adjusted_mutual_info_score),
]
```

### Step 2: Experiment 1 - Fixed Ground Truth Labels and Growing Number of Clusters

We create uniformly-distributed random labeling and use the `random_labels` function to create a fixed set of ground truth labels (`labels_a`) distributed in `n_classes` and then score several sets of randomly "predicted" labels (`labels_b`) to assess the variability of a given metric at a given `n_clusters`.

```python
rng = np.random.RandomState(0)

def random_labels(n_samples, n_classes):
    return rng.randint(low=0, high=n_classes, size=n_samples)

def fixed_classes_uniform_labelings_scores(
    score_func, n_samples, n_clusters_range, n_classes, n_runs=5
):
    scores = np.zeros((len(n_clusters_range), n_runs))
    labels_a = random_labels(n_samples=n_samples, n_classes=n_classes)

    for i, n_clusters in enumerate(n_clusters_range):
        for j in range(n_runs):
            labels_b = random_labels(n_samples=n_samples, n_classes=n_clusters)
            scores[i, j] = score_func(labels_a, labels_b)
    return scores
```

### Step 3: Plotting Experiment 1 Results

We plot the results of the first experiment using the `matplotlib` and `seaborn` libraries. The Rand index saturates for `n_clusters` > `n_classes`. Other non-adjusted measures such as the V-Measure show a linear dependency between the number of clusters and the number of samples. Adjusted for chance measure, such as ARI and AMI, display some random variations centered around a mean score of 0.0, independently of the number of samples and clusters.

```python
import matplotlib.pyplot as plt
import seaborn as sns

n_samples = 1000
n_classes = 10
n_clusters_range = np.linspace(2, 100, 10).astype(int)
plots = []
names = []

sns.color_palette("colorblind")
plt.figure(1)

for marker, (score_name, score_func) in zip("d^vx.,", score_funcs):
    scores = fixed_classes_uniform_labelings_scores(
        score_func, n_samples, n_clusters_range, n_classes=n_classes
    )
    plots.append(
        plt.errorbar(
            n_clusters_range,
            scores.mean(axis=1),
            scores.std(axis=1),
            alpha=0.8,
            linewidth=1,
            marker=marker,
        )[0]
    )
    names.append(score_name)

plt.title(
    "Clustering measures for random uniform labeling\n"
    f"against reference assignment with {n_classes} classes"
)
plt.xlabel(f"Number of clusters (Number of samples is fixed to {n_samples})")
plt.ylabel("Score value")
plt.ylim(bottom=-0.05, top=1.05)
plt.legend(plots, names, bbox_to_anchor=(0.5, 0.5))
plt.show()
```

### Step 4: Experiment 2 - Varying Number of Classes and Clusters

In this section, we define a similar function that uses several metrics to score 2 uniformly-distributed random labelings. In this case, the number of classes and assigned number of clusters are matched for each possible value in `n_clusters_range`.

```python
def uniform_labelings_scores(score_func, n_samples, n_clusters_range, n_runs=5):
    scores = np.zeros((len(n_clusters_range), n_runs))

    for i, n_clusters in enumerate(n_clusters_range):
        for j in range(n_runs):
            labels_a = random_labels(n_samples=n_samples, n_classes=n_clusters)
            labels_b = random_labels(n_samples=n_samples, n_classes=n_clusters)
            scores[i, j] = score_func(labels_a, labels_b)
    return scores
```

### Step 5: Plotting Experiment 2 Results

We plot the results of the second experiment using the `matplotlib` library. We observe similar results as for the first experiment: adjusted for chance metrics stay constantly near zero while other metrics tend to get larger with finer-grained labelings. The mean V-measure of random labeling increases significantly as the number of clusters is closer to the total number of samples used to compute the measure.

```python
n_samples = 100
n_clusters_range = np.linspace(2, n_samples, 10).astype(int)

plt.figure(2)

plots = []
names = []

for marker, (score_name, score_func) in zip("d^vx.,", score_funcs):
    scores = uniform_labelings_scores(score_func, n_samples, n_clusters_range)
    plots.append(
        plt.errorbar(
            n_clusters_range,
            np.median(scores, axis=1),
            scores.std(axis=1),
            alpha=0.8,
            linewidth=2,
            marker=marker,
        )[0]
    )
    names.append(score_name)

plt.title(
    "Clustering measures for 2 random uniform labelings\nwith equal number of clusters"
)
plt.xlabel(f"Number of clusters (Number of samples is fixed to {n_samples})")
plt.ylabel("Score value")
plt.legend(plots, names)
plt.ylim(bottom=-0.05, top=1.05)
plt.show()
```

## Summary

This lab explored the impact of uniformly-distributed random labeling on the behavior of some clustering evaluation metrics. The results indicated that non-adjusted clustering evaluation metrics can be misleading, and only adjusted measures can be safely used as a consensus index to evaluate the average stability of clustering algorithms for a given value of k on various overlapping sub-samples of the dataset.
