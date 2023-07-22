# Structured Arrays Lab

## Introduction

In this lab, we will learn about structured arrays in NumPy. Structured arrays are ndarrays whose datatype is a composition of simpler datatypes organized as a sequence of named fields. They are useful for working with structured data, such as tabular data, where each field represents a different attribute of the data.

## Steps

### Step 1: Creating a Structured Array

To create a structured array, we can use the `np.array` function and specify the data type using the `dtype` parameter. The data type should be a list of tuples, where each tuple represents a field in the structured array. Each tuple should contain the field name and the data type of the field.

```python
import numpy as np

# Create a structured array
x = np.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
```

### Step 2: Accessing Fields

We can access individual fields of a structured array by indexing with the field name. This will return a new array containing only the values of that field.

```python
# Access the 'name' field
names = x['name']
```

### Step 3: Modifying Fields

We can also modify individual fields of a structured array by indexing with the field name and assigning new values.

```python
# Modify the 'age' field
x['age'] = [26, 31]
```

### Step 4: Indexing with Multiple Fields

We can index a structured array with multiple fields by passing a list of field names. This will return a new structured array containing only the specified fields.

```python
# Index with multiple fields
subset = x[['name', 'age']]
```

### Step 5: Comparing Structured Arrays

If the dtypes of two structured arrays are equal, we can compare them using the equality operator (`==`). This will return a boolean array indicating which elements have the same values for all fields.

```python
# Compare two structured arrays
y = np.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
comparison = x == y
```

### Step 6: Creating a Record Array

A record array is a subclass of ndarray that allows access to fields by attribute instead of index. We can create a record array using the `np.rec.array` function.

```python
# Create a record array
recordarr = np.rec.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
```

### Step 7: Accessing Fields by Attribute

We can access fields of a record array by attribute instead of index. This provides a more convenient way to work with structured data.

```python
# Access fields by attribute
names = recordarr.name
```

### Step 8: Converting a Structured Array to a Record Array

We can convert a structured array to a record array using the `view` method and specifying the `np.recarray` type.

```python
# Convert a structured array to a record array
recordarr = x.view(np.recarray)
```

### Step 9: Converting a Record Array to a Structured Array

To convert a record array back to a structured array, we can use the `view` method and specify the original dtype of the structured array.

```python
# Convert a record array to a structured array
x = recordarr.view(dtype=[('name', 'U10'), ('age', int)])
```

## Summary

In this lab, we learned how to create and work with structured arrays in NumPy. Structured arrays are useful for working with structured data, and they allow us to access and modify individual fields of the array. We also learned about record arrays, which provide a more convenient way to work with structured data by allowing access to fields by attribute instead of index.
