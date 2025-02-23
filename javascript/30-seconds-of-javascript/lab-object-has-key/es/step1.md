# Función de JavaScript para Comprobar si un Objeto Tiene una Clave

Para comprobar si un valor objetivo existe en un objeto de JavaScript, utiliza la función `hasKey`.

La función toma dos argumentos: `obj`, el objeto JSON en el que se realizará la búsqueda, y `keys`, una matriz de claves a comprobar. Estos son los pasos para comprobar si el objeto tiene la clave(s) dada(s):

1. Comprueba si la matriz `keys` no está vacía. Si está vacía, devuelve `false`.
2. Utiliza el método `Array.prototype.every()` para iterar sobre la matriz `keys` y comprobar secuencialmente cada clave hasta la profundidad interna del `obj`.
3. Utiliza el método `Object.prototype.hasOwnProperty()` para comprobar si `obj` no tiene la clave actual o no es un objeto. Si cualquiera de estas condiciones es verdadera, detén la propagación y devuelve `false`.
4. En caso contrario, asigna el valor de la clave a `obj` para usarlo en la siguiente iteración.
5. Si se ha iterado correctamente sobre la matriz `keys`, devuelve `true`.

Aquí está el código de la función `hasKey`:

```js
const hasKey = (obj, keys) => {
  return (
    keys.length > 0 &&
    keys.every((key) => {
      if (typeof obj !== "object" || !obj.hasOwnProperty(key)) return false;
      obj = obj[key];
      return true;
    })
  );
};
```

Aquí hay algunos ejemplos de cómo utilizar la función `hasKey`:

```js
let obj = {
  a: 1,
  b: { c: 4 },
  "b.d": 5
};

hasKey(obj, ["a"]); // true
hasKey(obj, ["b"]); // true
hasKey(obj, ["b", "c"]); // true
hasKey(obj, ["b.d"]); // true
hasKey(obj, ["d"]); // false
hasKey(obj, ["c"]); // false
hasKey(obj, ["b", "f"]); // false
```
