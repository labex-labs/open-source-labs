# Representación (Rendering) de Listas

> El proyecto de React ya se ha proporcionado en la máquina virtual (VM). En general, solo necesitas agregar código a `App.js`.

Por favor, utiliza el siguiente comando para instalar las dependencias:

```bash
npm i
```

Dependerás de características de JavaScript como el bucle `for` y la función `map()` de los arrays para representar (render) listas de componentes.

Por ejemplo, digamos que tienes un array de productos:

```js
const products = [
  { title: "Cabbage", id: 1 },
  { title: "Garlic", id: 2 },
  { title: "Apple", id: 3 }
];
```

Dentro de tu componente, utiliza la función `map()` para transformar un array de productos en un array de elementos `<li>`:

```js
const listItems = products.map((product) => (
  <li key={product.id}>{product.title}</li>
));

return <ul>{listItems}</ul>;
```

Observa cómo `<li>` tiene un atributo `key`. Para cada elemento en una lista, debes pasar una cadena o un número que identifique de forma única ese elemento entre sus hermanos. Por lo general, una `key` debe provenir de tus datos, como un ID de base de datos. React utiliza tus `key` para saber qué ha pasado si más adelante insertas, eliminas o reordenas los elementos.

```js
// App.js
const products = [
  { title: "Cabbage", isFruit: false, id: 1 },
  { title: "Garlic", isFruit: false, id: 2 },
  { title: "Apple", isFruit: true, id: 3 }
];

export default function ShoppingList() {
  const listItems = products.map((product) => (
    <li
      key={product.id}
      style={{
        color: product.isFruit ? "magenta" : "darkgreen"
      }}
    >
      {product.title}
    </li>
  ));

  return <ul>{listItems}</ul>;
}
```

Para ejecutar el proyecto, utiliza el siguiente comando. Luego, puedes actualizar la pestaña **Web 8080** para previsualizar la página web.

```bash
npm start
```
