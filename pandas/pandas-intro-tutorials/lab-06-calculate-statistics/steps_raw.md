# Pandas Statistics Lab

## Introduction

In this lab, we will learn how to use Python's Pandas library to calculate summary statistics for data. We will use the Titanic dataset, which contains data on passengers from the Titanic shipwreck. We will learn how to calculate summary statistics, aggregate statistics, and count the number of records by category.

## Steps

### Step 1: Importing the Dataset

The first step is to import the dataset we will be using.

```python
# Importing pandas library
import pandas as pd

# Reading the dataset
titanic = pd.read_csv("data/titanic.csv")

# Displaying the first five rows of the dataset
titanic.head()
```

### Step 2: Calculating Summary Statistics

In this step, we will calculate summary statistics for the Titanic dataset.

```python
# Computing the average age of the Titanic passengers
average_age = titanic["Age"].mean()
# Printing the result
print(f"The average age of the Titanic passengers is {average_age}")

# Computing the median age and ticket fare price of the Titanic passengers
median_age_fare = titanic[["Age", "Fare"]].median()
# Printing the result
print(f"The median age and ticket fare price of the Titanic passengers are {median_age_fare}")
```

### Step 3: Aggregating Statistics Grouped by Category

Next, we will learn how to aggregate statistics grouped by category.

```python
# Computing the average age for male versus female Titanic passengers
average_age_sex = titanic[["Sex", "Age"]].groupby("Sex").mean()
# Printing the result
print(f"The average age for male versus female Titanic passengers is {average_age_sex}")

# Computing the mean ticket fare price for each of the sex and cabin class combinations
mean_fare_sex_class = titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
# Printing the result
print(f"The mean ticket fare price for each of the sex and cabin class combinations is {mean_fare_sex_class}")
```

### Step 4: Counting Number of Records by Category

Finally, we will count the number of records by category.

```python
# Counting the number of passengers in each of the cabin classes
passengers_per_class = titanic["Pclass"].value_counts()
# Printing the result
print(f"The number of passengers in each of the cabin classes is {passengers_per_class}")
```

## Summary

In this lab, we learned how to calculate summary statistics, aggregate statistics, and count the number of records by category using Python's Pandas library. We used the Titanic dataset to perform these operations. These techniques are fundamental for data analysis and can be applied to any dataset.
