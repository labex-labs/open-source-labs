# React useComponentWillUnmount-Hook

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um eine Callback-Funktion unmittelbar vor dem Entfernen und Zerstören eines Komponenten auszuführen, können Sie den `useEffect()`-Hook mit einem leeren Array als zweites Argument verwenden. Geben Sie die bereitgestellte Callback-Funktion zurück, um sie nur einmal vor der Bereinigung auszuführen. Dieses Verhalten ähnelt der `componentWillUnmount()`-Lebenszyklusmethode von Klassenkomponenten. Sie können auch den folgenden Codeausschnitt verwenden, um einen benutzerdefinierten Hook `useComponentWillUnmount()` zu erstellen, der eine `onUnmountHandler`-Funktion als Argument nimmt und sie vor dem Entfernen des Komponenten ausführt:

```jsx
const useComponentWillUnmount = (onUnmountHandler) => {
  React.useEffect(
    () => () => {
      onUnmountHandler();
    },
    []
  );
};
```

Sie können diesen benutzerdefinierten Hook dann in Ihrer Funktionskomponente wie folgt verwenden:

```jsx
const Unmounter = () => {
  useComponentWillUnmount(() => console.log("Component will unmount"));

  return <div>Check the console!</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Unmounter />);
```

Dies wird "Component will unmount" in der Konsole ausgeben, wenn das Komponenten entfernt werden soll.

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
