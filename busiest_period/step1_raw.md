# Busiest Period

Problem: Given an array of (unix_timestamp, num_people, EventType.ENTER or EventType.EXIT), find the busiest period.

## Requirements

- Can we assume the input array is valid?
  - Check for None
- Can we assume the elements of the input array are valid?
  - Yes
- Is the input sorted by time?
  - No
- Can you have enter and exit elements for the same timestamp?
  - Yes you can, order of enter and exit is not guaranteed
- Could we have multiple enter events (or multiple exit events) for the same timestamp?
  - No
- What is the format of the output?
  - An array of timestamps [t1, t2]
- Can we assume the starting number of people is zero?
  - Yes
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Example Usage

- None -> TypeError
- [] -> None
- General case

<pre>
timestamp  num_people  event_type
1          2           EventType.ENTER
3          1           EventType.ENTER
3          2           EventType.EXIT
7          3           EventType.ENTER
8          2           EventType.EXIT
9          2           EventType.EXIT

result = Period(7, 8)
</pre>
