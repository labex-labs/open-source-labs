# Data List

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

This function renders a list of items from an array of primitive values. It can be used to conditionally render an ordered or unordered list based on the value of the `isOrdered` prop. To render each item from the `data` array, it uses `Array.prototype.map()` to create a `<li>` element with a unique `key` for every item.

```jsx
const DataList = ({ data, isOrdered = false }) => {
  const list = data.map((value, index) => (
    <li key={`${index}_${value}`}>{value}</li>
  ));

  return isOrdered ? <ol>{list}</ol> : <ul>{list}</ul>;
};
```

Here's an example of how you can use this component:

```jsx
const names = ["John", "Paul", "Mary"];
ReactDOM.createRoot(document.getElementById("root")).render(
  <>
    <DataList data={names} />
    <DataList data={names} isOrdered={true} />
  </>
);
```

In this example, we're passing an array of names to the `DataList` component and rendering it twice. The first time, we're rendering an unordered list, while the second time we're rendering an ordered list.

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
