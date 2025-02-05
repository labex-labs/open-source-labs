# Generating Random Hex Color Code in Terminal/SSH

To generate a random hexadecimal color code in Terminal/SSH, follow the steps below:

1. Open the Terminal/SSH.
2. Type `node`.
3. Use the following code to generate a random 24-bit (6 \* 4bits) hexadecimal number:

```js
const randomHexColorCode = () => {
  let n = (Math.random() * 0xfffff * 1000000).toString(16);
  return "#" + n.slice(0, 6);
};
```

4. To generate a random hex color code, call the function `randomHexColorCode()`.

Example:

```js
randomHexColorCode(); // '#e34155'
```

This will generate a random hex color code that you can use in your coding projects.
