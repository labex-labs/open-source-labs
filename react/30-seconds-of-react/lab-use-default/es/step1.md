# Hook useDefault de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Aquí está el código:

```jsx
const useDefault = (defaultState, initialState) => {
  const [value, setValue] = React.useState(initialState);
  const isEmpty = value === undefined || value === null;
  return [isEmpty ? defaultState : value, setValue];
};
```

```jsx
const UserCard = () => {
  const [user, setUser] = useDefault({ name: "Adam" }, { name: "John" });

  return (
    <>
      <div>Usuario: {user.name}</div>
      <input onChange={(e) => setUser({ name: e.target.value })} />
      <button onClick={() => setUser(null)}>Limpiar</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<UserCard />);
```

Para crear un valor con estado con un valor de retorno predeterminado, use el hook `useState()` en React. Verifique si el valor inicial es `null` o `undefined`. Si es así, devuelva el `defaultState` en su lugar, de lo contrario, devuelva el estado real `value` y la función `setValue`. El código anterior muestra cómo implementar esta funcionalidad en un hook personalizado llamado `useDefault`.

En el ejemplo proporcionado, `useDefault` se utiliza para crear un estado `user` con un valor predeterminado de `{ name: 'Adam' }`. El estado inicial se establece en `{ name: 'John' }`. En el componente `UserCard`, `user` se muestra junto con un campo de entrada para actualizar su nombre. También se proporciona un botón de limpiar para restablecer el estado a `null`. Finalmente, el componente se renderiza usando `ReactDOM.createRoot()`.

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
