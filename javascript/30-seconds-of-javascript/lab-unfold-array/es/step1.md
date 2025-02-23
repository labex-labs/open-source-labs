# Desplegar un array

Para crear un array utilizando una función iteradora y un valor semilla inicial, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice un bucle `while` y `Array.prototype.push()` para llamar a la función iteradora repetidamente hasta que devuelva `false`.
3. La función iteradora debe aceptar un argumento (`seed`) y siempre devolver un array con dos elementos ([`value`, `nextSeed`]) o `false` para terminar.

Utilice el siguiente código para implementar la función `unfold`:

```js
const unfold = (fn, seed) => {
  let result = [],
    val = [null, seed];
  while ((val = fn(val[1]))) result.push(val[0]);
  return result;
};
```

Este es un ejemplo de cómo utilizar la función `unfold`:

```js
var f = (n) => (n > 50 ? false : [-n, n + 10]);
unfold(f, 10); // [-10, -20, -30, -40, -50]
```

Esto producirá un array con los valores generados por la función iteradora `f` a partir del valor semilla inicial de `10`. La función iteradora genera un array con dos elementos en cada paso: la negación del valor semilla actual y el siguiente valor semilla, que se incrementa en 10. El proceso continúa hasta que el valor semilla es mayor que 50, momento en el que la función devuelve `false`.
