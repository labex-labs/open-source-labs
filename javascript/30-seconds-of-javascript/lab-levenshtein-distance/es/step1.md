# Algoritmo de Distancia de Levenshtein

Para calcular la diferencia entre dos cadenas, puedes utilizar el algoritmo de distancia de Levenshtein. Aquí te muestra cómo hacerlo:

1. Si cualquiera de las cadenas tiene una `longitud` de cero, devuelve la `longitud` de la otra.
2. Utiliza un bucle `for` anidado para iterar sobre las letras de las cadenas objetivo y fuente.
3. Calcula el costo de sustituir las letras correspondientes a `i - 1` y `j - 1` en la cadena objetivo y fuente respectivamente (`0` si son iguales, `1` en caso contrario).
4. Utiliza `Math.min()` para poblar cada elemento en la matriz bidimensional con el mínimo de la celda arriba incrementada en uno, la celda a la izquierda incrementada en uno o la celda en la esquina superior izquierda incrementada por el costo previamente calculado.
5. Devuelve el último elemento de la última fila de la matriz producida.

Para comenzar a practicar este código, abre la Terminal/SSH y escribe `node`. Aquí te muestra el código que puedes utilizar:

```js
const levenshteinDistance = (s, t) => {
  if (!s.length) return t.length;
  if (!t.length) return s.length;
  const arr = [];
  for (let i = 0; i <= t.length; i++) {
    arr[i] = [i];
    for (let j = 1; j <= s.length; j++) {
      arr[i][j] =
        i === 0
          ? j
          : Math.min(
              arr[i - 1][j] + 1,
              arr[i][j - 1] + 1,
              arr[i - 1][j - 1] + (s[j - 1] === t[i - 1] ? 0 : 1)
            );
    }
  }
  return arr[t.length][s.length];
};

console.log(levenshteinDistance("duck", "dark")); // 2
```
