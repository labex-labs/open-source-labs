# Understanding Copy-On-Write

## Introduction

This lab provides a step-by-step guide on understanding and implementing the concept of Copy-On-Write (CoW) in Python Pandas. CoW is an optimization strategy that enhances performance and memory usage by delaying copies as long as possible. It also helps in avoiding accidental modifications of more than one object.

## Steps

### Step 1: Enabling Copy-On-Write

First, let's enable CoW in pandas. This can be done using the `copy_on_write` configuration option in pandas. Here are two ways you can enable CoW globally.

```python
# Enable CoW using set_option
pd.set_option("mode.copy_on_write", True)

# Or using direct assignment
pd.options.mode.copy_on_write = True
```

### Step 2: Understanding CoW with DataFrame

Now, let's create a DataFrame and see how CoW affects the modification of data.

```python
# Create a DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# Create a subset of the DataFrame
subset = df["foo"]

# Modify the subset
subset.iloc[0] = 100

# Print the original DataFrame
print(df)
```

### Step 3: Implementing CoW with DataFrame

Now, let's see how to implement CoW when modifying a DataFrame.

```python
# Enable CoW
pd.options.mode.copy_on_write = True

# Create a DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# Create a subset of the DataFrame
subset = df["foo"]

# Modify the subset
subset.iloc[0] = 100

# Print the original DataFrame
print(df)
```

### Step 4: Understanding Chained Assignment with CoW

Now, let's understand how chained assignment works with CoW.

```python
# Create a DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# Apply chained assignment, which would violate CoW principles
df["foo"][df["bar"] > 5] = 100

# Print the DataFrame
print(df)
```

### Step 5: Implementing Chained Assignment with CoW

Finally, let's see how to implement chained assignment with CoW using the `loc` method.

```python
# Create a DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# Apply chained assignment with CoW using 'loc'
df.loc[df["bar"] > 5, "foo"] = 100

# Print the DataFrame
print(df)
```

## Summary

In this lab, you learned about the concept of Copy-On-Write (CoW) and how to implement it in Python Pandas. You also understood how CoW affects the modification of data and how it works with chained assignment. By using CoW, you can optimize your code for better performance and memory usage.
