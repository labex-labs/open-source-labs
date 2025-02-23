# Comprueba si dos URLs pertenecen al mismo origen

Para comprobar si dos URLs pertenecen al mismo origen:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.

2. Utiliza `URL.protocol` y `URL.host` para comprobar si ambas URLs tienen el mismo protocolo y host.

```js
const isSameOrigin = (origin, destination) =>
  origin.protocol === destination.protocol && origin.host === destination.host;
```

3. Crea dos objetos URL con las URLs que quieres comparar.

```js
const origin = new URL("https://www.30secondsofcode.org/about");
const destination = new URL("https://www.30secondsofcode.org/contact");
```

4. Llama a la función `isSameOrigin` con los dos objetos URL como argumentos para obtener una salida booleana.

```js
isSameOrigin(origin, destination); // true
```

5. También puedes probar la función con otras URLs para ver si pertenecen al mismo origen o no.

```js
const other = new URL("https://developer.mozilla.org");
isSameOrigin(origin, other); // false
```
