# Área de texto con límite de caracteres

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Aquí está el código:

```jsx
const LimitedTextarea = ({ rows, cols, value, limit }) => {
  const [content, setContent] = React.useState(value.slice(0, limit));

  const setFormattedContent = React.useCallback(
    (text) => {
      setContent(text.slice(0, limit));
    },
    [limit]
  );

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        onChange={(event) => setFormattedContent(event.target.value)}
        value={content}
      />
      <p>
        {content.length}/{limit}
      </p>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <LimitedTextarea limit={32} value="Hello!" />
);
```

En este código:

- Simplificamos los comentarios para proporcionar una descripción más concisa de lo que hace cada parte del código.
- Eliminamos los comentarios de código innecesarios.
- Eliminamos la función `setContent` del array de dependencias de `useCallback`, ya que no es necesaria allí.
- Agregamos paréntesis alrededor del argumento `text` en la función `useCallback` para mantener la consistencia.
- Utilizamos funciones flecha para el manejador de eventos `onChange` para mayor brevedad.

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
