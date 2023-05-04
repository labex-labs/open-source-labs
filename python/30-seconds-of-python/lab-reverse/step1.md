# Reverse List Function

Write a Python function called `reverse(itr)` that takes a list or a string as its argument and returns a new list or string that contains the elements or characters in reverse order.

Your function should have the following requirements:

- The function should be named `reverse`
- The function should take a single argument, which is a list or a string
- The function should return a new list or string that contains the elements or characters in reverse order
- The function should not modify the original list or string

```py
def reverse(itr):
  return itr[::-1]
```

```py
reverse([1, 2, 3]) # [3, 2, 1]
reverse('snippet') # 'teppins'
```
