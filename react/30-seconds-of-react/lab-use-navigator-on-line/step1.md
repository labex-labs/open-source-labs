# React useNavigatorOnLine Hook

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

To check if the client is online or offline, you can create a `getOnLineStatus` function that utilizes the `Navigator.onLine` web API. Then, to implement this functionality in a React component, you can use the `useNavigatorOnLine` custom hook. This hook creates a state variable called `status` using the `useState()` hook and sets it to the value returned by `getOnLineStatus()`. The `useEffect()` hook is used to add event listeners for when the online/offline status changes, update the `status` state variable accordingly, and clean up those listeners when the component unmounts. Finally, the `isOnline` variable returned by `useNavigatorOnLine()` can be used to render a message indicating whether the client is online or offline.

```jsx
const getOnLineStatus = () => typeof navigator !== 'undefined' && typeof navigator.onLine === 'boolean' ? navigator.onLine : true;

const useNavigatorOnLine = () => {
  const [status, setStatus] = React.useState(getOnLineStatus());

  const setOnline = () => setStatus(true);
  const setOffline = () => setStatus(false);

  React.useEffect(() => {
    window.addEventListener('online', setOnline);
    window.addEventListener('offline', setOffline);

    return () => {
      window.removeEventListener('online', setOnline);
      window.removeEventListener('offline', setOffline);
    };
  }, []);

  return status;
};

const StatusIndicator = () => {
  const isOnline = useNavigatorOnLine();

  return <span>You are {isOnline ? 'online' : 'offline'}.</span>;
};

ReactDOM.createRoot(document.getElementById('root')).render(<StatusIndicator />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
