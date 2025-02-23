# Formato de duración

Para obtener el formato legible para humanos de un número dado de milisegundos, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Divida los `ms` con los valores adecuados para obtener los valores adecuados de `día`, `hora`, `minuto`, `segundo` y `milisegundo`.
3. Utilice `Object.entries()` con `Array.prototype.filter()` para conservar solo los valores no nulos.
4. Cree la cadena para cada valor, pluralizando adecuadamente, utilizando `Array.prototype.map()`.
5. Combine los valores en una cadena utilizando `Array.prototype.join()`.

Aquí está el código:

```js
const formatDuration = (ms) => {
  if (ms < 0) ms = -ms;
  const time = {
    day: Math.floor(ms / 86400000),
    hour: Math.floor(ms / 3600000) % 24,
    minute: Math.floor(ms / 60000) % 60,
    second: Math.floor(ms / 1000) % 60,
    millisecond: Math.floor(ms) % 1000
  };
  return Object.entries(time)
    .filter((val) => val[1] !== 0)
    .map(([key, val]) => `${val} ${key}${val !== 1 ? "s" : ""}`)
    .join(", ");
};
```

Aquí hay algunos ejemplos:

```js
formatDuration(1001); // '1 segundo, 1 milisegundo'
formatDuration(34325055574);
// '397 días, 6 horas, 44 minutos, 15 segundos, 574 milisegundos'
```
