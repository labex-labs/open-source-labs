# Algoritmo de clasificación heapsort

Para practicar la codificación, abre la Terminal/SSH y escribe 'node'. El siguiente algoritmo clasifica una matriz de números utilizando el algoritmo de clasificación heapsort. Sigue estos pasos:

- Utiliza recursividad en la función.
- Utiliza el operador de propagación `(...)` para clonar la matriz original, `arr`.
- Utiliza closures para declarar una variable, `l`, y una función `heapify`.
- Utiliza un bucle `for` y `Math.floor()` en combinación con `heapify` para crear un montón máximo a partir de la matriz.
- Utiliza un bucle `for` para reducir repetidamente el rango considerado, utilizando `heapify` y cambiando valores según sea necesario para ordenar la matriz clonada.

```js
const heapsort = (arr) => {
  const a = [...arr];
  let l = a.length;
  const heapify = (a, i) => {
    const left = 2 * i + 1;
    const right = 2 * i + 2;
    let max = i;
    if (left < l && a[left] > a[max]) max = left;
    if (right < l && a[right] > a[max]) max = right;
    if (max !== i) {
      [a[max], a[i]] = [a[i], a[max]];
      heapify(a, max);
    }
  };
  for (let i = Math.floor(l / 2); i >= 0; i -= 1) heapify(a, i);
  for (let i = a.length - 1; i > 0; i--) {
    [a[0], a[i]] = [a[i], a[0]];
    l--;
    heapify(a, 0);
  }
  return a;
};
```

Por ejemplo:

```js
heapsort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
