# Data Table

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

Here's the revised content:

---

Create a table element with two columns, `ID` and `Value`, where each row is generated dynamically from an array of primitive values.

To accomplish this, use the `Array.prototype.map()` method to create a new array of JSX elements representing each item in the input `data` array as a `<tr>` element with an appropriate `key`. Within each `<tr>`, add two `<td>` elements to display the row's index and value respectively.

Here's an example implementation:

```jsx
const DataTable = ({ data }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Value</th>
        </tr>
      </thead>
      <tbody>
        {data.map((val, i) => (
          <tr key={`${i}_${val}`}>
            <td>{i}</td>
            <td>{val}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

To use this component with an array of people's names, for example, you can call it as follows:

```jsx
const people = ["John", "Jesse"];
ReactDOM.createRoot(document.getElementById("root")).render(
  <DataTable data={people} />
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
