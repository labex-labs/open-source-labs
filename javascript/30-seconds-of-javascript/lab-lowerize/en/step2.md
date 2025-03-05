# Accessing Object Keys

Before we can transform object keys, we need to understand how to access them. JavaScript provides the `Object.keys()` method, which returns an array containing all the keys of an object.

In your Node.js interactive shell, try the following:

```javascript
Object.keys(user);
```

You should see an output like this:

```
[ 'Name', 'AGE', 'Email' ]
```

Now, let's try converting each key to lowercase using the `toLowerCase()` method. We can use the `map()` method to transform each key:

```javascript
Object.keys(user).map((key) => key.toLowerCase());
```

The output should be:

```
[ 'name', 'age', 'email' ]
```

Great! We now have an array with all the keys converted to lowercase. However, we still need to create a new object with these lowercase keys and the original values. For this, we'll use the `reduce()` method in the next step.

Let's understand the `reduce()` method before moving forward. This method executes a reducer function on each element of the array, resulting in a single output value.

Here's a simple example of `reduce()`:

```javascript
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((accumulator, currentValue) => {
  return accumulator + currentValue;
}, 0);

sum;
```

The output will be `10`, which is the sum of all numbers in the array. The `0` in the `reduce()` method is the initial value of the accumulator.
