# React useAsync Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

This code creates a custom hook that handles asynchronous calls. It accepts a handler function, `fn`, and returns an object containing the properties of `state` (`value`, `error`, and `loading`) and an asynchronous `run` function. The `run` function runs the provided callback, `fn`, while using `dispatch` to update `state` as necessary.

```jsx
const useAsync = (fn) => {
  const initialState = { loading: false, error: null, value: null };

  const stateReducer = (state, action) => {
    switch (action.type) {
      case "start":
        return { loading: true, error: null, value: null };
      case "finish":
        return { loading: false, error: null, value: action.value };
      case "error":
        return { loading: false, error: action.error, value: null };
      default:
        return state;
    }
  };

  const [state, dispatch] = React.useReducer(stateReducer, initialState);

  const run = async (args = null) => {
    try {
      dispatch({ type: "start" });
      const value = await fn(args);
      dispatch({ type: "finish", value });
    } catch (error) {
      dispatch({ type: "error", error });
    }
  };

  return { ...state, run };
};

const RandomImage = (props) => {
  const imgFetch = useAsync((url) =>
    fetch(url).then((response) => response.json())
  );

  return (
    <div>
      <button
        onClick={() => imgFetch.run("https://dog.ceo/api/breeds/image/random")}
        disabled={imgFetch.loading}
      >
        Load image
      </button>
      <br />
      {imgFetch.loading && <div>Loading...</div>}
      {imgFetch.error && <div>Error {imgFetch.error}</div>}
      {imgFetch.value && (
        <img
          src={imgFetch.value.message}
          alt="avatar"
          width={400}
          height="auto"
        />
      )}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<RandomImage />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
