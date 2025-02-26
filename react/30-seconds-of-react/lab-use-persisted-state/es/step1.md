# Hook usePersistedState de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Este hook devuelve un valor con estado que se persiste en `localStorage`, junto con una función que se puede usar para actualizarlo. Para usarlo, siga estos pasos:

1. Utilice el hook `useState()` para inicializar el `valor` a `valorPredeterminado`.
2. Utilice el hook `useRef()` para crear una referencia que contendrá el `nombre` del valor en `Window.localStorage`.
3. Utilice 3 instancias del hook `useEffect()` para la inicialización, el cambio de `valor` y el cambio de `nombre` respectivamente.
4. Cuando el componente se monta por primera vez, use `Storage.getItem()` para actualizar `valor` si hay un valor almacenado, o `Storage.setItem()` para persistir el valor actual.
5. Cuando `valor` se actualiza, use `Storage.setItem()` para almacenar el nuevo valor.
6. Cuando `nombre` se actualiza, use `Storage.setItem()` para crear la nueva clave, actualizar la `referenciaNombre` y use `Storage.removeItem()` para eliminar la clave anterior de `Window.localStorage`.
7. Tenga en cuenta que el hook está destinado a usarse con valores primitivos (es decir, no objetos) y no tiene en cuenta los cambios en `Window.localStorage` debido a otro código. Ambos problemas se pueden manejar fácilmente (por ejemplo, serialización JSON y manejo del evento `'storage'`).

Aquí está el código:

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

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
