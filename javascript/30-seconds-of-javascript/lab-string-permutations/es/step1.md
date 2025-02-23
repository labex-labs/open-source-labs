# Algoritmo de permutaciones de cadenas

Para generar todas las permutaciones de una cadena que contiene duplicados, utiliza el siguiente algoritmo:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza la recursión para crear todas las permutaciones posibles de la cadena dada.
3. Para cada letra en la cadena dada, crea todas las permutaciones parciales para el resto de sus letras.
4. Utiliza `Array.prototype.map()` para combinar la letra con cada permutación parcial.
5. Utiliza `Array.prototype.reduce()` para combinar todas las permutaciones en una matriz.
6. Los casos base son para `String.prototype.length` igual a `2` o `1`.
7. ⚠️ **ADVERTENCIA**: El tiempo de ejecución aumenta exponencialmente con cada carácter. Para cadenas con más de 8 a 10 caracteres, el entorno puede colgar mientras intenta resolver todas las combinaciones diferentes.

Aquí está el código JavaScript para el algoritmo:

```js
const stringPermutations = (str) => {
  if (str.length <= 2) return str.length === 2 ? [str, str[1] + str[0]] : [str];
  return str
    .split("")
    .reduce(
      (acc, letter, i) =>
        acc.concat(
          stringPermutations(str.slice(0, i) + str.slice(i + 1)).map(
            (val) => letter + val
          )
        ),
      []
    );
};
```

Puedes probar la función `stringPermutations` con el siguiente código:

```js
stringPermutations("abc"); // ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```
