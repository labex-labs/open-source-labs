# Updating the Screen

> The React project have already been provided in the VM. In general, you only need to add code to `App.js`.

Please use the following command to install the dependencies:

```bash
npm i
```

Often, you’ll want your component to “remember” some information and display it. For example, maybe you want to count the number of times a button is clicked. To do this, add state to your component.

First, import `useState` from React:

```js
import { useState } from "react";
```

Now you can declare a state variable inside your component:

```js
function MyButton() {
  const [count, setCount] = useState(0);
  // ...
```

You’ll get two things from `useState`: the current state (`count`), and the function that lets you update it (`setCount`). You can give them any names, but the convention is to write `[something, setSomething]`.

The first time the button is displayed, `count` will be `0` because you passed 0 to `useState()`. When you want to change state, call `setCount()` and pass the new value to it. Clicking this button will increment the counter:

```js
function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return <button onClick={handleClick}>Clicked {count} times</button>;
}
```

React will call your component function again. This time, `count` will be `1`. Then it will be `2`. And so on.

If you render the same component multiple times, each will get its own state. Click each button separately:

```js
// App.js
import { useState } from "react";

export default function MyApp() {
  return (
    <div>
      <h1>Counters that update separately</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return <button onClick={handleClick}>Clicked {count} times</button>;
}
```

Notice how each button “remembers” its own `count` state and doesn’t affect other buttons.

To run the project, use the following command. Then, you can refresh the **Web 8080** Tab to preview the web page.

```bash
npm start
```
