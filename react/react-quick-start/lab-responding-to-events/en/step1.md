# Responding to Events

> The React project have already been provided in the VM. In general, you only need to add code to `App.js`.

Please use the following command to install the dependencies:

```bash
npm i
```

React lets you add event handlers to your JSX. Event handlers are your own functions that will be triggered in response to interactions like clicking, hovering, focusing form inputs, and so on.

To add an event handler, you will first define a function and then [pass it as a prop](https://react.dev/learn/passing-props-to-a-component) to the appropriate JSX tag. For example, here is a button that doesn’t do anything yet:

```js
// App.js
export default function Button() {
  return <button>I don't do anything</button>;
}
```

You can make it show a message when a user clicks by following these three steps:

1. Declare a function called `handleClick` inside your `Button` component.
2. Implement the logic inside that function (use `alert` to show the message).
3. Add `onClick={handleClick}` to the `<button>` JSX.

```js
export default function Button() {
  function handleClick() {
    alert("You clicked me!");
  }

  return <button onClick={handleClick}>Click me</button>;
}
```

You defined the handleClick function and then passed it as a prop to `<button>`. handleClick is an event handler. Event handler functions:

Are usually defined inside your components.
Have names that start with handle, followed by the name of the event.

To run the project, use the following command. Then, you can refresh the **Web 8080** Tab to preview the web page.

```bash
npm start
```

By convention, it is common to name event handlers as handle followed by the event name. You’ll often see `onClick={handleClick}`, `onMouseEnter={handleMouseEnter}`, and so on.

Alternatively, you can define an event handler inline in the JSX:

```js
<button onClick={function handleClick() {
  alert('You clicked me!');
}}>
```

Or, more concisely, using an arrow function:

```js
<button onClick={() => {
  alert('You clicked me!');
}}>
```

All of these styles are equivalent. Inline event handlers are convenient for short functions.
