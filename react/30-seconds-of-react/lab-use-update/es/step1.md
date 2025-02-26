# React useUpdate Hook

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para forzar la re-renderización de un componente cuando es llamado, use el hook `useReducer()` para crear un nuevo objeto cada vez que se actualiza y devolver su dispatch. Aquí hay una implementación de ejemplo de la función `useUpdate()`:

```jsx
const useUpdate = () => {
  const [, update] = React.useReducer(() => ({}));
  return update;
};
```

Luego, puede usar `useUpdate()` en su componente para desencadenar una re-renderización cuando sea necesario:

```jsx
const MyApp = () => {
  const update = useUpdate();

  return (
    <>
      <div>Time: {Date.now()}</div>
      <button onClick={update}>Update</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
