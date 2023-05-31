# Remove Attributes

> To start practicing coding, open the Terminal/SSH and type `node`.

Removes all attributes from an HTML element.

- Use `Element.attributes` and `Object.values()` to get all the attributes of the element.
- Use `Array.prototype.forEach()` and object destructuring to get the name of each attribute and `Element.removeAttribute()` to remove it from the element.

```js
const removeAttributes = element =>
  Object.values(element.attributes).forEach(({ name }) =>
    element.removeAttribute(name)
  );
```

```js
removeAttributes(document.querySelector('p.special'));
// The paragraph will not have the 'special' class anymore
```
