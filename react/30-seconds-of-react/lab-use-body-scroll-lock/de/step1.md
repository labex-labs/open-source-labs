# React useBodyScrollLock-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Dieser Codeausschnitt ermöglicht es Benutzern, den Body-Scroll zu sperren, wenn ein Modal geöffnet ist. So funktioniert es:

Zunächst wird die `useBodyScrollLock`-Funktion definiert, die den `useLayoutEffect`-Hook verwendet, um den Scroll des `body`-Elements zu sperren. Dieser Hook wird nur einmal beim Mounten der Komponente ausgeführt und setzt den `overflow`-Wert des `body`-Elements auf `'hidden'`. Wenn die Komponente entnommen wird, wird der ursprüngliche `overflow`-Wert wiederhergestellt.

```jsx
const useBodyScrollLock = () => {
  React.useLayoutEffect(() => {
    const originalStyle = window.getComputedStyle(document.body).overflow;
    document.body.style.overflow = "hidden";
    return () => (document.body.style.overflow = originalStyle);
  }, []);
};
```

Anschließend wird die `Modal`-Komponente definiert, die die `useBodyScrollLock`-Funktion nutzt. Diese Komponente zeigt eine Nachricht in einem auf dem Bildschirm zentrierten Kasten an. Wenn der Kasten angeklickt wird, wird das Modal geschlossen und der Body-Scroll entsperrt.

```jsx
const Modal = ({ onClose }) => {
  useBodyScrollLock();

  return (
    <div
      style={{
        zIndex: 100,
        background: "rgba(0,0,0,0.25)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center"
      }}
      onClick={onClose}
    >
      <p style={{ padding: 8, borderRadius: 8, background: "#fff" }}>
        Scroll gesperrt! <br /> Klicken Sie mich, um zu entsperren
      </p>
    </div>
  );
};
```

Schließlich wird die `MyApp`-Komponente definiert, die einen Button rendert, der das `Modal`-Komponente öffnet, wenn er angeklickt wird.

```jsx
const MyApp = () => {
  const [modalOpen, setModalOpen] = React.useState(false);

  return (
    <div
      style={{
        height: "400vh",
        textAlign: "center",
        paddingTop: 100,
        background: "linear-gradient(to bottom, #1fa2ff, #12d8fa, #a6ffcb)"
      }}
    >
      <button onClick={() => setModalOpen(true)}>Modal öffnen</button>
      {modalOpen && <Modal onClose={() => setModalOpen(false)} />}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
