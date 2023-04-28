# Check Property

## Problem

Create a function called `check_prop` that takes in two parameters: `fn` and `prop`. The `fn` parameter is a predicate function that will be applied to the specified property of a dictionary. The `prop` parameter is a string that represents the name of the property that the predicate function will be applied to.

The `check_prop` function should return a lambda function that takes in a dictionary and applies the predicate function, `fn`, to the specified property.

## Example

```py
check_age = check_prop(lambda x: x >= 18, 'age')
user = {'name': 'Mark', 'age': 18}
check_age(user) # True
```

In the example above, we create a `check_age` function that checks if the value of the `age` property in a dictionary is greater than or equal to 18. We then create a `user` dictionary with a name and age property. Finally, we call the `check_age` function with the `user` dictionary as an argument, which returns `True` since the age property is equal to 18.
