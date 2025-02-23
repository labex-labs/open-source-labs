# Función para agregar días a una fecha

Aquí hay una función que puede calcular la fecha de `n` días a partir de la fecha dada y devolver su representación en cadena.

Para usar la función, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el constructor `Date` para crear un objeto `Date` a partir del primer argumento.
3. Utilice `Date.prototype.getDate()` y `Date.prototype.setDate()` para agregar `n` días a la fecha dada.
4. Utilice `Date.prototype.toISOString()` para devolver una cadena en el formato `yyyy-mm-dd`.

Aquí está el código de la función:

```js
const addDaysToDate = (date, n) => {
  const d = new Date(date);
  d.setDate(d.getDate() + n);
  return d.toISOString().split("T")[0];
};
```

Puede probar la función con los siguientes ejemplos:

```js
addDaysToDate("2020-10-15", 10); // '2020-10-25'
addDaysToDate("2020-10-15", -10); // '2020-10-05'
```
