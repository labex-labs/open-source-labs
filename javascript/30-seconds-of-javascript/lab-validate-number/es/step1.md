# Función de validación de números

Para validar si una entrada dada es un número, siga estos pasos:

- Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
- Utilice `parseFloat()` para intentar convertir la entrada en un número.
- Utilice `Number.isNaN()` y el operador de negación lógica (`!`) para comprobar si la entrada es un número.
- Utilice `Number.isFinite()` para comprobar si la entrada es finita.
- Utilice `Number` y el operador de igualdad débil (`==`) para comprobar si la coerción es válida.

Aquí está el código para la función `validateNumber`:

```js
const validateNumber = (input) => {
  const num = parseFloat(input);
  return !Number.isNaN(num) && Number.isFinite(num) && Number(input) == input;
};
```

Puede utilizar la función `validateNumber` de la siguiente manera:

```js
validateNumber("10"); // true
validateNumber("a"); // false
```
