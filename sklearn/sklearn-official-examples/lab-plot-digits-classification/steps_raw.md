# Recognizing Hand-written Digits

## Introduction

This lab demonstrates how to use scikit-learn to recognize images of hand-written digits from 0-9.

## Steps

### Step 1: Import Libraries

First, we need to import the necessary libraries. We will use `matplotlib` for visualization, `datasets` and `metrics` from `sklearn` to load and evaluate the dataset, and `svm` for training the support vector machine.

```python
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
```

### Step 2: Load and Visualize the Digits Dataset

We will load the digits dataset which consists of 8x8 pixel images of digits. We will use `imshow()` method from `matplotlib` to visualize the first 4 images along with their corresponding labels.

```python
digits = datasets.load_digits()

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title("Training: %i" % label)
```

### Step 3: Prepare the Dataset

We need to flatten the images to turn each 2-D array of grayscale values from shape `(8, 8)` into shape `(64,)`. This will give us a dataset of shape `(n_samples, n_features)`, where `n_samples` is the number of images and `n_features` is the total number of pixels in each image.

```python
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
```

### Step 4: Split the Dataset

We will split the dataset into 50% train and 50% test subsets using `train_test_split()` method from `sklearn.model_selection`.

```python
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)
```

### Step 5: Train the Support Vector Machine

We will train a support vector classifier on the train samples using `svm.SVC()` method from `sklearn`.

```python
clf = svm.SVC(gamma=0.001)
clf.fit(X_train, y_train)
```

### Step 6: Predict and Evaluate the Model

We will use the trained model to predict the value of the digits for the samples in the test subset. Then, we will evaluate the model using `metrics.classification_report()` and `metrics.ConfusionMatrixDisplay.from_predictions()` methods from `sklearn.metrics`.

```python
predicted = clf.predict(X_test)

print(
    f"Classification report for classifier {clf}:\n"
    f"{metrics.classification_report(y_test, predicted)}\n"
)

disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, predicted)
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")
```

### Step 7: Rebuild Classification Report from Confusion Matrix

If the results from evaluating a classifier are stored in the form of a confusion matrix and not in terms of `y_true` and `y_pred`, we can still build a classification report using `metrics.classification_report()` method as follows:

```python
y_true = []
y_pred = []
cm = disp.confusion_matrix

for gt in range(len(cm)):
    for pred in range(len(cm)):
        y_true += [gt] * cm[gt][pred]
        y_pred += [pred] * cm[gt][pred]

print(
    "Classification report rebuilt from confusion matrix:\n"
    f"{metrics.classification_report(y_true, y_pred)}\n"
)
```

## Summary

In this lab, we learned how to use scikit-learn to recognize hand-written digits from 0-9 using support vector machine. We loaded and visualized the digits dataset, prepared and split the dataset, trained the model, predicted and evaluated the model using classification report and confusion matrix.
