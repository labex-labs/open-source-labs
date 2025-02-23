# Así es como obtener la hora con minutos y segundos de un objeto de fecha

Si estás buscando practicar la programación, puedes comenzar abriendo la Terminal/SSH y escribiendo `node`.

Esta función devuelve una cadena con el formato `HH:MM:SS` a partir de un objeto `Date` dado.

Para lograr esto, se utilizan los métodos `Date.prototype.toTimeString()` y `String.prototype.slice()` para extraer la parte `HH:MM:SS` del objeto `Date`.

Aquí está el código de la función:

```js
const getColonTimeFromDate = (date) => date.toTimeString().slice(0, 8);
```

Y aquí está un ejemplo de uso:

```js
getColonTimeFromDate(new Date()); // '08:38:00'
```
