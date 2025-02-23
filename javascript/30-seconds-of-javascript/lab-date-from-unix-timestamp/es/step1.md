# Cómo crear un objeto Date a partir de una marca de tiempo Unix

Para crear un objeto `Date` a partir de una marca de tiempo Unix, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Multiplica la marca de tiempo por `1000` para convertirla a milisegundos.
3. Utiliza el constructor `Date` para crear un nuevo objeto `Date`.

Aquí hay un fragmento de código de ejemplo:

```js
const fromTimestamp = (timestamp) => new Date(timestamp * 1000);
```

Puedes utilizar esta función para convertir una marca de tiempo Unix en un objeto `Date` de la siguiente manera:

```js
fromTimestamp(1602162242); // 2020-10-08T13:04:02.000Z
```
