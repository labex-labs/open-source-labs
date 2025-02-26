# Zone de glisser-déposer de fichiers

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Ce composant permet la fonctionnalité de glisser-déposer pour un seul fichier. Pour implémenter ce composant, suivez ces étapes :

1. Créez une référence appelée `dropRef` et liez-la au wrapper du composant.
2. Utilisez le hook `useState()` pour créer les variables `drag` et `filename`. Initialisez-les respectivement à `false` et `''`.
3. Les variables `dragCounter` et `drag` sont utilisées pour déterminer si un fichier est en train d'être déplacé, tandis que `filename` est utilisée pour stocker le nom du fichier déposé.
4. Créez les méthodes `handleDrag`, `handleDragIn`, `handleDragOut` et `handleDrop` pour gérer la fonctionnalité de glisser-déposer. `handleDrag` empêche le navigateur d'ouvrir le fichier déplacé, `handleDragIn` et `handleDragOut` gèrent l'entrée et la sortie du fichier déplacé dans le composant, et `handleDrop` gère le déplacement du fichier et le transmet à `onDrop`.
5. Utilisez le hook `useEffect()` pour gérer chacun des événements de glisser-déposer à l'aide des méthodes précédemment créées.

Voici le CSS pour le composant :

```css
.filedrop {
  min-height: 120px;
  border: 3px solid #d3d3d3;
  text-align: center;
  font-size: 24px;
  padding: 32px;
  border-radius: 4px;
}

.filedrop.drag {
  border: 3px dashed #1e90ff;
}

.filedrop.ready {
  border: 3px solid #32cd32;
}
```

Voici le JSX pour le composant :

```jsx
const FileDrop = ({ onDrop }) => {
  const [drag, setDrag] = React.useState(false);
  const [filename, setFilename] = React.useState("");
  const dropRef = React.useRef(null);
  let dragCounter = 0;

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleDragIn = (e) => {
    e.preventDefault();
    e.stopPropagation();
    dragCounter++;
    if (e.dataTransfer.items && e.dataTransfer.items.length > 0) setDrag(true);
  };

  const handleDragOut = (e) => {
    e.preventDefault();
    e.stopPropagation();
    dragCounter--;
    if (dragCounter === 0) setDrag(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDrag(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      onDrop(e.dataTransfer.files[0]);
      setFilename(e.dataTransfer.files[0].name);
      e.dataTransfer.clearData();
      dragCounter = 0;
    }
  };

  React.useEffect(() => {
    const div = dropRef.current;
    div.addEventListener("dragenter", handleDragIn);
    div.addEventListener("dragleave", handleDragOut);
    div.addEventListener("dragover", handleDrag);
    div.addEventListener("drop", handleDrop);
    return () => {
      div.removeEventListener("dragenter", handleDragIn);
      div.removeEventListener("dragleave", handleDragOut);
      div.removeEventListener("dragover", handleDrag);
      div.removeEventListener("drop", handleDrop);
    };
  }, []);

  return (
    <div
      ref={dropRef}
      className={
        drag ? "filedrop drag" : filename ? "filedrop ready" : "filedrop"
      }
    >
      {filename && !drag ? <div>{filename}</div> : <div>Drop a file here!</div>}
    </div>
  );
};
```

Pour utiliser le composant, appelez `ReactDOM.createRoot(document.getElementById('root')).render(<FileDrop onDrop={console.log} />);`

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
