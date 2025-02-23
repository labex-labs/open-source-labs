# Truncar una cadena en JavaScript

Para truncar una cadena en JavaScript, puedes usar la función `truncateString`. Esta función toma dos argumentos: `str` (la cadena que se va a truncar) y `num` (la longitud máxima de la cadena truncada).

La función `truncateString` verifica si la longitud de `str` es mayor que `num`. Si es así, la función trunca la cadena a la longitud deseada y agrega `'...'` al final. Si no, devuelve la cadena original.

Aquí está el código de la función `truncateString`:

```js
const truncateString = (str, num) =>
  str.length > num ? str.slice(0, num > 3 ? num - 3 : num) + "..." : str;
```

Y aquí está un ejemplo de cómo usar la función `truncateString`:

```js
truncateString("boomerang", 7); // 'boom...'
```
