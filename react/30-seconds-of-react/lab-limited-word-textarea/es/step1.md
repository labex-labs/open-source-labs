# Área de texto con límite de palabras

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

```jsx
// Muestra un componente de área de texto con un límite de palabras.
const LimitedWordTextarea = ({ filas, columnas, valor, límite }) => {
  const [{ contenido, cantidadPalabras }, establecerContenido] = React.useState(
    {
      contenido: valor,
      cantidadPalabras: 0
    }
  );

  // Crea una función memoizada que formatea el texto de entrada.
  const establecerContenidoFormateado = React.useCallback(
    (texto) => {
      const palabras = texto.split(" ").filter(Boolean);
      const truncado = palabras.slice(0, límite).join(" ");
      establecerContenido({
        contenido: palabras.length > límite ? truncado : texto,
        cantidadPalabras: palabras.length > límite ? límite : palabras.length
      });
    },
    [límite, establecerContenido]
  );

  // Llama a establecerContenidoFormateado con el valor inicial de contenido.
  React.useEffect(() => {
    establecerContenidoFormateado(contenido);
  }, []);

  return (
    <>
      <textarea
        filas={filas}
        columnas={columnas}
        valor={contenido}
        onChange={(evento) =>
          establecerContenidoFormateado(evento.target.value)
        }
      />
      <p>
        {cantidadPalabras}/{límite}
      </p>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <LimitedWordTextarea límite={5} valor="Hello there!" />
);
```

Cambios realizados:

- Se agregaron comentarios para explicar lo que hace cada parte del código.
- Se simplificó la lógica en `establecerContenidoFormateado` para hacerlo más conciso.
- Se movió la función `establecerContenido` al final de la llamada de función para que sea más fácil de leer.
- Se reordenaron las propiedades en el componente `<textarea>` para mantener la consistencia.
- Se eliminaron espacios y saltos de línea innecesarios.

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
