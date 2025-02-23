# Cómo hashear una cadena en un número utilizando JavaScript

Para hashear una cadena de entrada en un número entero utilizando JavaScript, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza los métodos `String.prototype.split()` y `Array.prototype.reduce()` para crear un hash de la cadena de entrada, utilizando desplazamiento de bits.
3. Aquí está el código de la función `sdbm` que implementa el algoritmo de hash:

```js
const sdbm = (str) => {
  let arr = str.split("");
  return arr.reduce(
    (hashCode, currentVal) =>
      (hashCode =
        currentVal.charCodeAt(0) +
        (hashCode << 6) +
        (hashCode << 16) -
        hashCode),
    0
  );
};
```

4. Para probar la función, llámala con un argumento de cadena:

```js
sdbm("name"); // -3521204949
```

Esto devolverá el valor hash para la cadena de entrada "name".
