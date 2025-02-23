# Emparejar Propiedades de Objetos con una Función

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

Esta función compara dos objetos y verifica si el primer objeto contiene valores de propiedad equivalentes al segundo. Lo hace en base a una función proporcionada.

Para usar esta función, sigue estos pasos:

- Utiliza `Object.keys()` para recuperar todas las claves del segundo objeto.
- Utiliza `Array.prototype.every()`, `Object.prototype.hasOwnProperty()` y la función proporcionada para determinar si todas las claves existen en el primer objeto y tienen valores equivalentes.
- Si no se proporciona ninguna función, los valores se compararán utilizando el operador de igualdad.

```js
const matchesWith = (obj, source, fn) =>
  Object.keys(source).every((key) =>
    obj.hasOwnProperty(key) && fn
      ? fn(obj[key], source[key], key, obj, source)
      : obj[key] == source[key]
  );
```

A continuación, se muestra un ejemplo de cómo usar esta función:

```js
const isGreeting = (val) => /^h(?:i|ello)$/.test(val);
matchesWith(
  { greeting: "hello" },
  { greeting: "hi" },
  (oV, sV) => isGreeting(oV) && isGreeting(sV)
); // true
```

Este ejemplo verifica si los dos objetos tienen valores equivalentes para la propiedad `greeting`. Utiliza la función `isGreeting` para asegurarse de que ambos valores son saludos válidos.
