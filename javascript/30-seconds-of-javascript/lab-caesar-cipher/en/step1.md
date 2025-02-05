# Caesar Cipher

To use the Caesar cipher, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Call the `caesarCipher` function with the string to be encrypted or decrypted, the shift value, and a boolean indicating whether to decrypt or not.
3. The `caesarCipher` function uses the modulo (`%`) operator and the ternary operator (`?`) to calculate the correct encryption or decryption key.
4. It uses the spread operator (`...`) and `Array.prototype.map()` to iterate over the letters of the given string.
5. It uses `String.prototype.charCodeAt()` and `String.fromCharCode()` to convert each letter appropriately, ignoring special characters, spaces, etc.
6. It uses `Array.prototype.join()` to combine all the letters into a string.
7. If you want to decrypt an encrypted string, pass `true` to the last parameter, `decrypt`, when calling the `caesarCipher` function.

Here is the code for the `caesarCipher` function:

```js
const caesarCipher = (str, shift, decrypt = false) => {
  const s = decrypt ? (26 - shift) % 26 : shift;
  const n = s > 0 ? s : 26 + (s % 26);
  return [...str]
    .map((l, i) => {
      const c = str.charCodeAt(i);
      if (c >= 65 && c <= 90)
        return String.fromCharCode(((c - 65 + n) % 26) + 65);
      if (c >= 97 && c <= 122)
        return String.fromCharCode(((c - 97 + n) % 26) + 97);
      return l;
    })
    .join("");
};
```

Here are some examples of how to use the `caesarCipher` function:

```js
caesarCipher("Hello World!", -3); // 'Ebiil Tloia!'
caesarCipher("Ebiil Tloia!", 23, true); // 'Hello World!'
```
