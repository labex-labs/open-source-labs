# Object Table View

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

This component renders a table with rows that are dynamically created from an array of objects and a list of property names. To achieve this:

- Use `Object.keys()`, `Array.prototype.filter()`, `Array.prototype.includes()`, and `Array.prototype.reduce()` to produce a `filteredData` array that contains all objects with the keys specified in `propertyNames`.
- Render a `<table>` element with a set of columns equal to the number of values in `propertyNames`.
- Use `Array.prototype.map()` to render each value in the `propertyNames` array as a `<th>` element.
- Use `Array.prototype.map()` to render each object in the `filteredData` array as a `<tr>` element containing a `<td>` for each key in the object.
- Note that this component does not work with nested objects and will break if there are nested objects inside any of the properties specified in `propertyNames`.

Here's the code:

```jsx
const MappedTable = ({ data, propertyNames }) => {
  const filteredData = data.map((obj) =>
    Object.keys(obj)
      .filter((key) => propertyNames.includes(key))
      .reduce((acc, key) => ({ ...acc, [key]: obj[key] }), {})
  );

  return (
    <table>
      <thead>
        <tr>
          {propertyNames.map((name) => (
            <th key={`header-${name}`}>{name}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {filteredData.map((obj, i) => (
          <tr key={`row-${i}`}>
            {propertyNames.map((name) => (
              <td key={`cell-${i}-${name}`}>{obj[name]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

You can use the component by passing in an array of objects and a list of property names:

```jsx
const people = [
  { name: "John", surname: "Smith", age: 42 },
  { name: "Adam", surname: "Smith", gender: "male" }
];
const propertyNames = ["name", "surname", "age"];

ReactDOM.render(
  <MappedTable data={people} propertyNames={propertyNames} />,
  document.getElementById("root")
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
