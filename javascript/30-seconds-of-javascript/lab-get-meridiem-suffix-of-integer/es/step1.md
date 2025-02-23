# Cómo obtener el sufijo meridiano de un número entero

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`.

Aquí hay una función que convierte un número entero en una cadena con un sufijo meridiano en un formato de 12 horas.

Para hacer esto, utiliza el operador módulo (`%`) y comprobaciones condicionales.

```js
const getMeridiemSuffixOfInteger = (num) => {
  if (num === 0 || num === 24) {
    return "12am";
  } else if (num === 12) {
    return "12pm";
  } else if (num < 12) {
    return num + "am";
  } else {
    return (num % 12) + "pm";
  }
};
```

Aquí hay algunos ejemplos de cómo utilizar esta función:

```js
getMeridiemSuffixOfInteger(0); // '12am'
getMeridiemSuffixOfInteger(11); // '11am'
getMeridiemSuffixOfInteger(13); // '1pm'
getMeridiemSuffixOfInteger(25); // '1pm'
```

Esta función toma un número entero como argumento y devuelve una cadena con el sufijo meridiano.
