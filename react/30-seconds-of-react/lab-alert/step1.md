# Closable Alert

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

Renders an alert component with the `type` prop.

The `Alert` component takes in the following props:

- `isDefaultShown`: a boolean that determines if the alert is initially shown or not (default is `false`)
- `timeout`: a number that specifies the duration in milliseconds before the alert fades out (default is `250`)
- `type`: a string that determines the type of alert (e.g. "warning", "error", "info")
- `message`: a string that contains the message to display in the alert

The component does the following:

- Uses the `useState()` hook to create the `isShown` and `isLeaving` state variables and sets both to `false` initially.
- Defines a `timeoutId` variable to keep the timer instance for clearing on component unmount.
- Uses the `useEffect()` hook to update the value of `isShown` to `true` and clear the interval by using `timeoutId` when the component is unmounted.
- Defines a `closeAlert` function to set the component as removed from the DOM by displaying a fading out animation and setting `isShown` to `false` via `setTimeout()`.
- Renders the alert component if `isShown` is `true`. The component has the appropriate styles based on the `type` prop and fades out if `isLeaving` is `true`.

Here's the code:

```css
@keyframes leave {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

.alert {
  padding: 0.75rem 0.5rem;
  margin-bottom: 0.5rem;
  text-align: left;
  padding-right: 40px;
  border-radius: 4px;
  font-size: 16px;
  position: relative;
}

.alert.warning {
  color: #856404;
  background-color: #fff3cd;
  border-color: #ffeeba;
}

.alert.error {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
}

.alert.leaving {
  animation: leave 0.5s forwards;
}

.alert .close {
  position: absolute;
  top: 0;
  right: 0;
  padding: 0 0.75rem;
  color: #333;
  border: 0;
  height: 100%;
  cursor: pointer;
  background: none;
  font-weight: 600;
  font-size: 16px;
}

.alert .close::after {
  content: "x";
}
```

```jsx
const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
  const [isShown, setIsShown] = React.useState(isDefaultShown);
  const [isLeaving, setIsLeaving] = React.useState(false);

  let timeoutId = null;

  React.useEffect(() => {
    setIsShown(true);
    return () => {
      clearTimeout(timeoutId);
    };
  }, [isDefaultShown, timeout, timeoutId]);

  const closeAlert = () => {
    setIsLeaving(true);
    timeoutId = setTimeout(() => {
      setIsLeaving(false);
      setIsShown(false);
    }, timeout);
  };

  return (
    isShown && (
      <div
        className={`alert ${type} ${isLeaving ? "leaving" : ""}`}
        role="alert"
      >
        <button className="close" onClick={closeAlert} />
        {message}
      </div>
    )
  );
};
```

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Alert type="info" message="This is info" />,
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
