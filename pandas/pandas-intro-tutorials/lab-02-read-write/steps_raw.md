# Pandas Data Manipulation Lab

## Introduction

This lab will guide you on how to read, write, and manipulate data using Pandas, a powerful data analysis and manipulation library for Python. We will use a dataset from the Titanic shipwreck for this exercise.

## Steps

### Step 1: Importing Necessary Libraries

First, we need to import the necessary libraries for our task. For this lab, we will only need pandas.

```python
# Importing pandas library
import pandas as pd
```

### Step 2: Reading Data From CSV

The next step is to read the data from a CSV file. We will use the `read_csv` function from pandas to do this.

```python
# Reading data from CSV file
titanic = pd.read_csv("data/titanic.csv")
```

### Step 3: Checking the Data

After reading the data, it's always a good idea to check what it looks like. We will display the first few rows of the DataFrame.

```python
# Displaying the first few rows of the DataFrame
titanic.head()
```

### Step 4: Checking the Data Types

We can check the data types of each column using the `dtypes` attribute of the DataFrame.

```python
# Checking the data types of each column
titanic.dtypes
```

### Step 5: Writing Data to Excel

You can also write the data to an Excel file using the `to_excel` method. Let's save our DataFrame to an Excel file.

```python
# Saving DataFrame to an Excel file
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
```

### Step 6: Reading Data From Excel

Reading data from an Excel file is as easy as reading data from a CSV file. We will use the `read_excel` function from pandas.

```python
# Reading data from an Excel file
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
```

### Step 7: Checking DataFrame Information

The `info` method provides a technical summary of a DataFrame. This can be useful to check the data types, number of non-null values, and memory usage.

```python
# Checking DataFrame information
titanic.info()
```

## Summary

In this lab, we learned how to read and write data using pandas, and how to check a DataFrame's information. Pandas provides a wide range of functionalities for handling and manipulating data, making it a powerful tool for data analysis.
