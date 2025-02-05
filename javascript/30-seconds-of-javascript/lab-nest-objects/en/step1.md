# How to Nest Objects Using Recursion in JavaScript

To nest objects in a flat array recursively, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use recursion to nest objects that are linked to one another.
3. Use `Array.prototype.filter()` to filter the items where the `id` matches the `link`.
4. Use `Array.prototype.map()` to map each item to a new object that has a `children` property which recursively nests the items based on which ones are children of the current item.
5. Omit the second argument, `id`, to default to `null` which indicates the object is not linked to another one (i.e. it is a top level object).
6. Omit the third argument, `link`, to use `'parent_id'` as the default property which links the object to another one by its `id`.

Here's the code:

```js
const nest = (items, id = null, link = "parent_id") =>
  items
    .filter((item) => item[link] === id)
    .map((item) => ({ ...item, children: nest(items, item.id, link) }));
```

To use the `nest()` function, create an array of objects that have an `id` property and a `parent_id` property that links them to another object. Then, call the `nest()` function and pass the array as an argument. The function will return a new array of objects that are nested based on their `parent_id` property.

For example:

```js
const comments = [
  { id: 1, parent_id: null },
  { id: 2, parent_id: 1 },
  { id: 3, parent_id: 1 },
  { id: 4, parent_id: 2 },
  { id: 5, parent_id: 4 }
];
const nestedComments = nest(comments);
// [{ id: 1, parent_id: null, children: [...] }]
```
