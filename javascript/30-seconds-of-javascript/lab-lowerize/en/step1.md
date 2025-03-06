# Understanding Objects in JavaScript

Before we start converting object keys to lowercase, let's understand what JavaScript objects are and how we can work with them.

In JavaScript, an object is a collection of key-value pairs. Keys are strings (or Symbols), and values can be any data type, including other objects.

Let's start by opening the Node.js interactive shell:

1. Open the terminal in your WebIDE
2. Type `node` and press Enter

You should now see the Node.js prompt (`>`), which allows you to type JavaScript code directly.

Let's create a simple object with mixed case keys:

```javascript
const user = {
  Name: "John",
  AGE: 30,
  Email: "john@example.com"
};
```

Type this code into the Node.js prompt and press Enter. To see the object, simply type `user` and press Enter:

```javascript
user;
```

You should see the output:

```
{ Name: 'John', AGE: 30, Email: 'john@example.com' }
```

As you can see, this object has keys with different casing styles. In the next step, we'll learn how to access these keys and convert them to lowercase.
