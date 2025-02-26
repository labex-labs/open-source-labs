# React usePersistedState Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Ce hook renvoie une valeur d'état qui est conservée dans `localStorage`, ainsi qu'une fonction qui peut être utilisée pour la mettre à jour. Pour l'utiliser, suivez ces étapes :

1. Utilisez le hook `useState()` pour initialiser la `value` à `defaultValue`.
2. Utilisez le hook `useRef()` pour créer une réf qui contiendra le `name` de la valeur dans `Window.localStorage`.
3. Utilisez 3 instances du hook `useEffect()` pour l'initialisation, le changement de `value` et le changement de `name` respectivement.
4. Lorsque le composant est monté pour la première fois, utilisez `Storage.getItem()` pour mettre à jour `value` s'il existe une valeur stockée, ou `Storage.setItem()` pour conserver la valeur actuelle.
5. Lorsque `value` est mise à jour, utilisez `Storage.setItem()` pour stocker la nouvelle valeur.
6. Lorsque `name` est mis à jour, utilisez `Storage.setItem()` pour créer la nouvelle clé, mettre à jour la `nameRef`, et utilisez `Storage.removeItem()` pour supprimer la clé précédente de `Window.localStorage`.
7. Notez que le hook est destiné à être utilisé avec des valeurs primitives (c'est-à-dire pas des objets) et ne tient pas compte des changements apportés à `Window.localStorage` par d'autres codes. Ces deux problèmes peuvent être facilement gérés (par exemple, la sérialisation JSON et la gestion de l'événement `'storage'`).

Voici le code :

```jsx
const usePersistedState = (name, defaultValue) => {
  const [value, setValue] = React.useState(defaultValue);
  const nameRef = React.useRef(name);

  React.useEffect(() => {
    try {
      const storedValue = localStorage.getItem(name);
      if (storedValue !== null) {
        setValue(storedValue);
      } else {
        localStorage.setItem(name, defaultValue);
      }
    } catch {
      setValue(defaultValue);
    }
  }, []);

  React.useEffect(() => {
    try {
      localStorage.setItem(nameRef.current, value);
    } catch {}
  }, [value]);

  React.useEffect(() => {
    const lastName = nameRef.current;
    if (name !== lastName) {
      try {
        localStorage.setItem(name, value);
        nameRef.current = name;
        localStorage.removeItem(lastName);
      } catch {}
    }
  }, [name]);

  return [value, setValue];
};
```

```jsx
const MyComponent = ({ name }) => {
  const [value, setValue] = usePersistedState(name, 10);

  const handleInputChange = (event) => {
    setValue(event.target.value);
  };

  return <input value={value} onChange={handleInputChange} />;
};

const MyApp = () => {
  const [name, setName] = React.useState("my-value");

  const handleInputChange = (event) => {
    setName(event.target.value);
  };

  return (
    <>
      <MyComponent name={name} />
      <input value={name} onChange={handleInputChange} />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
