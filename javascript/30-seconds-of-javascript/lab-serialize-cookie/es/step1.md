# Cómo serializar una cookie

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`. Luego, sigue estos pasos para serializar un par nombre-valor de cookie en una cadena de encabezado Set-Cookie:

1. Utiliza literales de plantilla y `encodeURIComponent()` para crear la cadena adecuada.
2. Implementa la función `serializeCookie` pasando los parámetros `name` y `val`.
3. La función devolverá una cadena que esté adecuadamente serializada.

A continuación, se muestra un ejemplo de cómo utilizar la función `serializeCookie`:

```js
const serializeCookie = (name, val) =>
  `${encodeURIComponent(name)}=${encodeURIComponent(val)}`;

serializeCookie("foo", "bar"); // 'foo=bar'
```

En este ejemplo, la función `serializeCookie` toma `foo` como el nombre de la cookie y `bar` como el valor de la cookie, y devuelve una cadena de cookie serializada de `foo=bar`.
