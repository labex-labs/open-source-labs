# Algoritmo de Ordenamiento Burbuja

Para practicar la codificación, abre la Terminal/SSH y escribe `node` para comenzar. El algoritmo de ordenamiento burbuja ordena un array de números.

Pasos para ordenar un array utilizando el algoritmo de ordenamiento burbuja:

1. Declara una variable, `swapped`, que indique si se intercambiaron valores durante la iteración actual.

2. Utiliza el operador de propagación (`...`) para clonar el array original, `arr`.

3. Utiliza un bucle `for` para iterar sobre los elementos del array clonado, terminando antes del último elemento.

4. Utiliza un bucle `for` anidado para iterar sobre el segmento del array entre `0` e `i`, intercambiando cualquier elemento adyacente desordenado y estableciendo `swapped` en `true`.

5. Si `swapped` es `false` después de una iteración, ya no se necesitan más cambios, por lo que se devuelve el array clonado.

Código de ejemplo:

```js
const bubbleSort = (arr) => {
  let swapped = false;
  const a = [...arr];
  for (let i = 1; i < a.length; i++) {
    swapped = false;
    for (let j = 0; j < a.length - i; j++) {
      if (a[j + 1] < a[j]) {
        [a[j], a[j + 1]] = [a[j + 1], a[j]];
        swapped = true;
      }
    }
    if (!swapped) return a;
  }
  return a;
};

bubbleSort([2, 1, 4, 3]); // [1, 2, 3, 4]
```
