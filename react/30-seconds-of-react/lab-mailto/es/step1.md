# Email Link

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual (VM). En general, solo necesitas agregar código a `script.js` y `style.css`.

Esta función crea un enlace que, cuando se hace clic en él, abre el cliente de correo electrónico del usuario y rellena un nuevo correo electrónico con el asunto y el contenido del cuerpo especificados. El enlace se formatea utilizando el protocolo `mailto:`.

Para utilizar la función, proporciona una propiedad `email` con la dirección de correo electrónico del destinatario, y opcionalmente, proporciona las propiedades `subject` y `body` para rellenar el correo electrónico con contenido inicial. Estas propiedades se codifican de forma segura utilizando `encodeURIComponent` antes de agregarlas a la URL del enlace.

El enlace se renderiza con el contenido proporcionado en `children`.

```jsx
const Mailto = ({ email, subject = "", body = "", children }) => {
  const params =
    subject || body
      ? `?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(
          body
        )}`
      : "";

  return <a href={`mailto:${email}${params}`}>{children}</a>;
};
```

Ejemplo de uso:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Mailto email="foo@bar.baz" subject="Hello & Welcome" body="Hello world!">
    Mail me!
  </Mailto>
);
```

Haz clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puedes actualizar la pestaña **Web 8080** para ver una vista previa de la página web.
