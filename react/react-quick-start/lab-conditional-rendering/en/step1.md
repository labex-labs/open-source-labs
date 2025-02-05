# Conditional Rendering

> The React project have already been provided in the VM. In general, you only need to add code to `App.js`.

Please use the following command to install the dependencies:

```bash
npm i
```

In React, there is no special syntax for writing conditions. Instead, you’ll use the same techniques as you use when writing regular JavaScript code. For example, you can use an `if` statement to conditionally include JSX:

```js
if (isPacked) {
  return <li className="item">{name} ✔</li>;
}
return <li className="item">{name}</li>;
```

If you prefer more compact code, you can use the conditional `?` operator. Unlike `if`, it works inside JSX:

```js
return <li className="item">{isPacked ? name + " ✔" : name}</li>;
```

When you don’t need the else branch, you can also use a shorter logical `&&` syntax:

```js
return <li className="item">{isPacked && name + " ✔"}</li>;
```

If the isPacked prop is true, this code returns a different JSX tree. With this change, some of the items get a checkmark at the end:

```js
// App.js
function Item({ name, isPacked }) {
  if (isPacked) {
    return <li className="item">{name} ✔</li>;
  }
  return <li className="item">{name}</li>;
}

export default function PackingList() {
  return (
    <section>
      <h1>Sally Ride's Packing List</h1>
      <ul>
        <Item isPacked={true} name="Space suit" />
        <Item isPacked={true} name="Helmet with a golden leaf" />
        <Item isPacked={false} name="Photo of Tam" />
      </ul>
    </section>
  );
}
```

To run the project, use the following command. Then, you can refresh the **Web 8080** Tab to preview the web page.

```bash
npm start
```
