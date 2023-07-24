# Preprocessing Data

## Introduction

In this lab, we will explore the preprocessing techniques available in scikit-learn. Preprocessing is an essential step in any machine learning workflow as it helps to transform raw data into a suitable format for the learning algorithm. We will cover various preprocessing techniques such as standardization, scaling, normalization, encoding categorical features, imputing missing values, generating polynomial features, and creating custom transformers.

## Steps

1. Standardization
2. Scaling
3. Normalization
4. Encoding Categorical Features
5. Imputation of Missing Values
6. Generating Polynomial Features
7. Creating Custom Transformers

### Step 1: Standardization

Standardization is a common preprocessing step for many machine learning algorithms. It transforms features to have zero mean and unit variance. We can use the `StandardScaler` from scikit-learn to perform standardization.

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

# Create a sample dataset
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit the scaler on the training data
scaler.fit(X)

# Transform the training data
X_scaled = scaler.transform(X)

# Print the transformed data
print(X_scaled)
```

### Step 2: Scaling

Scaling features to a specific range is another common preprocessing technique. It is useful when features have different scales and we want to bring them all to a similar range. The `MinMaxScaler` and `MaxAbsScaler` can be used to perform scaling.

```python
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler
import numpy as np

# Create a sample dataset
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Initialize the MinMaxScaler
min_max_scaler = MinMaxScaler()

# Fit and transform the training data
X_minmax = min_max_scaler.fit_transform(X)

# Print the transformed data
print(X_minmax)

# Initialize the MaxAbsScaler
max_abs_scaler = MaxAbsScaler()

# Fit and transform the training data
X_maxabs = max_abs_scaler.fit_transform(X)

# Print the transformed data
print(X_maxabs)
```

### Step 3: Normalization

Normalization is the process of scaling individual samples to have unit norm. It is commonly used when the magnitude of the data is not important and we are only interested in the direction (or angle) of the data. We can use the `Normalizer` from scikit-learn to perform normalization.

```python
from sklearn.preprocessing import Normalizer
import numpy as np

# Create a sample dataset
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Initialize the Normalizer
normalizer = Normalizer()

# Fit and transform the training data
X_normalized = normalizer.fit_transform(X)

# Print the transformed data
print(X_normalized)
```

### Step 4: Encoding Categorical Features

Categorical features need to be encoded into numerical values before they can be used in machine learning algorithms. We can use the `OrdinalEncoder` and `OneHotEncoder` from scikit-learn to encode categorical features.

```python
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
import numpy as np

# Create a sample dataset
X = [['male', 'from US', 'uses Safari'],
     ['female', 'from Europe', 'uses Firefox']]

# Initialize the OrdinalEncoder
ordinal_encoder = OrdinalEncoder()

# Fit and transform the training data
X_encoded = ordinal_encoder.fit_transform(X)

# Print the transformed data
print(X_encoded)

# Initialize the OneHotEncoder
onehot_encoder = OneHotEncoder()

# Fit and transform the training data
X_onehot = onehot_encoder.fit_transform(X)

# Print the transformed data
print(X_onehot.toarray())
```

### Step 5: Imputation of Missing Values

Missing values in a dataset can cause issues with machine learning algorithms. We can use the methods provided in scikit-learn's `impute` module to handle missing values. Here, we will use the `SimpleImputer` to impute missing values.

```python
from sklearn.impute import SimpleImputer
import numpy as np

# Create a sample dataset with missing values
X = np.array([[1., 2., np.nan],
              [3., np.nan, 5.],
              [np.nan, 4., 6.]])

# Initialize the SimpleImputer
imputer = SimpleImputer()

# Fit and transform the training data
X_imputed = imputer.fit_transform(X)

# Print the transformed data
print(X_imputed)
```

### Step 6: Generating Polynomial Features

Sometimes it is beneficial to add complexity to a model by considering nonlinear features of the input data. We can use the `PolynomialFeatures` from scikit-learn to generate polynomial features.

```python
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Create a sample dataset
X = np.array([[0, 1],
              [2, 3],
              [4, 5]])

# Initialize the PolynomialFeatures
poly = PolynomialFeatures(2)

# Fit and transform the training data
X_poly = poly.fit_transform(X)

# Print the transformed data
print(X_poly)
```

### Step 7: Creating Custom Transformers

In some cases, we may want to convert an existing Python function into a transformer to assist in data cleaning or processing. We can achieve this using the `FunctionTransformer` from scikit-learn.

```python
from sklearn.preprocessing import FunctionTransformer
import numpy as np

# Create a custom function
def custom_function(X):
    return np.log1p(X)

# Initialize the FunctionTransformer
transformer = FunctionTransformer(custom_function)

# Create a sample dataset
X = np.array([[0, 1],
              [2, 3]])

# Transform the data using the custom function
X_transformed = transformer.transform(X)

# Print the transformed data
print
```
