# Using Blob to Calculate String Byte Size

Now that we understand string representation, let's learn how to calculate the actual byte size of a string using the `Blob` object.

A `Blob` (Binary Large Object) represents a file-like object of immutable, raw data. By converting our string to a Blob, we can access its size property to determine the byte size.

In the Node.js console, let's create a function to calculate the byte size:

```javascript
const byteSize = (str) => new Blob([str]).size;
```

This function takes a string as input, converts it to a Blob, and returns its size in bytes.

Let's test this function with a simple example:

```javascript
byteSize("Hello World");
```

You should see the output:

```
11
```

In this case, the character count and byte size are the same because "Hello World" contains only ASCII characters, each represented by a single byte.

Now let's try with a non-ASCII character:

```javascript
byteSize("😀");
```

You should see the output:

```
4
```

This shows that while the emoji appears as a single character, it actually takes up 4 bytes of storage.
