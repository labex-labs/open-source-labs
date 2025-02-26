# React useBodyScrollLock Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Ce fragment de code permet aux utilisateurs de bloquer le défilement du corps lorsqu'un modal est ouvert. Voici comment cela fonctionne :

Tout d'abord, la fonction `useBodyScrollLock` est définie, qui utilise le hook `useLayoutEffect` pour bloquer le défilement de l'élément `body`. Ce hook s'exécute une seule fois lors du montage du composant, et il définit la valeur de `overflow` de l'élément `body` sur `'hidden'`. Lorsque le composant est démonté, la valeur d'`overflow` d'origine est restaurée.

```jsx
const useBodyScrollLock = () => {
  React.useLayoutEffect(() => {
    const originalStyle = window.getComputedStyle(document.body).overflow;
    document.body.style.overflow = "hidden";
    return () => (document.body.style.overflow = originalStyle);
  }, []);
};
```

Ensuite, le composant `Modal` est défini, qui utilise la fonction `useBodyScrollLock`. Ce composant affiche un message dans une boîte centrée sur l'écran. Lorsque la boîte est cliquée, le modal est fermé et le défilement du corps est débloqué.

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
        Scroll bloqué! <br /> Cliquez sur moi pour le débloquer
      </p>
    </div>
  );
};
```

Enfin, le composant `MyApp` est défini, qui affiche un bouton qui ouvre le composant `Modal` lorsqu'il est cliqué.

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
      <button onClick={() => setModalOpen(true)}>Ouvrir le modal</button>
      {modalOpen && <Modal onClose={() => setModalOpen(false)} />}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
