# React useLocalStorage Hook

> `index.html` y `script.js` ya se han proporcionado en la VM. En general, solo es necesario agregar código a `script.js` y `style.css`.

Esta función crea un valor que se guarda en `localStorage` y una función para modificarlo. Aquí está cómo funciona:

1. Para crear el valor, use el hook `useState()` con una función para inicializarlo de manera perezosa.
2. Para recuperar el valor guardado de `localStorage`, use un bloque `try...catch` y `Storage.getItem()`. Si no hay un valor guardado, use `Storage.setItem()` para almacenar el `defaultValue` y usarlo como el estado inicial. Si hay un error, use `defaultValue`.
3. Defina una función que actualice la variable de estado con el valor pasado y use `Storage.setItem()` para guardarlo.

Aquí está el código:

```jsx
const useLocalStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.localStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.localStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.localStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

Puedes usar esta función en tu aplicación de la siguiente manera:

```jsx
const MyApp = () => {
  const [name, setName] = useLocalStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
