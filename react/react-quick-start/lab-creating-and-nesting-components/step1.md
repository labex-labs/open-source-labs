# Creating and Nesting Components

> The React project have already been provided in the VM. In general, you only need to add code to `App.js`.

Please use the following command to install the dependencies:

```bash
npm i
```

React apps are made out of components. A component is a piece of the UI (user interface) that has its own logic and appearance. A component can be as small as a button, or as large as an entire page.

React components are JavaScript functions that return markup:

```js
// App.js
function MyButton() {
  return <button>I'm a button</button>;
}
```

Now that you’ve declared `MyButton`, you can nest it into another component:

```js
// App.js
export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
    </div>
  );
}
```

Notice that `<MyButton />` starts with a capital letter. That’s how you know it’s a React component. React component names must always start with a capital letter, while HTML tags must be lowercase.

The export default keywords specify the main component in the file. If you’re not familiar with some piece of JavaScript syntax, [MDN](https://developer.mozilla.org/en-US/docs/web/javascript/reference/statements/export) and [javascript.info](https://javascript.info/import-export) have great references.

To run the project, use the following command. Then, you can refresh the **Web 8080** Tab to preview the web page.

```bash
npm start
```
