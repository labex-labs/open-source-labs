# Hook useMutationObserver de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual (VM). En general, solo necesitas agregar código a `script.js` y `style.css`.

Para monitorear los cambios realizados en el árbol DOM, se puede utilizar el hook `useMutationObserver`. Así es cómo funciona:

1. El hook recibe tres parámetros: `ref`, `callback` y `options`.
2. Dentro del hook, se utiliza un hook `useEffect()` que depende de los valores de `callback` y `options`.
3. Si la `ref` dada está inicializada, se crea un nuevo `MutationObserver` y se le pasa la función de devolución de llamada (`callback`).
4. Se llama a `MutationObserver.observe()` con las `options` dadas para monitorear la `ref` dada en busca de cambios.
5. Se utiliza `MutationObserver.disconnect()` para eliminar el observador de la `ref` cuando el componente se desmonta.

Aquí está el código:

```jsx
const useMutationObserver = (
  ref,
  callback,
  options = {
    attributes: true,
    characterData: true,
    childList: true,
    subtree: true
  }
) => {
  React.useEffect(() => {
    if (!ref.current) return;

    const observer = new MutationObserver(callback);
    observer.observe(ref.current, options);

    return () => observer.disconnect();
  }, [callback, options, ref]);
};
```

En el componente `App`, se utiliza el hook `useMutationObserver` para monitorear los cambios realizados en el elemento `mutationRef`. La función `incrementMutationCount` se pasa como la función de devolución de llamada (`callback`).

```jsx
const App = () => {
  const mutationRef = React.useRef();
  const [mutationCount, setMutationCount] = React.useState(0);

  const incrementMutationCount = React.useCallback(() => {
    setMutationCount((count) => count + 1);
  }, []);

  useMutationObserver(mutationRef, incrementMutationCount);

  const [content, setContent] = React.useState("Hello world");

  return (
    <>
      <label htmlFor="content-input">Edit this to update the text:</label>
      <textarea
        id="content-input"
        style={{ width: "100%" }}
        value={content}
        onChange={(e) => setContent(e.target.value)}
      />
      <div style={{ width: "100%" }} ref={mutationRef}>
        <div
          style={{
            resize: "both",
            overflow: "auto",
            maxWidth: "100%",
            border: "1px solid black"
          }}
        >
          <h2>Resize or change the content:</h2>
          <p>{content}</p>
        </div>
      </div>
      <div>
        <h3>Mutation count {mutationCount}</h3>
      </div>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Haz clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puedes actualizar la pestaña **Web 8080** para ver una vista previa de la página web.
