# Mapear recursivamente las propiedades de un objeto

Para mapear recursivamente las propiedades de un objeto, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice la función `deepMapKeys` con el objeto proporcionado y una función que genere nuevas propiedades.
3. La función crea un objeto con los mismos valores que el objeto proporcionado y propiedades generadas al ejecutar la función proporcionada para cada propiedad.
4. Itere sobre las propiedades del objeto utilizando `Object.keys()`.
5. Cree un nuevo objeto con los mismos valores y propiedades mapeadas utilizando `Array.prototype.reduce()` y la función proporcionada.
6. Si un valor es un objeto, llame recursivamente a `deepMapKeys` en él para mapear también sus propiedades.

```js
const deepMapKeys = (obj, fn) =>
  Array.isArray(obj)
    ? obj.map((val) => deepMapKeys(val, fn))
    : typeof obj === "object"
      ? Object.keys(obj).reduce((acc, current) => {
          const key = fn(current);
          const val = obj[current];
          acc[key] =
            val !== null && typeof val === "object"
              ? deepMapKeys(val, fn)
              : val;
          return acc;
        }, {})
      : obj;
```

A continuación, se muestra un ejemplo de uso de `deepMapKeys`:

```js
const obj = {
  foo: "1",
  nested: {
    child: {
      withArray: [
        {
          grandChild: ["hello"]
        }
      ]
    }
  }
};

const upperKeysObj = deepMapKeys(obj, (key) => key.toUpperCase());
/*
{
  "FOO":"1",
  "NESTED":{
    "CHILD":{
      "WITHARRAY":[
        {
          "GRANDCHILD":[ 'hello' ]
        }
      ]
    }
  }
}
*/
```
