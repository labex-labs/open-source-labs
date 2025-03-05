# Creating a Reusable Module

Now that we have working functions, let's create a reusable JavaScript module file that we can import into other projects.

First, let's exit the Node.js interactive shell by pressing Ctrl+C twice or typing `.exit` and pressing Enter.

Now, create a new file named `object-utils.js` in the project directory:

1. In the WebIDE, navigate to the file explorer panel on the left
2. Right-click in the project directory and select "New File"
3. Name the file `object-utils.js`
4. Add the following code to the file:

```javascript
/**
 * Converts all keys of an object to lowercase
 * @param {Object} obj - The input object
 * @returns {Object} A new object with all keys in lowercase
 */
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};

/**
 * Recursively converts all keys of an object and its nested objects to lowercase
 * @param {Object} obj - The input object
 * @returns {Object} A new object with all keys in lowercase (including nested objects)
 */
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

// Export the functions
module.exports = {
  lowerizeKeys,
  deepLowerizeKeys
};
```

Now, let's create a test file to verify that our module works correctly. Create a new file named `test.js`:

1. In the WebIDE, navigate to the file explorer panel on the left
2. Right-click in the project directory and select "New File"
3. Name the file `test.js`
4. Add the following code to the file:

```javascript
// Import the functions from our module
const { lowerizeKeys, deepLowerizeKeys } = require("./object-utils");

// Test with a simple object
const user = {
  Name: "John",
  AGE: 30,
  Email: "john@example.com"
};

console.log("Original object:");
console.log(user);

console.log("\nObject with lowercase keys:");
console.log(lowerizeKeys(user));

// Test with a nested object
const nestedObject = {
  User: {
    Name: "John",
    Contact: {
      EMAIL: "john@example.com",
      PHONE: "123-456-7890"
    }
  }
};

console.log("\nNested object:");
console.log(nestedObject);

console.log("\nNested object with lowercase keys (shallow):");
console.log(lowerizeKeys(nestedObject));

console.log("\nNested object with lowercase keys (deep):");
console.log(deepLowerizeKeys(nestedObject));
```

Now, let's run the test file:

```bash
node test.js
```

You should see output similar to:

```
Original object:
{ Name: 'John', AGE: 30, Email: 'john@example.com' }

Object with lowercase keys:
{ name: 'John', age: 30, email: 'john@example.com' }

Nested object:
{
  User: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Nested object with lowercase keys (shallow):
{
  user: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Nested object with lowercase keys (deep):
{
  user: {
    name: 'John',
    contact: { email: 'john@example.com', phone: '123-456-7890' }
  }
}
```

Congratulations! You've successfully created a reusable JavaScript module with functions to convert object keys to lowercase. This module can now be imported into any of your JavaScript projects.
