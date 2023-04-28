# Radians to Degrees Challenge

## Introduction
In mathematics, angles can be measured in different units such as degrees and radians. Radians are a unit of measurement for angles that are commonly used in mathematics and physics. However, sometimes we may need to convert an angle from radians to degrees to make it more understandable. In this challenge, you will be asked to write a Python function that converts an angle from radians to degrees.

## Problem
Write a Python function called `rads_to_degrees` that takes a single argument `rad`, which is a float representing an angle in radians. The function should return the angle in degrees as a float. You can use the following formula to convert an angle from radians to degrees:

```
degrees = radians * (180 / pi)
```

where `pi` is a constant value representing the ratio of the circumference of a circle to its diameter, which is approximately equal to 3.14159.

Your function should import the `pi` constant from the `math` module.

## Example
Here is an example of how your function should work:

```py
from math import pi

assert rads_to_degrees(pi / 2) == 90.0
```

## Summary
In this challenge, you have written a Python function that converts an angle from radians to degrees. You have used the `pi` constant from the `math` module and the radian to degree formula to perform the conversion.