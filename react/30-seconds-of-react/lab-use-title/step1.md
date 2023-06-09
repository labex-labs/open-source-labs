# React useTitle Hook

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

To set the title of the page, you can use the `useTitle` custom hook. This hook uses `typeof` to check if the `Document` is defined. If it is defined, the `useRef()` hook is used to store the original title of the `Document`. The `useEffect()` hook is then used to set `Document.title` to the passed value when the component mounts and clean up when unmounting.

```jsx
const useTitle = (title) => {
  const documentDefined = typeof document !== "undefined";
  const originalTitle = React.useRef(documentDefined ? document.title : null);

  React.useEffect(() => {
    if (!documentDefined) return;

    if (document.title !== title) {
      document.title = title;
    }

    return () => {
      document.title = originalTitle.current;
    };
  }, [title]);
};
```

In the example code, the `Alert` component uses the `useTitle` hook to set the title to "Alert". The `MyApp` component renders a button that toggles the `Alert` component.

```jsx
const Alert = () => {
  useTitle("Alert");

  return (
    <div>
      <p>Alert! Title has changed</p>
    </div>
  );
};

const MyApp = () => {
  const [alertOpen, setAlertOpen] = React.useState(false);

  return (
    <div>
      <button onClick={() => setAlertOpen(!alertOpen)}>Toggle alert</button>
      {alertOpen && <Alert />}
    </div>
  );
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
