# Map Number to Range

## Introduction

In programming, we often need to map a number from one range to another range. For example, we may have a number that ranges from 0 to 10, but we need to map it to a range of 0 to 100. This can be useful in many applications, such as scaling data or converting units.

## Problem

Write a function called `num_to_range` that takes five arguments: `num`, `inMin`, `inMax`, `outMin`, and `outMax`. The function should return `num` mapped between `outMin`-`outMax` from `inMin`-`inMax`. In other words, the function should take a number (`num`) that falls within a certain range (`inMin`-`inMax`) and map it to a new range (`outMin`-`outMax`).

## Example

```py
num_to_range(5, 0, 10, 0, 100) # 50.0
```

In this example, we are mapping the number 5 from a range of 0 to 10 to a range of 0 to 100. The result should be 50.0.

## Summary

In this challenge, you were asked to write a function that maps a number from one range to another range. This can be a useful tool in many programming applications.
