# Cómo comprobar la igualdad de objetos en JavaScript

Para comprobar si dos valores son equivalentes, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Realice una comparación profunda entre los dos valores utilizando la función `equals()`.
3. Compruebe si los dos valores son idénticos. Si es así, devuelva `true`.
4. Compruebe si ambos valores son objetos `Date` con la misma hora, utilizando `Date.prototype.getTime()`. Si es así, devuelva `true`.
5. Compruebe si ambos valores son valores no objeto con un valor equivalente (comparación estricta). Si es así, devuelva `true`.
6. Compruebe si solo un valor es `null` o `undefined` o si sus prototipos son diferentes. Si es así, devuelva `false`.
7. Si ninguna de las condiciones anteriores se cumple, utilice `Object.keys()` para comprobar si ambos valores tienen el mismo número de claves.
8. Utilice `Array.prototype.every()` para comprobar si cada clave en `a` existe en `b` y si son equivalentes llamando recursivamente a `equals()`.

Utilice el siguiente código para implementar la función `equals()`:

```js
const equals = (a, b) => {
  if (a === b) return true;

  if (a instanceof Date && b instanceof Date)
    return a.getTime() === b.getTime();

  if (!a || !b || (typeof a !== "object" && typeof b !== "object"))
    return a === b;

  if (a.prototype !== b.prototype) return false;

  const keys = Object.keys(a);
  if (keys.length !== Object.keys(b).length) return false;

  return keys.every((k) => equals(a[k], b[k]));
};
```

Utilice los siguientes ejemplos de código para probar la función `equals()`:

```js
equals(
  { a: [2, { e: 3 }], b: [4], c: "foo" },
  { a: [2, { e: 3 }], b: [4], c: "foo" }
); // true

equals([1, 2, 3], { 0: 1, 1: 2, 2: 3 }); // true
```
