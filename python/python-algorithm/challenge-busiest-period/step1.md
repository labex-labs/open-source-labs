# Busiest Period

## Problem

Given an array of (unix_timestamp, num_people, EventType.ENTER or EventType.EXIT), find the busiest period. The input array may not be sorted by time, and there may be enter and exit events for the same timestamp. However, there will not be multiple enter events (or multiple exit events) for the same timestamp.

## Requirements

To solve this problem, we need to consider the following requirements:

- Check for None input array
- The elements of the input array are valid
- The input is not sorted by time
- There can be enter and exit events for the same timestamp
- There will not be multiple enter events (or multiple exit events) for the same timestamp
- The output should be an array of timestamps [t1, t2]
- The starting number of people is zero
- The inputs may not be valid
- The solution should fit in memory

## Example Usage

Here are some examples of how to use the Period function:

- None -> TypeError
- [] -> None
- General case

```txt
timestamp  num_people  event_type
1          2           EventType.ENTER
3          1           EventType.ENTER
3          2           EventType.EXIT
7          3           EventType.ENTER
8          2           EventType.EXIT
9          2           EventType.EXIT

result = Period(7, 8)
```
