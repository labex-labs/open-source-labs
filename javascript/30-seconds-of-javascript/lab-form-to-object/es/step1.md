# Convertir un formulario en un objeto

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. Puedes codificar un conjunto de elementos de formulario como un objeto siguiendo los siguientes pasos:

1. Utiliza el constructor `FormData` para convertir el `formulario` HTML en `FormData`.
2. Convierte el `FormData` en una matriz utilizando `Array.from()`.
3. Recopila el objeto de la matriz utilizando `Array.prototype.reduce()`.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const formToObject = (form) =>
  Array.from(new FormData(form)).reduce(
    (acc, [key, value]) => ({
      ...acc,
      [key]: value
    }),
    {}
  );
```

Para convertir un formulario específico, puedes llamar a la función `formToObject` y pasar el elemento del formulario como argumento:

```js
formToObject(document.querySelector("#form"));
// { email: 'test@email.com', name: 'Test Name' }
```
