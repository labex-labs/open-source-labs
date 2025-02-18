# Cómo recuperar propiedades de objetos anidados a partir de cadenas de ruta

Para practicar la codificación, abre la Terminal/SSH y escribe `node`.

La siguiente función recupera un conjunto de propiedades de un objeto utilizando selectores especificados en una cadena de ruta. Para lograr esto, sigue estos pasos:

1. Utiliza `Array.prototype.map()` para iterar a través de cada selector y aplica `String.prototype.replace()` para reemplazar los corchetes con puntos.
2. Utiliza `String.prototype.split()` para dividir cada selector en un array de cadenas.
3. Utiliza `Array.prototype.filter()` para eliminar cualquier valor vacío.
4. Utiliza `Array.prototype.reduce()` para recuperar el valor indicado por cada selector.

Aquí está la función:

```js
const get = (from, ...selectors) =>
  [...selectors].map((s) =>
    s
      .replace(/\[([^\[\]]*)\]/g, ".$1.")
      .split(".")
      .filter((t) => t !== "")
      .reduce((prev, cur) => prev && prev[cur], from)
  );
```

Puedes utilizar esta función para recuperar valores de un objeto anidado utilizando una cadena de ruta. Aquí tienes un ejemplo:

```js
const obj = {
  selector: { to: { val: "val to select" } },
  target: [1, 2, { a: "test" }]
};
get(obj, "selector.to.val", "target[0]", "target[2].a");
// ['val to select', 1, 'test']
```
