# Cómo extraer valores de un array basado en una función dada

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

La función `pullBy` muta el array original filtrando los valores especificados basados en una función iteradora dada. Aquí cómo funciona:

1. Verifica si el último argumento proporcionado es una función.
2. Usa `Array.prototype.map()` para aplicar la función iteradora `fn` a todos los elementos del array.
3. Usa `Array.prototype.filter()` y `Array.prototype.includes()` para extraer los valores que no se necesitan.
4. Establece `Array.prototype.length` para restablecer la longitud del array pasado a `0`.
5. Usa `Array.prototype.push()` para volver a poblarlo solo con los valores extraídos.

Aquí está el código:

```js
const pullBy = (arr, ...args) => {
  const length = args.length;
  let fn = length > 1 ? args[length - 1] : undefined;
  fn = typeof fn == "function" ? (args.pop(), fn) : undefined;
  let argState = (Array.isArray(args[0]) ? args[0] : args).map((val) =>
    fn(val)
  );
  let pulled = arr.filter((v, i) => !argState.includes(fn(v)));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
};
```

Y aquí está un ejemplo de cómo usarlo:

```js
var myArray = [{ x: 1 }, { x: 2 }, { x: 3 }, { x: 1 }];
pullBy(myArray, [{ x: 1 }, { x: 3 }], (o) => o.x); // myArray = [{ x: 2 }]
```

Tenga en cuenta que en este ejemplo, estamos extrayendo todos los elementos con una propiedad `x` de `1` o `3`. El `myArray` resultante solo contendrá el elemento con una propiedad `x` de `2`.
