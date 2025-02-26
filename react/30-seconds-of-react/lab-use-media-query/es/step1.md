# React useMediaQuery Hook

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Esta función comprueba si el entorno actual coincide con una consulta de medios dada y devuelve el valor adecuado.

- Primero, comprueba si `Window` y `Window.matchMedia()` existen. Si no es así (por ejemplo, en un entorno SSR o un navegador no compatible), devuelve `whenFalse`.
- Utiliza `Window.matchMedia()` para coincidir con la `query` dada. Castea su propiedad `matches` a un booleano y guárdalo en una variable de estado, `match`, utilizando el hook `useState()`.
- Utiliza el hook `useEffect()` para agregar un oyente de cambios y para limpiar los oyentes después de que el hook se destruya.
- Finalmente, devuelve `whenTrue` o `whenFalse` según el valor de `match`.

```jsx
const useMediaQuery = (query, whenTrue, whenFalse) => {
  if (
    typeof window === "undefined" ||
    typeof window.matchMedia === "undefined"
  ) {
    return whenFalse;
  }

  const mediaQuery = window.matchMedia(query);
  const [match, setMatch] = React.useState(!!mediaQuery.matches);

  React.useEffect(() => {
    const handler = () => setMatch(!!mediaQuery.matches);
    mediaQuery.addListener(handler);
    return () => mediaQuery.removeListener(handler);
  }, [mediaQuery]);

  return match ? whenTrue : whenFalse;
};
```

```jsx
const ResponsiveText = () => {
  const text = useMediaQuery(
    "(max-width: 400px)",
    "Menos de 400px de ancho",
    "Más de 400px de ancho"
  );

  return <span>{text}</span>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<ResponsiveText />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
