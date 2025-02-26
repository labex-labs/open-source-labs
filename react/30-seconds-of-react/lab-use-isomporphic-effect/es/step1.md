# React useIsomporphicEffect Hook

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para garantizar el uso adecuado de `useEffect()` en el servidor y `useLayoutEffect()` en el cliente, se puede usar `typeof` para comprobar si el objeto `Window` está definido. Si es así, devuelva `useLayoutEffect()`, de lo contrario devuelva `useEffect()`. Aquí hay un ejemplo de cómo implementar esto:

```jsx
const useIsomorphicEffect =
  typeof window !== "undefined" ? React.useLayoutEffect : React.useEffect;
```

Luego, en su código, puede usar `useIsomorphicEffect()` como se muestra en este ejemplo:

```jsx
const MyApp = () => {
  useIsomorphicEffect(() => {
    window.console.log("Hello");
  }, []);

  return null;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Esto registrará 'Hello' en la consola cuando el componente se monte y funcionará correctamente tanto en el servidor como en el cliente.

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
