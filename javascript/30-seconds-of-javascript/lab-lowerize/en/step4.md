# Handling Edge Cases

Our function works well for simple objects, but what about more complex cases? Let's explore some edge cases and see how our function handles them.

## Empty Objects

First, let's test with an empty object:

```javascript
lowerizeKeys({});
```

The output should be an empty object:

```
{}
```

## Objects with Nested Objects

What if the object contains nested objects? Let's try that:

```javascript
const nestedObject = {
  User: {
    Name: "John",
    Contact: {
      EMAIL: "john@example.com",
      PHONE: "123-456-7890"
    }
  }
};

lowerizeKeys(nestedObject);
```

The output will be:

```
{ user: { Name: 'John', Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' } } }
```

Notice that only the top-level key `User` is converted to lowercase. The keys inside the nested objects remain unchanged.

To handle nested objects, we would need to modify our function to recursively process all objects. Let's create an enhanced version:

```javascript
const deepLowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    const value = obj[key];
    // Check if the value is an object and not null
    const newValue =
      value && typeof value === "object" && !Array.isArray(value)
        ? deepLowerizeKeys(value)
        : value;

    acc[key.toLowerCase()] = newValue;
    return acc;
  }, {});
};
```

This enhanced function:

1. Checks if each value is also an object (and not an array or null)
2. If it is, it recursively calls itself on that nested object
3. Otherwise, it uses the original value

Let's test it with our nested object:

```javascript
const deepLowerizedObject = deepLowerizeKeys(nestedObject);
deepLowerizedObject;
```

Now you should see all keys converted to lowercase, even in nested objects:

```
{ user: { name: 'John', contact: { email: 'john@example.com', phone: '123-456-7890' } } }
```

Great job! You've created an advanced function that can handle nested objects.
