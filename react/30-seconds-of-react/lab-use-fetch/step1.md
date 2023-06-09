# React useFetch Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

Refactored code:

```jsx
const useFetch = (url, options) => {
  const [response, setResponse] = React.useState(null);
  const [error, setError] = React.useState(null);
  const [abort, setAbort] = React.useState(() => {});

  React.useEffect(() => {
    const abortController = new AbortController();
    const signal = abortController.signal;
    setAbort(abortController.abort);

    const fetchData = async () => {
      try {
        const res = await fetch(url, { ...options, signal });
        const json = await res.json();
        setResponse(json);
      } catch (error) {
        setError(error);
      }
    };
    fetchData();

    return () => {
      abort();
    };
  }, []);

  return { response, error, abort };
};

const ImageFetch = (props) => {
  const res = useFetch("https://dog.ceo/api/breeds/image/random", {});

  if (!res.response) {
    return <div>Loading...</div>;
  }

  const imageUrl = res.response.message;

  return (
    <div>
      <img src={imageUrl} alt="avatar" width={400} height="auto" />
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<ImageFetch />);
```

Explanation:

- The purpose of the code is to implement a `fetch()` call in a declarative manner using React hooks.
- The `useFetch` hook takes two parameters: a `url` and `options` object.
- The hook initializes three state variables using the `useState()` hook: `response`, `error`, and `abort`.
- The `useEffect()` hook is used to asynchronously call `fetch()` and update the state variables accordingly.
- An `AbortController` is used to allow aborting the request, and it's used to cancel the request when the component unmounts.
- The hook returns an object containing the `response`, `error`, and `abort` state variables.
- The `ImageFetch` component uses the `useFetch` hook to fetch a random dog image and display it in an `<img>` element.

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
