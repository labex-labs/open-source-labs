# Statistical Learning

## Introduction

In this lab, we will explore the setting and the estimator object in scikit-learn, a popular machine learning library in Python. We will learn about datasets, which are represented as 2D arrays, and how to preprocess them for scikit-learn. We will also explore the concept of estimator objects, which are used to learn from data and make predictions.

## Steps

### Step 1: Understanding Datasets

Scikit-learn represents datasets as 2D arrays, where the first axis represents the samples and the second axis represents the features. Let's take a look at an example using the iris dataset:

```python
from sklearn import datasets

iris = datasets.load_iris()
data = iris.data
print(data.shape)
```

Output:

```
(150, 4)
```

The iris dataset consists of 150 observations of irises, with each observation described by 4 features. The shape of the data array is (150, 4).

### Step 2: Reshaping Data

Sometimes the data may not be initially in the shape required by scikit-learn. In such cases, we need to preprocess the data to transform it into the `(n_samples, n_features)` shape. An example of reshaping data is the digits dataset, which consists of 1797 8x8 images of hand-written digits:

```python
digits = datasets.load_digits()
print(digits.images.shape)
```

Output:

```
(1797, 8, 8)
```

To use this dataset with scikit-learn, we need to reshape each 8x8 image into a feature vector of length 64:

```python
data = digits.images.reshape((digits.images.shape[0], -1))
```

### Step 3: Estimator Objects

Estimator objects in scikit-learn are used to learn from data and make predictions. They can be classification, regression, or clustering algorithms, or transformers that extract useful features from raw data. Let's create a simple example of an estimator object:

```python
from sklearn.base import BaseEstimator

class Estimator(BaseEstimator):
    def __init__(self, param1=0, param2=0):
        self.param1 = param1
        self.param2 = param2

    def fit(self, data):
        # Implementation of the fit method
        pass

estimator = Estimator()
```

### Step 4: Fitting Data

The main API implemented by scikit-learn is the `fit` method of an estimator object. It takes a dataset (usually a 2D array) as input. To fit data with an estimator, we can call the `fit` method:

```python
estimator.fit(data)
```

### Step 5: Estimator Parameters

Estimator objects can have parameters that affect their behavior. These parameters can be set when the estimator is instantiated or by modifying the corresponding attribute. Let's set some parameters for our example estimator:

```python
estimator = Estimator(param1=1, param2=2)
print(estimator.param1)
```

Output:

```
1
```

### Step 6: Estimated Parameters

When data is fitted with an estimator, the parameters are estimated from the data. All the estimated parameters are attributes of the estimator object, ending with an underscore. For example:

```python
print(estimator.estimated_param_)
```

### Summary

In this lab, we learned about datasets in scikit-learn, how to reshape data, and the concept of estimator objects. We explored fitting data with an estimator, setting parameters, and accessing estimated parameters. This understanding of the setting and the estimator object will be essential when working with scikit-learn for statistical learning tasks.
