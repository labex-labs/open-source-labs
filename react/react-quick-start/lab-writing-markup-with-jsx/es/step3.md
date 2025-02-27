# Agregando estilos

En React, se especifica una clase CSS con `className`. Funciona de la misma manera que el atributo HTML [class](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/class):

```html
<img className="avatar" />
```

Luego, se escriben las reglas CSS para ello en un archivo CSS separado:

```css
/* App.css */
.avatar {
  border-radius: 50%;
}
```

React no prescriba cómo agregar archivos CSS. En el caso más simple, agregará una etiqueta `<link>` a su HTML. Si utiliza una herramienta de compilación o un framework, consulte su documentación para aprender cómo agregar un archivo CSS a su proyecto.

```js
// App.js
import "./App.css";
```

También se pueden poner expresiones más complejas dentro de las llaves curvas de JSX, por ejemplo, [concatenación de cadenas](https://javascript.info/operators#string-concatenation-with-binary):

```js
// App.js
const user = {
  name: "Hedy Lamarr",
  imageUrl: "https://i.imgur.com/yXOvdOSs.jpg",
  imageSize: 90
};

export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
      <img
        className="avatar"
        src={user.imageUrl}
        alt={"Photo of " + user.name}
        style={{
          width: user.imageSize,
          height: user.imageSize
        }}
      />
    </>
  );
}
```

En el ejemplo anterior, `style={{}}` no es una sintaxis especial, sino un objeto `{}` regular dentro de las llaves curvas `style={ }` de JSX. Puede usar el atributo `style` cuando sus estilos dependen de variables de JavaScript.
