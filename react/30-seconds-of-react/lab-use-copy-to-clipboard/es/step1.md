# React useCopyToClipboard Hook

> `index.html` y `script.js` ya se han proporcionado en la VM. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para copiar el texto dado al portapapeles, use el fragmento de código `copyToClipboard` proporcionado en `/js/s/copy-to-clipboard/` junto con el hook `useState()` para inicializar la variable `copied`. Para crear una devolución de llamada para el método `copyToClipboard`, use el hook `useCallback()`. Para restablecer la variable de estado `copied` cuando cambie el `text`, use el hook `useEffect()`. Finalmente, devuelva la variable de estado `copied` y la devolución de llamada `copy`.

El siguiente código demuestra un ejemplo de cómo usar estos hooks y métodos para crear un componente `TextCopy`. Cuando el usuario hace clic en el botón "Haz clic para copiar", se llama a la función `copy` y la variable `copied` se establece en `true`. Si la copia es exitosa, se mostrará "¡Copiado!".

```jsx
const useCopyToClipboard = (text) => {
  const copyToClipboard = (str) => {
    const el = document.createElement("textarea");
    el.value = str;
    el.setAttribute("readonly", "");
    el.style.position = "absolute";
    el.style.left = "-9999px";
    document.body.appendChild(el);
    const selected =
      document.getSelection().rangeCount > 0
        ? document.getSelection().getRangeAt(0)
        : false;
    el.select();
    const success = document.execCommand("copy");
    document.body.removeChild(el);
    if (selected) {
      document.getSelection().removeAllRanges();
      document.getSelection().addRange(selected);
    }
    return success;
  };

  const [copied, setCopied] = React.useState(false);

  const copy = React.useCallback(() => {
    if (!copied) setCopied(copyToClipboard(text));
  }, [text]);

  React.useEffect(() => () => setCopied(false), [text]);

  return [copied, copy];
};

const TextCopy = (props) => {
  const [copied, copy] = useCopyToClipboard("Lorem ipsum");

  return (
    <div>
      <button onClick={copy}>Click to copy</button>
      <span>{copied && "Copied!"}</span>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<TextCopy />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
