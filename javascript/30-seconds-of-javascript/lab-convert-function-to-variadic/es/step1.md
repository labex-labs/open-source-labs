# Convertir una función en una función variádica

Para convertir una función que acepta un arreglo en una función variádica, puedes seguir estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.

2. Devuelva una clausura que recopile todas las entradas en una función que acepta arreglos.

```js
const collectInto =
  (fn) =>
  (...args) =>
    fn(args);
```

3. Utilice la función `collectInto` para convertir una función en una función variádica.

```js
const Pall = collectInto(Promise.all.bind(Promise));
let p1 = Promise.resolve(1);
let p2 = Promise.resolve(2);
let p3 = new Promise((resolve) => setTimeout(resolve, 2000, 3));
Pall(p1, p2, p3).then(console.log); // [1, 2, 3] (después de aproximadamente 2 segundos)
```

Esto le permitirá aceptar cualquier número de argumentos en su función y recopilarlos en un arreglo para su posterior procesamiento.
