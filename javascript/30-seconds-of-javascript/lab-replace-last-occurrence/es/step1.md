# Función para reemplazar la última aparición de un patrón en una cadena

Aquí hay una función que reemplaza la última aparición de un patrón en una cadena:

```js
const replaceLast = (str, pattern, replacement) => {
```

Para usarla, abra la Terminal/SSH y escriba `node`.

- Primero, use `typeof` para determinar si `pattern` es una cadena o una expresión regular.
- Si `pattern` es una cadena, úsela como `match`.
- De lo contrario, use el constructor `RegExp` para crear una nueva expresión regular usando `RegExp.prototype.source` del `pattern` y agregando la bandera `'g'` a ella. Use `String.prototype.match()` y `Array.prototype.slice()` para obtener la última coincidencia, si la hay.

```js
const match =
  typeof pattern === "string"
    ? pattern
    : (str.match(new RegExp(pattern.source, "g")) || []).slice(-1)[0];
```

- Use `String.prototype.lastIndexOf()` para encontrar la última aparición de la coincidencia en la cadena.
- Si se encuentra una coincidencia, use `String.prototype.slice()` y una plantilla literal para reemplazar la subcadena coincidente con el `replacement` dado.
- Si no se encuentra ninguna coincidencia, devuelva la cadena original.

```js
  if (!match) return str;
  const last = str.lastIndexOf(match);
  return last!== -1
   ? `${str.slice(0, last)}${replacement}${str.slice(last + match.length)}`
    : str;
};
```

Aquí hay algunos ejemplos de cómo usar la función:

```js
replaceLast("abcabdef", "ab", "gg"); // 'abcggdef'
replaceLast("abcabdef", /ab/, "gg"); // 'abcggdef'
replaceLast("abcabdef", "ad", "gg"); // 'abcabdef'
replaceLast("abcabdef", /ad/, "gg"); // 'abcabdef'
```
