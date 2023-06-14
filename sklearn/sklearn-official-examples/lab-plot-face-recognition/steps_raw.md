# Face Recognition with Eigenfaces and SVMs

## Introduction

This lab will guide you through the steps to perform face recognition using eigenfaces and Support Vector Machines (SVMs). The dataset used in this lab is a preprocessed excerpt of the "Labeled Faces in the Wild" dataset.

## Steps

### Step 1: Import Libraries

```python
from time import time
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from sklearn.datasets import fetch_lfw_people
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from scipy.stats import loguniform
```

First, we need to import all the necessary libraries.

### Step 2: Load and Explore Dataset

```python
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
n_samples, h, w = lfw_people.images.shape
X = lfw_people.data
n_features = X.shape[1]
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]
```

We download the dataset using the `fetch_lfw_people()` function from scikit-learn. We then explore the dataset by getting the number of samples, height, and width of the images. We also get the input data `X`, target `y`, target names `target_names`, and number of classes `n_classes`.

### Step 3: Data Preprocessing

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

We split the dataset into a training set and a test set and preprocess the data by scaling the input data using the `StandardScaler()` function.

### Step 4: Perform PCA

```python
n_components = 150

pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
eigenfaces = pca.components_.reshape((n_components, h, w))

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
```

We perform Principal Component Analysis (PCA) to extract features from the input data. We set the number of components to 150 and fit the PCA model to the training data. We then get the eigenfaces and transform the input data into principal components.

### Step 5: Train a Support Vector Machine (SVM) Classification Model

```python
param_grid = {
    "C": loguniform(1e3, 1e5),
    "gamma": loguniform(1e-4, 1e-1),
}

clf = RandomizedSearchCV(
    SVC(kernel="rbf", class_weight="balanced"), param_grid, n_iter=10
)
clf = clf.fit(X_train_pca, y_train)
```

We train a SVM classification model using the transformed data. We use `RandomizedSearchCV()` to find the best hyperparameters for the SVM model.

### Step 6: Evaluate Model Performance

```python
y_pred = clf.predict(X_test_pca)
print(classification_report(y_test, y_pred, target_names=target_names))
ConfusionMatrixDisplay.from_estimator(
    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation="vertical"
)
```

We predict the target values using the test data and evaluate the model performance using the `classification_report()` function. We also plot the confusion matrix using the `ConfusionMatrixDisplay()` function.

### Step 7: Visualize Predictions

```python
def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    """Helper function to plot a gallery of portraits"""
    plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    plt.subplots_adjust(bottom=0, left=0.01, right=0.99, top=0.90, hspace=0.35)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())

prediction_titles = [
    title(y_pred, y_test, target_names, i) for i in range(y_pred.shape[0])
]

plot_gallery(X_test, prediction_titles, h, w)
```

We visualize the predictions by plotting a gallery of portraits with their predicted and true names.

### Step 8: Visualize Eigenfaces

```python
eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

plt.show()
```

We also plot the eigenfaces to visualize the features extracted from the input data.

## Summary

In this lab, we learned how to perform face recognition using eigenfaces and SVMs. We first loaded and explored the dataset, then preprocessed the data by scaling the input data. We then performed PCA to extract features from the input data and trained a SVM classification model. We evaluated the model performance and visualized the predictions and eigenfaces.
