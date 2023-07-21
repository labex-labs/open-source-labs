# Feature Discretization

## Introduction

In machine learning, feature discretization is a method of reducing the number of continuous variables in a dataset by creating bins or intervals to represent them. This method can be useful in cases where the number of continuous variables is large, and the algorithm needs to be simplified for easier analysis. In this lab, we will demonstrate feature discretization on synthetic classification datasets.

## Steps

### Step 1: Import Libraries

In this step, we will import the required libraries for the lab. We will be using the scikit-learn library for machine learning tasks, numpy for mathematical operations, and matplotlib for data visualization.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning
```

### Step 2: Prepare the Data

In this step, we will prepare the synthetic classification datasets for feature discretization. We will use the scikit-learn library to generate three different datasets: moons, concentric circles, and linearly separable data.

```python
h = 0.02  # step size in the mesh

n_samples = 100
datasets = [
    make_moons(n_samples=n_samples, noise=0.2, random_state=0),
    make_circles(n_samples=n_samples, noise=0.2, factor=0.5, random_state=1),
    make_classification(
        n_samples=n_samples,
        n_features=2,
        n_redundant=0,
        n_informative=2,
        random_state=2,
        n_clusters_per_class=1,
    ),
]
```

### Step 3: Define Classifiers and Parameters

In this step, we will define the classifiers and parameters to be used in the feature discretization process. We will create a list of classifiers that includes logistic regression, linear support vector machine (SVM), gradient boosting classifier, and SVM with a radial basis function kernel. We will also define a set of parameters for each classifier to be used in the GridSearchCV algorithm.

```python
# list of (estimator, param_grid), where param_grid is used in GridSearchCV
# The parameter spaces in this example are limited to a narrow band to reduce
# its runtime. In a real use case, a broader search space for the algorithms
# should be used.
classifiers = [
    (
        make_pipeline(StandardScaler(), LogisticRegression(random_state=0)),
        {"logisticregression__C": np.logspace(-1, 1, 3)},
    ),
    (
        make_pipeline(StandardScaler(), LinearSVC(random_state=0, dual="auto")),
        {"linearsvc__C": np.logspace(-1, 1, 3)},
    ),
    (
        make_pipeline(
            StandardScaler(),
            KBinsDiscretizer(encode="onehot"),
            LogisticRegression(random_state=0),
        ),
        {
            "kbinsdiscretizer__n_bins": np.arange(5, 8),
            "logisticregression__C": np.logspace(-1, 1, 3),
        },
    ),
    (
        make_pipeline(
            StandardScaler(),
            KBinsDiscretizer(encode="onehot"),
            LinearSVC(random_state=0, dual="auto"),
        ),
        {
            "kbinsdiscretizer__n_bins": np.arange(5, 8),
            "linearsvc__C": np.logspace(-1, 1, 3),
        },
    ),
    (
        make_pipeline(
            StandardScaler(), GradientBoostingClassifier(n_estimators=5, random_state=0)
        ),
        {"gradientboostingclassifier__learning_rate": np.logspace(-2, 0, 5)},
    ),
    (
        make_pipeline(StandardScaler(), SVC(random_state=0)),
        {"svc__C": np.logspace(-1, 1, 3)},
    ),
]

names = [get_name(e).replace("StandardScaler + ", "") for e, _ in classifiers]
```

### Step 4: Visualize the Data

In this step, we will visualize the synthetic classification datasets before feature discretization. We will plot the training and testing points for each dataset.

```python
fig, axes = plt.subplots(
    nrows=len(datasets), ncols=len(classifiers) + 1, figsize=(21, 9)
)

cm_piyg = plt.cm.PiYG
cm_bright = ListedColormap(["#b30065", "#178000"])

# iterate over datasets
for ds_cnt, (X, y) in enumerate(datasets):
    print(f"\ndataset {ds_cnt}\n---------")

    # split into training and test part
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.5, random_state=42
    )

    # create the grid for background colors
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # plot the dataset first
    ax = axes[ds_cnt, 0]
    if ds_cnt == 0:
        ax.set_title("Input data")
    # plot the training points
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolors="k")
    # and testing points
    ax.scatter(
        X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6, edgecolors="k"
    )
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xticks(())
    ax.set_yticks(())
```

### Step 5: Implement Feature Discretization

In this step, we will implement feature discretization on the datasets using the KBinsDiscretizer class from scikit-learn. This will discretize the features by creating a set of bins and then one-hot encoding the discrete values. We will then fit the data to a linear classifier and evaluate the performance.

```python
# iterate over classifiers
for est_idx, (name, (estimator, param_grid)) in enumerate(zip(names, classifiers)):
    ax = axes[ds_cnt, est_idx + 1]

    clf = GridSearchCV(estimator=estimator, param_grid=param_grid)
    with ignore_warnings(category=ConvergenceWarning):
        clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    print(f"{name}: {score:.2f}")

    # plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]*[y_min, y_max].
    if hasattr(clf, "decision_function"):
        Z = clf.decision_function(np.column_stack([xx.ravel(), yy.ravel()]))
    else:
        Z = clf.predict_proba(np.column_stack([xx.ravel(), yy.ravel()]))[:, 1]

    # put the result into a color plot
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap=cm_piyg, alpha=0.8)

    # plot the training points
    ax.scatter(
        X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolors="k"
    )
    # and testing points
    ax.scatter(
        X_test[:, 0],
        X_test[:, 1],
        c=y_test,
        cmap=cm_bright,
        edgecolors="k",
        alpha=0.6,
    )
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xticks(())
    ax.set_yticks(())

    if ds_cnt == 0:
        ax.set_title(name.replace(" + ", "\n"))
    ax.text(
        0.95,
        0.06,
        (f"{score:.2f}").lstrip("0"),
        size=15,
        bbox=dict(boxstyle="round", alpha=0.8, facecolor="white"),
        transform=ax.transAxes,
        horizontalalignment="right",
    )
```

### Step 6: Visualize Results

In this step, we will visualize the results of the feature discretization process. We will plot the classification accuracy on the test set for each classifier and dataset.

```python
plt.tight_layout()

# Add suptitles above the figure
plt.subplots_adjust(top=0.90)
suptitles = [
    "Linear classifiers",
    "Feature discretization and linear classifiers",
    "Non-linear classifiers",
]
for i, suptitle in zip([1, 3, 5], suptitles):
    ax = axes[0, i]
    ax.text(
        1.05,
        1.25,
        suptitle,
        transform=ax.transAxes,
        horizontalalignment="center",
        size="x-large",
    )
plt.show()
```

## Summary

In this lab, we demonstrated feature discretization on synthetic classification datasets using scikit-learn. We prepared the data, defined classifiers and parameters, implemented feature discretization, and visualized the results. This preprocessing technique can be useful in reducing the complexity of a dataset and improving the performance of linear classifiers. However, it should be used with caution and in conjunction with other techniques to avoid overfitting.
