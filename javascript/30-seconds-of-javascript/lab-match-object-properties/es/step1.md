# Cómo comparar propiedades de objetos en JavaScript

Para comparar dos objetos y comprobar si tienen los mismos valores de propiedad, utiliza la función `matches`. Aquí está cómo se utiliza:

1. Abre la Terminal/SSH y escribe `node` para comenzar a codificar.
2. Copia y pega el código de la función `matches` en tu archivo JavaScript.
3. Llama a la función y pasa dos objetos como argumentos. El primer objeto es el que quieres comparar, y el segundo objeto es el que quieres compararlo con.

```js
matches({ age: 25, hair: "long", beard: true }, { hair: "long", beard: true });
// true
matches({ hair: "long", beard: true }, { age: 25, hair: "long", beard: true });
// false
```

La función `matches` utiliza `Object.keys()` para obtener todas las claves del segundo objeto y luego comprueba si todas las claves existen en el primer objeto y tienen los mismos valores utilizando `Array.prototype.every()`, `Object.prototype.hasOwnProperty()` y una comparación estricta.
