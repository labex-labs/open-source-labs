# Rendering Lists

> The React project have already been provided in the VM. In general, you only need to add code to `App.js`.

Please use the following command to install the dependencies:

```bash
npm i
```

You will rely on JavaScript features like for loop and the array `map()` function to render lists of components.

For example, let’s say you have an array of products:

```js
const products = [
  { title: "Cabbage", id: 1 },
  { title: "Garlic", id: 2 },
  { title: "Apple", id: 3 },
];
```

Inside your component, use the `map()` function to transform an array of products into an array of `<li>` items:

```js
const listItems = products.map((product) => (
  <li key={product.id}>{product.title}</li>
));

return <ul>{listItems}</ul>;
```

Notice how `<li>` has a key attribute. For each item in a list, you should pass a string or a number that uniquely identifies that item among its siblings. Usually, a key should be coming from your data, such as a database ID. React uses your keys to know what happened if you later insert, delete, or reorder the items.

```js
// App.js
const products = [
  { title: "Cabbage", isFruit: false, id: 1 },
  { title: "Garlic", isFruit: false, id: 2 },
  { title: "Apple", isFruit: true, id: 3 },
];

export default function ShoppingList() {
  const listItems = products.map((product) => (
    <li
      key={product.id}
      style={{
        color: product.isFruit ? "magenta" : "darkgreen",
      }}
    >
      {product.title}
    </li>
  ));

  return <ul>{listItems}</ul>;
}
```

To run the project, use the following command. Then, you can refresh the HTTP 8080 Tab to preview the web page.

```bash
npm start
```
