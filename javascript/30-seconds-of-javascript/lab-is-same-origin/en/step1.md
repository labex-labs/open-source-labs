# Check if Two URLs are on the Same Origin

To check if two URLs are on the same origin:

1. Open the Terminal/SSH and type `node` to start practicing coding.

2. Use `URL.protocol` and `URL.host` to check if both URLs have the same protocol and host.

```js
const isSameOrigin = (origin, destination) =>
  origin.protocol === destination.protocol && origin.host === destination.host;
```

3. Create two URL objects with the URLs you want to compare.

```js
const origin = new URL("https://www.30secondsofcode.org/about");
const destination = new URL("https://www.30secondsofcode.org/contact");
```

4. Call the `isSameOrigin` function with the two URL objects as arguments to get a boolean output.

```js
isSameOrigin(origin, destination); // true
```

5. You can also test the function with other URLs to see if they are on the same origin or not.

```js
const other = new URL("https://developer.mozilla.org");
isSameOrigin(origin, other); // false
```
