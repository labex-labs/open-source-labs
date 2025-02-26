# React useNavigatorOnLine-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um zu überprüfen, ob der Client online oder offline ist, können Sie eine `getOnLineStatus`-Funktion erstellen, die die `Navigator.onLine`-Web-API nutzt. Um diese Funktionalität in einem React-Komponenten zu implementieren, können Sie den benutzerdefinierten `useNavigatorOnLine`-Hook verwenden. Dieser Hook erstellt eine Zustandsvariable namens `status` mithilfe des `useState()`-Hooks und setzt sie auf den von `getOnLineStatus()` zurückgegebenen Wert. Der `useEffect()`-Hook wird verwendet, um Ereignislistener für den Fall hinzuzufügen, dass der Online-/Offline-Zustand sich ändert, den `status`-Zustandsvariablen entsprechend zu aktualisieren und diese Listener zu bereinigen, wenn die Komponente entfernt wird. Schließlich kann die von `useNavigatorOnLine()` zurückgegebene `isOnline`-Variable verwendet werden, um eine Nachricht anzuzeigen, die angibt, ob der Client online oder offline ist.

```jsx
const getOnLineStatus = () =>
  typeof navigator !== "undefined" && typeof navigator.onLine === "boolean"
    ? navigator.onLine
    : true;

const useNavigatorOnLine = () => {
  const [status, setStatus] = React.useState(getOnLineStatus());

  const setOnline = () => setStatus(true);
  const setOffline = () => setStatus(false);

  React.useEffect(() => {
    window.addEventListener("online", setOnline);
    window.addEventListener("offline", setOffline);

    return () => {
      window.removeEventListener("online", setOnline);
      window.removeEventListener("offline", setOffline);
    };
  }, []);

  return status;
};

const StatusIndicator = () => {
  const isOnline = useNavigatorOnLine();

  return <span>You are {isOnline ? "online" : "offline"}.</span>;
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <StatusIndicator />
);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
