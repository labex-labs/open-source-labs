# Power Set

## Problem

Given a set, return all possible subsets of the set. The subsets should be unique, meaning that if two subsets have the same elements, they should be treated as the same subset. The empty set should also be included as a subset. The inputs are not necessarily unique, and we cannot assume that the inputs are valid. However, we can assume that the problem fits in memory.

## Requirements

To generate the power set of a set, we need to meet the following requirements:

- The resulting subsets should be unique, treating subsets with the same elements as the same.
- The empty set should be included as a subset.
- The inputs are not necessarily unique.
- We cannot assume that the inputs are valid.
- We can assume that the problem fits in memory.

## Example Usage

```txt
* None -> None
* [] -> [[]]
* ['a'] -> [[], 
            ['a']]
* ['a', 'b'] -> [[], 
                 ['a'], 
                 ['b'], 
                 ['a', 'b']]
* ['a', 'b', 'c'] -> [[], 
                      ['a'], 
                      ['b'], 
                      ['c'],
                      ['a', 'b'], 
                      ['a', 'c'], 
                      ['b', 'c'],
                      ['a', 'b', 'c']]
```
