# Here's how to get the colon time from a date object

If you're looking to practice coding, you can start by opening the Terminal/SSH and typing `node`.

This function returns a string of the form `HH:MM:SS` from a given `Date` object.

To achieve this, the `Date.prototype.toTimeString()` and `String.prototype.slice()` methods are utilized to extract the `HH:MM:SS` part of the `Date` object.

Here's the code for the function:

```js
const getColonTimeFromDate = (date) => date.toTimeString().slice(0, 8);
```

And here's an example usage:

```js
getColonTimeFromDate(new Date()); // '08:38:00'
```
