# Comparison of Calibration of Classifiers

## Introduction

In this lab, we will compare the calibration of four different models: Logistic Regression, Gaussian Naive Bayes, Random Forest Classifier, and Linear SVM. Calibration curves will be plotted for each model, which show the relationship between predicted probabilities and actual outcomes. This is important because well-calibrated models produce probabilities that are accurate and reliable.

## Steps

### Step 1: Import Libraries and Generate Dataset

We start by importing the necessary libraries and generating a synthetic binary classification dataset with 100,000 samples and 20 features. Of the 20 features, only 2 are informative, 2 are redundant, and the remaining 16 are uninformative. Of the 100,000 samples, 100 will be used for model fitting and the remaining for testing.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generate dataset
X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=2, random_state=42
)

train_samples = 100  # Samples used for training the models
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    shuffle=False,
    test_size=100_000 - train_samples,
)
```

### Step 2: Plot Calibration Curves

We train each of the four models with the small training dataset and plot calibration curves using predicted probabilities of the test dataset. Calibration curves are created by binning predicted probabilities, then plotting the mean predicted probability in each bin against the observed frequency ('fraction of positives'). Below the calibration curve, we plot a histogram showing the distribution of the predicted probabilities or more specifically, the number of samples in each predicted probability bin.

```python
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibrationDisplay
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Create classifiers
lr = LogisticRegression()
gnb = GaussianNB()
svc = NaivelyCalibratedLinearSVC(C=1.0, dual="auto")
rfc = RandomForestClassifier()

clf_list = [
    (lr, "Logistic"),
    (gnb, "Naive Bayes"),
    (svc, "SVC"),
    (rfc, "Random forest"),
]

fig = plt.figure(figsize=(10, 10))
gs = GridSpec(4, 2)
colors = plt.get_cmap("Dark2")

ax_calibration_curve = fig.add_subplot(gs[:2, :2])
calibration_displays = {}
markers = ["^", "v", "s", "o"]
for i, (clf, name) in enumerate(clf_list):
    clf.fit(X_train, y_train)
    display = CalibrationDisplay.from_estimator(
        clf,
        X_test,
        y_test,
        n_bins=10,
        name=name,
        ax=ax_calibration_curve,
        color=colors(i),
        marker=markers[i],
    )
    calibration_displays[name] = display

ax_calibration_curve.grid()
ax_calibration_curve.set_title("Calibration plots")

# Add histogram
grid_positions = [(2, 0), (2, 1), (3, 0), (3, 1)]
for i, (_, name) in enumerate(clf_list):
    row, col = grid_positions[i]
    ax = fig.add_subplot(gs[row, col])

    ax.hist(
        calibration_displays[name].y_prob,
        range=(0, 1),
        bins=10,
        label=name,
        color=colors(i),
    )
    ax.set(title=name, xlabel="Mean predicted probability", ylabel="Count")

plt.tight_layout()
plt.show()
```

### Step 3: Interpret Calibration Curves

The calibration curves show the relationship between predicted probabilities and actual outcomes for each model. Well-calibrated models produce curves that follow the diagonal line, indicating that predicted probabilities match actual outcomes. The four models produce different results:

- Logistic regression produces well-calibrated predictions as it directly optimizes log-loss.
- Gaussian Naive Bayes tends to push probabilities to 0 or 1, mainly because the naive Bayes equation only provides a correct estimate of probabilities when the assumption that features are conditionally independent holds.
- Random Forest Classifier shows the opposite behavior: the histograms show peaks at approx. 0.2 and 0.9 probability, while probabilities close to 0 or 1 are very rare.
- Linear SVM shows an even more sigmoid curve than the Random Forest Classifier, which is typical for maximum-margin methods.

### Step 4: Conclusion

In this lab, we compared the calibration of four different models: Logistic Regression, Gaussian Naive Bayes, Random Forest Classifier, and Linear SVM. We plotted calibration curves for each model and observed that well-calibrated models produce curves that follow the diagonal line. The four models produced different results, with Logistic Regression being well calibrated and the other models showing varying degrees of bias. Calibration is an important aspect of machine learning models, and well-calibrated models produce probabilities that are accurate and reliable.
