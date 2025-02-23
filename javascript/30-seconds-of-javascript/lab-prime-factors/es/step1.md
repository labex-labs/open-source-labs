# Cómo encontrar los factores primos de un número utilizando el algoritmo de división de prueba

Para encontrar los factores primos de un número dado utilizando el algoritmo de división de prueba, siga estos pasos:

- Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
- Utilice un bucle `while` para iterar sobre todos los posibles factores primos, comenzando con `2`.
- Si el factor actual, `f`, divide exactamente a `n`, agregue `f` al array de factores y divida `n` por `f`. De lo contrario, incremente `f` en uno.
- La función `primeFactors` toma un número `n` como entrada y devuelve un array de sus factores primos.
- Para probar la función, llame a `primeFactors(147)` y devolverá `[3, 7, 7]`.

Aquí está el código de JavaScript:

```js
const primeFactors = (n) => {
  let a = [],
    f = 2;
  while (n > 1) {
    if (n % f === 0) {
      a.push(f);
      n /= f;
    } else {
      f++;
    }
  }
  return a;
};
```

Recuerde reemplazar `147` con el número del que desea encontrar los factores primos.
