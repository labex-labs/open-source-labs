# React useComponentDidMount-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um eine Callback-Funktion sofort nach dem Mounten einer Komponente auszuführen, können Sie den `useEffect()`-Hook mit einem leeren Array als zweites Argument verwenden. Dadurch wird sichergestellt, dass der bereitgestellte Callback nur einmal ausgeführt wird, wenn die Komponente gemountet wird. Die unten gezeigte `useComponentDidMount()`-Funktion verwendet diesen Hook, um das gleiche Verhalten wie die `componentDidMount()`-Lebenszyklusmethode von Klassenkomponenten zu implementieren.

```jsx
const useComponentDidMount = (onMountHandler) => {
  React.useEffect(() => {
    onMountHandler();
  }, []);
};

const Mounter = () => {
  useComponentDidMount(() => console.log("Component did mount"));

  return <div>Check the console!</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Mounter />);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
