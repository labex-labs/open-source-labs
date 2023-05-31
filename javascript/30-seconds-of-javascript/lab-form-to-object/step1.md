# Converting a Form to an Object

To practice coding, open the Terminal/SSH and type `node`. You can encode a set of form elements as an object using the following steps:

1. Use the `FormData` constructor to convert the HTML `form` to `FormData`.
2. Convert the `FormData` to an array using `Array.from()`.
3. Collect the object from the array using `Array.prototype.reduce()`.

Here's an example code snippet:

```js
const formToObject = (form) =>
  Array.from(new FormData(form)).reduce(
    (acc, [key, value]) => ({
      ...acc,
      [key]: value,
    }),
    {}
  );
```

To convert a specific form, you can call the `formToObject` function and pass in the form element as an argument:

```js
formToObject(document.querySelector("#form"));
// { email: 'test@email.com', name: 'Test Name' }
```
