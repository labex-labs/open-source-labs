# Exercise 6.14: Generator Expressions in Function Arguments

Generator expressions are sometimes placed into function arguments. It looks a little weird at first, but try this experiment:

```python
>>> nums = [1,2,3,4,5]
>>> sum([x*x for x in nums])    # A list comprehension
55
>>> sum(x*x for x in nums)      # A generator expression
55
>>>
```

In the above example, the second version using generators would use significantly less memory if a large list was being manipulated.

In your `portfolio.py` file, you performed a few calculations involving list comprehensions. Try replacing these with generator expressions.
