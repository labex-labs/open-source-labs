# Cómo serializar un JSON circular

Para serializar un objeto JSON que contiene referencias circulares, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Cree un `WeakSet` para almacenar y comprobar valores ya vistos utilizando `WeakSet.prototype.add()` y `WeakSet.prototype.has()`.
3. Utilice `JSON.stringify()` con una función reemplazadora personalizada que omita valores ya presentes en `seen` y agregue nuevos valores si es necesario.
4. ⚠️ **AVISO:** Esta función encuentra y elimina referencias circulares, lo que causa la pérdida de datos circulares en el JSON serializado.

Aquí está el código para la función `stringifyCircularJSON`:

```js
const stringifyCircularJSON = (obj) => {
  const seen = new WeakSet();
  return JSON.stringify(obj, (key, value) => {
    if (value !== null && typeof value === "object") {
      if (seen.has(value)) return;
      seen.add(value);
    }
    return value;
  });
};
```

Para probar la función, puede crear un objeto con una referencia circular y llamar a `stringifyCircularJSON`:

```js
const obj = { n: 42 };
obj.obj = obj;
stringifyCircularJSON(obj); // '{"n": 42}'
```
