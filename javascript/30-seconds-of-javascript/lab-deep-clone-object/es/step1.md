# Instrucciones para clonar profundamente un objeto

Para clonar profundamente un objeto, siga estos pasos:

1. Cree una nueva instancia de terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice la recursión para clonar primitivos, arrays y objetos, excluyendo las instancias de clase.
3. Verifique si el objeto pasado es `null` y, si es así, devuelva `null`.
4. Utilice `Object.assign()` y un objeto vacío (`{}`) para crear una clonación superficial del original.
5. Utilice `Object.keys()` y `Array.prototype.forEach()` para determinar qué pares clave-valor deben ser clonados profundamente.
6. Si el objeto es un `Array`, establezca la `length` del `clone` en la del original y utilice `Array.from()` para crear un clon.
7. Utilice el siguiente código para implementar la clonación profunda:

```js
const deepClone = (obj) => {
  if (obj === null) return null;
  let clone = Object.assign({}, obj);
  Object.keys(clone).forEach(
    (key) =>
      (clone[key] =
        typeof obj[key] === "object" ? deepClone(obj[key]) : obj[key])
  );
  if (Array.isArray(obj)) {
    clone.length = obj.length;
    return Array.from(clone);
  }
  return clone;
};
```

Utilice el siguiente código para probar su función de clonación profunda:

```js
const a = { foo: "bar", obj: { a: 1, b: 2 } };
const b = deepClone(a); // a!== b, a.obj!== b.obj
```
