# Comprobando si el entorno es Travis CI

Para comprobar si estás ejecutando en Travis CI, utiliza la función `isTravisCI()`. Esta función comprueba si las variables de entorno `TRAVIS` y `CI` están presentes.

```js
const isTravisCI = () => "TRAVIS" in process.env && "CI" in process.env;
```

Para comenzar a codificar en Travis CI, abre la Terminal/SSH y escribe `node`.
