# Recuperar el nombre del día a partir de un objeto de fecha

Para recuperar el nombre del día de la semana a partir de un objeto `Date`, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Date.prototype.toLocaleDateString()` con la opción `{ weekday: 'long' }` para recuperar el día de la semana.
3. Puede utilizar el segundo argumento opcional para obtener un nombre específico del idioma o omitirlo para utilizar la configuración regional predeterminada.

A continuación, se muestra una implementación de ejemplo:

```js
const dayName = (date, locale) =>
  date.toLocaleDateString(locale, { weekday: "long" });
```

Puede utilizar esta función de la siguiente manera:

```js
dayName(new Date()); // 'Saturday'
dayName(new Date("09/23/2020"), "de-DE"); // 'Samstag'
```
