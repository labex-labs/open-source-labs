# How to Bind All Object Methods in JavaScript

To bind methods of an object to the object itself, thus overwriting the existing method, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.

2. Use `Array.prototype.forEach()` to iterate over the given `fns`.

3. Return a function for each one, using `Function.prototype.apply()` to apply the given context (`obj`) to `fn`.

```js
const bindAll = (obj, ...fns) =>
  fns.forEach((fn) => {
    const f = obj[fn];
    obj[fn] = function () {
      return f.apply(obj);
    };
  });
```

4. Once you have the `bindAll()` function, you can use it to bind the methods of an object. For example:

```js
const view = {
  label: "docs",
  click: function () {
    console.log("clicked " + this.label);
  },
};

bindAll(view, "click");

document.body.addEventListener("click", view.click);
// This will log 'clicked docs' when clicked.
```
