# Creando una Promesa con Retraso

Para crear una nueva promesa que se resuelva después de un tiempo específico, siga estos pasos:

1. Utilice el constructor `Promise` para crear una nueva promesa.
2. Dentro de la función ejecutora de la promesa, utilice `setTimeout()` para llamar a la función `resolve` de la promesa con el `value` proporcionado después del `delay` especificado.

A continuación, se muestra una implementación de ejemplo de `resolveAfter()`:

```js
const resolveAfter = (value, delay) =>
  new Promise((resolve) => {
    setTimeout(() => resolve(value), delay);
  });
```

Ahora puede llamar a `resolveAfter()` para obtener una promesa que se resuelva al valor proporcionado después del retraso especificado:

```js
resolveAfter("Hello", 1000);
// Devuelve una promesa que se resuelve a 'Hello' después de 1s
```

Para comenzar a practicar la codificación, abra la Terminal o SSH y escriba `node`.
