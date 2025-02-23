# Función para Formatear Segundos en Formato de Tiempo ISO

Para usar este código, abre la Terminal/SSH y escribe `node`. Esta función toma un número de segundos como argumento y devuelve el formato de tiempo ISO. Aquí está cómo funciona:

- Divide el número de segundos por los valores adecuados para obtener los valores correspondientes de `hora`, `minuto` y `segundo`.
- Guarda el signo del número en una variable para agregarlo al principio del resultado.
- Usa `Array.prototype.map()` en combinación con `Math.floor()` y `String.prototype.padStart()` para convertir a cadena y formatear cada segmento.
- Usa `Array.prototype.join()` para combinar los valores en una cadena.

Aquí está el código:

```js
const formatSeconds = (s) => {
  const [hour, minute, second, sign] =
    s > 0
      ? [s / 3600, (s / 60) % 60, s % 60, ""]
      : [-s / 3600, (-s / 60) % 60, -s % 60, "-"];

  return (
    sign +
    [hour, minute, second]
      .map((v) => `${Math.floor(v)}`.padStart(2, "0"))
      .join(":")
  );
};
```

Puedes probar la función con estos ejemplos:

```js
formatSeconds(200); // '00:03:20'
formatSeconds(-200); // '-00:03:20'
formatSeconds(99999); // '27:46:39'
```
