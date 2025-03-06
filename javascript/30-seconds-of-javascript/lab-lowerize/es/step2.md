# Accediendo a las claves de un objeto

Antes de poder transformar las claves de un objeto, necesitamos entender cómo acceder a ellas. JavaScript proporciona el método `Object.keys()`, que devuelve un array que contiene todas las claves de un objeto.

En la shell interactiva de Node.js, intenta lo siguiente:

```javascript
Object.keys(user);
```

Deberías ver una salida como esta:

```
[ 'Name', 'AGE', 'Email' ]
```

Ahora, intentemos convertir cada clave a minúsculas utilizando el método `toLowerCase()`. Podemos usar el método `map()` para transformar cada clave:

```javascript
Object.keys(user).map((key) => key.toLowerCase());
```

La salida debería ser:

```
[ 'name', 'age', 'email' ]
```

¡Genial! Ahora tenemos un array con todas las claves convertidas a minúsculas. Sin embargo, todavía necesitamos crear un nuevo objeto con estas claves en minúsculas y los valores originales. Para esto, usaremos el método `reduce()` en el siguiente paso.

Entendamos el método `reduce()` antes de continuar. Este método ejecuta una función reductora en cada elemento del array, resultando en un solo valor de salida.

Aquí hay un ejemplo sencillo de `reduce()`:

```javascript
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((accumulator, currentValue) => {
  return accumulator + currentValue;
}, 0);

sum;
```

La salida será `10`, que es la suma de todos los números en el array. El `0` en el método `reduce()` es el valor inicial del acumulador.
