# Cómo comprobar si una fecha es posterior a otra fecha en JavaScript

Para comprobar si una fecha es posterior a otra fecha en JavaScript, puedes usar el operador mayor que (`>`). Aquí hay un fragmento de código de ejemplo que comprueba si una fecha dada (`dateA`) es posterior a otra fecha (`dateB`):

```js
const isAfterDate = (dateA, dateB) => dateA > dateB;
```

Para usar esta función, simplemente pasa dos objetos de fecha, como esto:

```js
isAfterDate(new Date(2010, 10, 21), new Date(2010, 10, 20)); // true
```

Para probar esto, puedes abrir la Terminal/SSH y escribir `node` para comenzar a practicar la codificación.
