# How to Convert a Tilde Path to an Absolute Path in Node.js

To begin coding practice in Node.js, open the Terminal or SSH and type `node`. To convert a tilde path to an absolute path, use the following code:

```js
const untildify = (str) =>
  str.replace(/^~($|\/|\\)/, `${require("os").homedir()}$1`);
```

The code uses `String.prototype.replace()` with a regular expression and `os.homedir()` to replace the `~` at the beginning of the path with the home directory. Here is an example of how to use the `untildify` function:

```js
untildify("~/node"); // returns '/Users/aUser/node'
```
