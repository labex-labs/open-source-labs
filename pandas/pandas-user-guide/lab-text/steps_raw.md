# Text Data Handling in Pandas

## Introduction

This lab introduces how to handle text data in pandas. We will learn how to store text data, use string methods for data preprocessing and transformation, and extract substrings using regular expressions. We will also learn how to create dummy variables for machine learning algorithms.

## Steps

### Step 1: Store Text Data

In pandas, you can store text data in two ways: using an `object` dtype NumPy array or a `StringDtype` extension type. We recommend using `StringDtype` because it's safer and more specific than the generic `object` dtype.

```python
import pandas as pd

# create a series with `object` dtype
s1 = pd.Series(["a", "b", "c"], dtype="object")

# create a series with `StringDtype`
s2 = pd.Series(["a", "b", "c"], dtype="string")
```

### Step 2: Use String Methods

Pandas provides a suite of string processing methods that make it easy to operate on string data. These methods automatically exclude missing/NA values.

```python
s = pd.Series(
    ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"], dtype="string"
)

# convert to lowercase
s.str.lower()

# convert to uppercase
s.str.upper()

# calculate the length of each string
s.str.len()
```

### Step 3: Extract Substrings

You can extract substrings using regular expressions. The `extract` method accepts a regular expression with at least one capture group.

```python
# extract the first digit from each string
s = pd.Series(["a1", "b2", "c3"], dtype="string")
s.str.extract(r"(\d)", expand=False)
```

### Step 4: Test for Strings

You can check whether elements contain or match a pattern using the `contains` and `match` methods respectively.

```python
# check if each string contains the pattern "a"
s.str.contains("a", na=False)

# check if each string matches the pattern "a"
s.str.match("a", na=False)
```

### Step 5: Create Dummy Variables

You can create dummy variables from string data using the `get_dummies` method.

```python
# create dummy variables
s = pd.Series(["a", "a|b", np.nan, "a|c"], dtype="string")
s.str.get_dummies(sep="|")
```

## Summary

In this lab, we learned how to handle text data in pandas. We learned how to store text data, use string methods for data preprocessing and transformation, extract substrings using regular expressions, test whether elements contain or match a pattern, and create dummy variables. These techniques are fundamental for processing text data for machine learning algorithms.
