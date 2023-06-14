# Semi-Supervised Learning with Label Spreading

## Introduction

This lab demonstrates how to perform semi-supervised learning using the Label Spreading algorithm. We will use a subset of the handwritten digit dataset and only 40 of these samples will be labeled. We will then use Label Spreading to predict the remaining 300 samples.

## Steps

### Step 1: Load and Shuffle Data

We first load the digits dataset and randomly shuffle the data.

```python
digits = datasets.load_digits()
rng = np.random.RandomState(2)
indices = np.arange(len(digits.data))
rng.shuffle(indices)
```

### Step 2: Prepare Data for Semi-Supervised Learning

We select 340 samples and only 40 of these samples are associated with a known label. We store the indices of the 300 other samples for which we are not supposed to know their labels. We then shuffle the labels so that the unlabeled samples are marked with -1.

```python
X = digits.data[indices[:340]]
y = digits.target[indices[:340]]

n_total_samples = len(y)
n_labeled_points = 40

indices = np.arange(n_total_samples)

unlabeled_set = indices[n_labeled_points:]

y_train = np.copy(y)
y_train[unlabeled_set] = -1
```

### Step 3: Train the Label Spreading Model

We train the Label Spreading model with gamma=0.25 and max_iter=20.

```python
lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
```

### Step 4: Evaluate Model Performance

We evaluate the performance of the model by generating a classification report and a confusion matrix.

```python
predicted_labels = lp_model.transduction_[unlabeled_set]
true_labels = y[unlabeled_set]

print(
    "Label Spreading model: %d labeled & %d unlabeled points (%d total)"
    % (n_labeled_points, n_total_samples - n_labeled_points, n_total_samples)
)

print(classification_report(true_labels, predicted_labels))

ConfusionMatrixDisplay.from_predictions(
    true_labels, predicted_labels, labels=lp_model.classes_
)
```

### Step 5: Plot the Most Uncertain Predictions

We pick and show the top 10 most uncertain predictions.

```python
pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)

uncertainty_index = np.argsort(pred_entropies)[-10:]

f = plt.figure(figsize=(7, 5))
for index, image_index in enumerate(uncertainty_index):
    image = images[image_index]

    sub = f.add_subplot(2, 5, index + 1)
    sub.imshow(image, cmap=plt.cm.gray_r)
    plt.xticks([])
    plt.yticks([])
    sub.set_title(
        "predict: %i\ntrue: %i" % (lp_model.transduction_[image_index], y[image_index])
    )

f.suptitle("Learning with small amount of labeled data")
plt.show()
```

## Summary

In this lab, we demonstrated how to perform semi-supervised learning using the Label Spreading algorithm. We trained the model with a small amount of labeled data and used it to predict the labels of the remaining samples. The model performed well and correctly predicted the labels of most samples.
