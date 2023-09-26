# Check Property

Create a function called `check_prop` that takes in two parameters: `fn` and `prop`. The `fn` parameter is a predicate function that will be applied to the specified property of a dictionary. The `prop` parameter is a string that represents the name of the property that the predicate function will be applied to.

The `check_prop` function should return a lambda function that takes in a dictionary and applies the predicate function, `fn`, to the specified property.

```python
def check_prop(fn, prop):
  return lambda obj: fn(obj[prop])
```

```python
check_age = check_prop(lambda x: x >= 18, 'age')
user = {'name': 'Mark', 'age': 18}
check_age(user) # True
```
