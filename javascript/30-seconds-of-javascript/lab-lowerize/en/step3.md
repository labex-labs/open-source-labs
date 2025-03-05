# Creating the Lowercase Function

Now that we understand how to access object keys and use the `reduce()` method, let's create a function that converts all keys of an object to lowercase.

In your Node.js interactive shell, define the following function:

```javascript
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};
```

Let's break down what this function does:

1. `Object.keys(obj)` gets all the keys of the input object
2. `.reduce()` transforms these keys into a new object
3. For each key, we create a new entry in the accumulator object (`acc`) with:
   - The key converted to lowercase using `key.toLowerCase()`
   - The original value from the input object (`obj[key]`)
4. We start with an empty object `{}` as the initial value for the accumulator
5. Finally, we return the accumulator, which is our new object with lowercase keys

Now, let's test our function with the `user` object we created earlier:

```javascript
const lowercaseUser = lowerizeKeys(user);
lowercaseUser;
```

You should see the output:

```
{ name: 'John', age: 30, email: 'john@example.com' }
```

Perfect! All the keys are now in lowercase.

Let's try another example to make sure our function works correctly:

```javascript
const product = {
  ProductID: 101,
  ProductName: "Laptop",
  PRICE: 999.99
};

lowerizeKeys(product);
```

The output should be:

```
{ productid: 101, productname: 'Laptop', price: 999.99 }
```

Our function works correctly for different objects with various key casing styles.
