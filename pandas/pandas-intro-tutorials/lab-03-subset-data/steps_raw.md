# Data Selection in Pandas

## Introduction

In this lab, we are going to learn how to select specific data from a DataFrame using Pandas, a popular data analysis and manipulation library in Python. We will use the Titanic dataset for this tutorial.

## Steps

### Step 1: Importing the Necessary Libraries and Data

First, we need to import the Pandas library and the Titanic dataset.

```python
# Import pandas library
import pandas as pd

# Load the Titanic dataset
titanic = pd.read_csv("data/titanic.csv")
titanic.head()
```

### Step 2: Selecting a Single Column

To select a single column, use the square brackets `[]` with the column name of interest.

```python
# Select the 'Age' column
ages = titanic["Age"]

# Display the first 5 rows
ages.head()
```

### Step 3: Selecting Multiple Columns

To select multiple columns, use a list of column names within the selection brackets `[]`.

```python
# Select the 'Age' and 'Sex' columns
age_sex = titanic[["Age", "Sex"]]

# Display the first 5 rows
age_sex.head()
```

### Step 4: Filtering Specific Rows

To select rows based on a conditional expression, use the condition inside the selection brackets `[]`.

```python
# Filter rows where 'Age' is greater than 35
above_35 = titanic[titanic["Age"] > 35]

# Display the first 5 rows
above_35.head()
```

### Step 5: Selecting Specific Rows and Columns

To select both rows and columns in one go, we use the `loc` or `iloc` operators.

```python
# Select 'Name' of passengers older than 35
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

# Display the first 5 rows
adult_names.head()
```

## Summary

In this lab, we have learned how to select and filter data from a DataFrame in Pandas. We learned how to select single or multiple columns, filter rows based on certain conditions, and select specific rows and columns. These operations are fundamental in data analysis and manipulation with Pandas.
