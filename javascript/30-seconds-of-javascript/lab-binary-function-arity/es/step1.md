# Función que acepta hasta dos argumentos

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`.

La función `binary` se crea con la capacidad de aceptar hasta dos argumentos mientras ignora cualquier argumento adicional.

La función `fn` proporcionada se llama con los primeros dos argumentos dados.

Aquí está el código:

```js
const binary = (fn) => (a, b) => fn(a, b);
```

Y aquí está un ejemplo de uso:

```js
["2", "1", "0"].map(binary(Math.max)); // [2, 1, 2]
```
