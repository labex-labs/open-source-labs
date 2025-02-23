# Pluralizar una Cadena

Para pluralizar una palabra basada en un número dado, utiliza la función `pluralize`. Comienza abriendo la Terminal/SSH y escribiendo `node`. Esta función puede devolver la forma singular o plural de la palabra, dependiendo del número de entrada. También puedes suministrar un diccionario opcional para utilizar formas plurales personalizadas.

Para definir la función `pluralize`, utiliza una clausura que tome la `palabra` y una forma `plural` opcional. Si la entrada `num` es `-1` o `1`, devuelve la forma singular de la `palabra`. De lo contrario, devuelve la forma `plural`. Si no se suministra una forma `plural` personalizada, la función utilizará el valor predeterminado de la forma singular de la `palabra` + `s`.

Si el primer argumento es un objeto, la función `pluralize` devuelve una nueva función que puede utilizar el diccionario suministrado para resolver la forma plural correcta de la `palabra`.

Aquí está la función `pluralize` en acción:

```js
const pluralize = (val, word, plural = word + "s") => {
  const _pluralize = (num, word, plural = word + "s") =>
    [1, -1].includes(Number(num)) ? word : plural;
  if (typeof val === "object")
    return (num, word) => _pluralize(num, word, val[word]);
  return _pluralize(val, word, plural);
};
```

Puedes utilizar la función `pluralize` de la siguiente manera:

```js
pluralize(0, "apple"); // 'apples'
pluralize(1, "apple"); // 'apple'
pluralize(2, "apple"); // 'apples'
pluralize(2, "person", "people"); // 'people'
```

Si tienes un diccionario de formas plurales personalizadas, puedes crear una función `autoPluralize` que automáticamente utilice la forma plural correcta para una `palabra` dada:

```js
const PLURALS = {
  person: "people",
  radius: "radii"
};
const autoPluralize = pluralize(PLURALS);
autoPluralize(2, "person"); // 'people'
```
