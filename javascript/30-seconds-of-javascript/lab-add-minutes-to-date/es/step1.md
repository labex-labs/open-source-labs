# Función para agregar minutos a una fecha

Para agregar un número específico de minutos a una fecha dada, utiliza la siguiente función:

```js
const addMinutesToDate = (date, n) => {
  // Crea un objeto Date a partir de la fecha dada
  const d = new Date(date);
  // Agrega n minutos al objeto Date
  d.setTime(d.getTime() + n * 60000);
  // Devuelve una representación en cadena de la nueva fecha en el formato yyyy-mm-dd HH:MM:SS
  return d.toISOString().split(".")[0].replace("T", " ");
};
```

Para utilizar esta función, pasa una representación en cadena de la fecha como primer argumento y el número de minutos a agregar (o restar, si es negativo) como segundo argumento. Por ejemplo:

```js
addMinutesToDate("2020-10-19 12:00:00", 10); // '2020-10-19 12:10:00'
addMinutesToDate("2020-10-19", -10); // '2020-10-18 23:50:00'
```

Tenga en cuenta que la función devuelve la nueva fecha como una cadena en el formato `yyyy-mm-dd HH:MM:SS`.
