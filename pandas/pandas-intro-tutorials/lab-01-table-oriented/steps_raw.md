# Working with Pandas

## Introduction

Pandas is a powerful data manipulation tool developed by Python. It's often used in data analysis and cleaning because it's flexible and easy to use. In this lab, we will learn how to use Pandas to perform basic operations like loading data, creating data frames, accessing data, and performing simple statistics.

## Steps

### Step 1: Import the Pandas Package

Before you can use Pandas, you need to import it. It's a common practice to import Pandas with the alias `pd`.

```python
# Importing pandas package
import pandas as pd
```

### Step 2: Create a DataFrame

Data in pandas is stored in a DataFrame, which is a 2-dimensional labeled data structure with columns potentially of different types.

```python
# Creating a DataFrame
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
```

### Step 3: Select a Column

If you want to work with data in a specific column, you can select it using the column label. The result is a pandas Series.

```python
# Selecting the 'Age' column
df["Age"]
```

### Step 4: Perform Basic Statistics

Pandas provides a lot of functionalities to perform statistics. For instance, you can find the maximum value in a column using `max()`.

```python
# Finding the maximum age
df["Age"].max()
```

You can also get a quick overview of the numerical data in a DataFrame using `describe()`.

```python
# Describing the numerical data
df.describe()
```

## Summary

In this lab, we learned how to import the Pandas package, create a DataFrame, select a column, and perform basic statistics. Pandas is a versatile tool that can handle data of different types, making it a great choice for data analysis and manipulation.
