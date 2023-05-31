# Prefix a CSS Property

To prefix a CSS property based on the current browser, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.findIndex()` on an array of vendor prefix strings to test if `Document.body` has one of them defined in its `CSSStyleDeclaration` object, otherwise return `null`.
3. Use `String.prototype.charAt()` and `String.prototype.toUpperCase()` to capitalize the property, which will be appended to the vendor prefix string.
4. Use the provided function to prefix the desired property.

```js
const prefix = (prop) => {
  const capitalizedProp = prop.charAt(0).toUpperCase() + prop.slice(1);
  const prefixes = ["", "webkit", "moz", "ms", "o"];
  const i = prefixes.findIndex(
    (prefix) =>
      typeof document.body.style[prefix ? prefix + capitalizedProp : prop] !==
      "undefined"
  );
  return i !== -1 ? (i === 0 ? prop : prefixes[i] + capitalizedProp) : null;
};
```

To use the function, simply call `prefix('appearance')`. This will return 'appearance' on a supported browser. If the browser does not support the property, it will return one of the vendor-prefixed versions: 'webkitAppearance', 'mozAppearance', 'msAppearance', or 'oAppearance'.
