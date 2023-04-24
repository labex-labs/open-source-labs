# Power Set

Problem: Return all subsets of a set.

## Requirements

- Should the resulting subsets be unique?
  - Yes, treat 'ab' and 'bc' as the same
- Is the empty set included as a subset?
  - Yes
- Are the inputs unique?
  - No
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Example Usage

<pre>
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
</pre>
