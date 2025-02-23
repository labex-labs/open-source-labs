# Cómo comprobar si una fecha es anterior a otra en JavaScript

Para comprobar si una fecha es anterior a otra en JavaScript, puedes usar el operador menor que (`<`). Aquí hay un ejemplo de función que recibe dos fechas y devuelve un valor booleano que indica si la primera fecha es anterior a la segunda:

```js
const isBeforeDate = (dateA, dateB) => dateA < dateB;
```

Puedes usar esta función para comprobar si una fecha específica es anterior a otra fecha pasando dos objetos `Date` como argumentos. Por ejemplo:

```js
isBeforeDate(new Date(2010, 10, 20), new Date(2010, 10, 21)); // true
```
