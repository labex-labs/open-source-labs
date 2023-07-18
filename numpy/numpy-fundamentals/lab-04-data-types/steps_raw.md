# NumPy Data Types

## Introduction

This lab will provide a step-by-step guide to understanding the different data types available in NumPy, and how to modify an array's data type. NumPy supports a wide range of numerical types, including booleans, integers, floating point numbers, and complex numbers. Understanding these data types is important for performing various numerical computations and data analysis tasks using NumPy.

## Steps

### Step 1: Understanding Data Types

NumPy supports a variety of numerical types that are closely tied to those in the C programming language. Here are some of the most commonly used data types in NumPy:

- `numpy.bool_`: Boolean (True or False) stored as a byte
- `numpy.byte`: Signed char (platform-defined)
- `numpy.ubyte`: Unsigned char (platform-defined)
- `numpy.short`: Short (platform-defined)
- `numpy.ushort`: Unsigned short (platform-defined)
- `numpy.intc`: Int (platform-defined)
- `numpy.uintc`: Unsigned int (platform-defined)
- `numpy.int_`: Long (platform-defined)
- `numpy.uint`: Unsigned long (platform-defined)
- `numpy.longlong`: Long long (platform-defined)
- `numpy.ulonglong`: Unsigned long long (platform-defined)
- `numpy.half` / `numpy.float16`: Half precision float
- `numpy.single`: Single precision float (platform-defined)
- `numpy.double`: Double precision float (platform-defined)
- `numpy.longdouble`: Extended-precision float (platform-defined)
- `numpy.csingle`: Complex number represented by two single-precision floats
- `numpy.cdouble`: Complex number represented by two double-precision floats
- `numpy.clongdouble`: Complex number represented by two extended-precision floats

These data types have platform-dependent definitions, but NumPy also provides fixed-size aliases for convenience.

### Step 2: Working with Data Types

NumPy data types are represented as `dtype` (data-type) objects. Once you have imported NumPy using `import numpy as np`, you can access the data types using `np.bool_`, `np.float32`, etc.

You can use data types as functions to convert Python numbers to array scalars, Python sequences of numbers to arrays of that type, or as arguments to the dtype keyword in many NumPy functions or methods. Here are some examples:

```python
x = np.float32(1.0)
# x is now a float32 array scalar with value 1.0

y = np.int_([1,2,4])
# y is now an int array with values [1, 2, 4]

z = np.arange(3, dtype=np.uint8)
# z is now a uint8 array with values [0, 1, 2]
```

You can also refer to array types using character codes, although it is recommended to use dtype objects instead. For example:

```python
np.array([1, 2, 3], dtype='f')
# returns an array with values [1., 2., 3.] and dtype float32
```

To convert the type of an array, you can use the `.astype()` method or the type itself as a function. For example:

```python
z.astype(float)
# returns the array z with dtype float64

np.int8(z)
# returns the array z with dtype int8
```

### Step 3: Retrieving the Data Type of an Array

To determine the data type of an array, you can access the `dtype` attribute. For example:

```python
z.dtype
# returns the dtype of array z, which is uint8
```

The `dtype` object also contains information about the type, such as its bit-width and byte-order. You can use the `dtype` object to query properties of the type, such as whether it is an integer. For example:

```python
d = np.dtype(int)
# creates a dtype object for int

np.issubdtype(d, np.integer)
# returns True, indicating that d is a subdtype of np.integer

np.issubdtype(d, np.floating)
# returns False, indicating that d is not a subdtype of np.floating
```

## Summary

In this lab, you learned about the different numerical data types available in NumPy and how to work with them. You can use `dtype` objects to convert Python numbers to array scalars, create arrays of specific types, and modify the data type of an array. Understanding data types is important for performing numerical computations and data analysis tasks using NumPy.
