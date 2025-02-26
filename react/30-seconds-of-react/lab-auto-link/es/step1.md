# Enlace de texto automático

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Este componente muestra una cadena como texto sin formato, con las URLs convertidas en elementos de enlace adecuados.

Para lograr esto, utiliza `String.prototype.split()` y `String.prototype.match()` con una expresión regular para encontrar URLs en la cadena dada. Las URLs coincidentes se devuelven como elementos `<a>`, manejando los prefijos de protocolo faltantes si es necesario. Las partes restantes de la cadena se muestran como texto sin formato.

Aquí está el código:

```jsx
const AutoLink = ({ text }) => {
  const urlRegex =
    /((?:https?:\/\/)?(?:(?:[a-z0-9]?(?:[a-z0-9\-]{1,61}[a-z0-9])?\.[^\.|\s])+[a-z\.]*[a-z]+|(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})(?::\d{1,5})*[a-z0-9.,_\/~#&=;%+?\-\\(\\)]*)/gi;

  const renderText = () => {
    return text.split(urlRegex).map((word, index) => {
      const urlMatch = word.match(urlRegex);
      if (urlMatch) {
        const url = urlMatch[0];
        return (
          <a key={index} href={url.startsWith("http") ? url : `http://${url}`}>
            {url}
          </a>
        );
      }
      return <span key={index}>{word}</span>;
    });
  };

  return <div>{renderText()}</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <AutoLink text="foo bar baz http://example.org bar" />
);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
