# Renderizado Condicional

> El proyecto de React ya se ha proporcionado en la máquina virtual. En general, solo necesitas agregar código a `App.js`.

Por favor, utiliza el siguiente comando para instalar las dependencias:

```bash
npm i
```

En React, no hay una sintaxis especial para escribir condiciones. En cambio, usarás las mismas técnicas que utilizas al escribir código JavaScript regular. Por ejemplo, puedes usar una declaración `if` para incluir JSX de manera condicional:

```js
if (isPacked) {
  return <li className="item">{name} ✔</li>;
}
return <li className="item">{name}</li>;
```

Si prefieres un código más compacto, puedes usar el operador condicional `?`. A diferencia de `if`, funciona dentro de JSX:

```js
return <li className="item">{isPacked ? name + " ✔" : name}</li>;
```

Cuando no necesitas la rama `else`, también puedes usar una sintaxis lógica `&&` más corta:

```js
return <li className="item">{isPacked && name + " ✔"}</li>;
```

Si la propiedad `isPacked` es `true`, este código devuelve un árbol de JSX diferente. Con este cambio, algunos de los elementos obtienen una marca de verificación al final:

```js
// App.js
function Item({ name, isPacked }) {
  if (isPacked) {
    return <li className="item">{name} ✔</li>;
  }
  return <li className="item">{name}</li>;
}

export default function PackingList() {
  return (
    <section>
      <h1>Lista de equipaje de Sally Ride</h1>
      <ul>
        <Item isPacked={true} name="Traje espacial" />
        <Item isPacked={true} name="Casco con una hoja de oro" />
        <Item isPacked={false} name="Foto de Tam" />
      </ul>
    </section>
  );
}
```

Para ejecutar el proyecto, utiliza el siguiente comando. Luego, puedes actualizar la pestaña **Web 8080** para previsualizar la página web.

```bash
npm start
```
