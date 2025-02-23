# Cómo crear un clon superficial de un objeto

Para crear un clon superficial de un objeto, utiliza `Object.assign()` y un objeto vacío (`{}`). Sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza el siguiente código para crear un clon superficial del objeto original:

```js
const shallowClone = (obj) => Object.assign({}, obj);
```

3. Para clonar el objeto, utiliza la función `shallowClone()` de la siguiente manera:

```js
const a = { x: true, y: 1 };
const b = shallowClone(a); // a!== b
```

En este ejemplo, `a` y `b` son dos objetos diferentes, pero tienen los mismos valores.
