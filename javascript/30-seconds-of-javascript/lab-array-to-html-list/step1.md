# Converting Array to HTML List

To begin coding, launch the Terminal/SSH and enter `node`.

This function converts the given array elements into `<li>` tags and adds them to the list with the given id.

Use `Array.prototype.map()` and `Document.querySelector()` to generate a list of HTML tags.

```js
const arrayToHTMLList = (arr, listID) =>
  (document.querySelector(`#${listID}`).innerHTML += arr
    .map((item) => `<li>${item}</li>`)
    .join(""));
```

Example usage:

```js
arrayToHTMLList(["item 1", "item 2"], "myListID");
```
