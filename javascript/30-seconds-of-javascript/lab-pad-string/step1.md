# Function to Pad String

To pad a string on both sides with the specified character, if it's shorter than the specified `length`, use the following function:

```js
const pad = (str, length, char = " ") =>
  str.padStart((str.length + length) / 2, char).padEnd(length, char);
```

The function uses `String.prototype.padStart()` and `String.prototype.padEnd()` to pad both sides of the given string. You can omit the third argument, `char`, to use the whitespace character as the default padding character.

Here are some examples of how to use the `pad()` function:

```js
pad("cat", 8); // '  cat   '
pad(String(42), 6, "0"); // '004200'
pad("foobar", 3); // 'foobar'
```

To start practicing coding, open the Terminal/SSH and type `node`.
