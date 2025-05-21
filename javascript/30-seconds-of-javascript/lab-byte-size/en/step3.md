# Testing with Different String Types

Let's explore how different types of characters affect the byte size of a string.

In the Node.js console, let's test our `byteSize` function with various strings:

1. Plain English text:

```javascript
byteSize("The quick brown fox jumps over the lazy dog");
```

Expected output:

```
43
```

2. Numbers and special characters:

```javascript
byteSize("123!@#$%^&*()");
```

Expected output:

```
13
```

3. A mix of ASCII and non-ASCII characters:

```javascript
byteSize("Hello, 世界！");
```

Expected output:

```
13
```

4. Multiple emojis:

```javascript
byteSize("😀😃😄😁");
```

Expected output:

```
16
```

Notice that with the mixed character types, especially with non-ASCII characters like Chinese characters and emojis, the byte size is larger than the character count.

This is important to understand when working with data that might contain international characters or special symbols, as it affects storage requirements and data transfer sizes.

Let's exit the Node.js console by typing:

```javascript
.exit
```

This will return you to the regular terminal prompt.
