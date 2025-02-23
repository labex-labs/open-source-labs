# Comprobar si una fecha es un fin de semana

Para comprobar si una fecha determinada es un fin de semana, siga estos pasos:

- Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
- Utilice el método `Date.prototype.getDay()` para obtener el día de la semana como un número (0-6), siendo el domingo 0 y el sábado 6.
- Compruebe si el día es un fin de semana utilizando un operador módulo (`%`) y comparándolo con 0 o 6.
- Omita el argumento `d` para utilizar la fecha actual como predeterminada.

A continuación, se muestra un fragmento de código de ejemplo que puede utilizar:

```js
const isWeekend = (d = new Date()) => d.getDay() % 6 === 0;
```

Para probar la función, simplemente llámela sin ningún argumento:

```js
isWeekend(); // true o false (según la fecha actual)
```

Esto devolverá `true` si la fecha actual es un fin de semana (sábado o domingo) y `false` en caso contrario.
