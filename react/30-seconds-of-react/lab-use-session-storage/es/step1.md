# Hook useSessionStorage de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para crear un valor con estado que se persista en `sessionStorage` y una función para actualizarlo, siga estos pasos:

1. Utilice el hook `useState()` con una función para inicializar su valor de manera perezosa.
2. Utilice un bloque `try...catch` y `Storage.getItem()` para intentar obtener el valor de `Window.sessionStorage`. Si no se encuentra ningún valor, utilice `Storage.setItem()` para almacenar el `defaultValue` y usarlo como estado inicial. Si ocurre un error, utilice `defaultValue` como estado inicial.
3. Defina una función que actualizará la variable de estado con el valor pasado y utilice `Storage.setItem()` para almacenarlo.

A continuación, se muestra una implementación de ejemplo:

```jsx
const useSessionStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.sessionStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.sessionStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.sessionStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

Puede usar este hook en su aplicación de la siguiente manera:

```jsx
const MyApp = () => {
  const [name, setName] = useSessionStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
