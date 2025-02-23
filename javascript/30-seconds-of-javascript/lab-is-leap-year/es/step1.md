# Código para Verificar Año Bisiesto

Para verificar si un año `year` dado es bisiesto, sigue estos pasos:

1. Abre la Terminal/SSH.
2. Escribe `node` para comenzar a codificar.
3. Utiliza el constructor `Date` y establece la fecha en 29 de febrero del año dado.
4. Verifica si el mes es igual a `1` utilizando `Date.prototype.getMonth()`.
5. Utiliza el siguiente fragmento de código para verificar si un año es bisiesto:

```js
const isLeapYear = (year) => new Date(year, 1, 29).getMonth() === 1;
```

A continuación, se muestra un ejemplo de cómo utilizar este código:

```js
isLeapYear(2019); // false
isLeapYear(2020); // true
```
