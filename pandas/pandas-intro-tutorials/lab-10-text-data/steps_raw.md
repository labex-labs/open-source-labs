# Pandas Textual Data Lab

## Introduction

In this lab, we will explore how to manipulate textual data using Python's Pandas library. You will learn how to convert string characters to lowercase, extract parts of strings, replace string values and more using various built-in Pandas methods.

## Steps

### Step 1: Import Necessary Libraries and Data

Let's start by importing the Pandas library and loading the data we will use for this tutorial.

```python
# Import necessary libraries
import pandas as pd

# Load the data
titanic = pd.read_csv("data/titanic.csv")
```

### Step 2: Convert String Characters to Lowercase

Next, we will convert all characters in the `Name` column to lowercase. We'll use the `str.lower()` method to achieve this.

```python
# Convert all characters in the 'Name' column to lowercase
titanic["Name"] = titanic["Name"].str.lower()
```

### Step 3: Extract Surnames from Full Names

Now, let's create a new column `Surname` that contains the surname of the passengers. We'll achieve this by extracting the part before the comma in the `Name` column.

```python
# Split the 'Name' column on comma and extract the first part
titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)
```

### Step 4: Extract Specific Passenger Data

Next, let's extract the passenger data for the countesses on board of the Titanic. We'll use the `str.contains()` method to find rows where the `Name` column contains the word 'Countess'.

```python
# Find rows where 'Name' contains 'Countess'
countesses = titanic[titanic["Name"].str.contains("Countess")]
```

### Step 5: Find the Longest Name

Let's find out which passenger of the Titanic has the longest name. We'll use the `str.len()` method to get the length of each name, and the `idxmax()` method to find the index of the longest name.

```python
# Get the length of each name
name_lengths = titanic["Name"].str.len()

# Find the index of the longest name
longest_name_index = name_lengths.idxmax()

# Get the longest name
longest_name = titanic.loc[longest_name_index, "Name"]
```

### Step 6: Replace Values in a Column

Finally, let's replace the values in the `Sex` column: 'male' with 'M' and 'female' with 'F'. We'll use the `replace()` method for this.

```python
# Replace 'male' with 'M' and 'female' with 'F' in the 'Sex' column
titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
```

## Summary

In this lab, we have seen how to manipulate textual data using Python's Pandas library. We have learnt how to convert string characters to lowercase, extract parts of strings, find specific rows based on string contents, find the longest string, and replace string values. This knowledge is very useful in data preprocessing, a crucial step in data analysis and machine learning.
