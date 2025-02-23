# Verificador de Propiedades

Para comprobar si una propiedad específica de un objeto cumple una determinada condición, utiliza la función `checkProp`. Esta función crea una función curried que toma una función predicado y un nombre de propiedad como argumentos. La función devuelta luego toma un objeto y devuelve `true` o `false` según si la propiedad especificada cumple la condición especificada por la función predicado.

A continuación, se muestra una implementación de ejemplo de `checkProp`:

```js
const checkProp = (predicate, prop) => (obj) => !!predicate(obj[prop]);
```

Y aquí hay algunos ejemplos de cómo podrías utilizarla:

```js
const lengthIs4 = checkProp((l) => l === 4, "length");
lengthIs4([]); // false
lengthIs4([1, 2, 3, 4]); // true
lengthIs4(new Set([1, 2, 3, 4])); // false (Set utiliza Size, no length)

const session = { user: {} };
const validUserSession = checkProp((u) => u.active && !u.disabled, "user");

validUserSession(session); // false

session.user.active = true;
validUserSession(session); // true

const noLength = checkProp((l) => l === undefined, "length");
noLength([]); // false
noLength({}); // true
noLength(new Set()); // true
```

En resumen, la función `checkProp` te permite comprobar fácilmente el valor de una propiedad específica en un objeto al especificar una función predicado para esa propiedad.
