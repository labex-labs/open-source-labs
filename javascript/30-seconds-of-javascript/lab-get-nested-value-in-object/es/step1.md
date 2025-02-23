# Cómo obtener un valor anidado en un objeto JSON

Para recuperar un valor objetivo de un objeto JSON anidado basado en una clave dada, siga estos pasos:

- Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
- Verifique si el `target` existe en el `obj` utilizando el operador `in`.
- Si se encuentra el `target`, devuelva el valor correspondiente en el `obj`.
- Si no se encuentra el `target`, utilice `Object.values()` y `Array.prototype.reduce()` para llamar recursivamente a la función `dig` en cada objeto anidado hasta que se encuentre el primer par clave/valor coincidente.

A continuación, se muestra el código de la función `dig`:

```js
const dig = (obj, target) =>
  target in obj
    ? obj[target]
    : Object.values(obj).reduce((acc, val) => {
        if (acc !== undefined) return acc;
        if (typeof val === "object") return dig(val, target);
      }, undefined);
```

Para utilizar la función `dig`, primero cree un objeto JSON con niveles anidados, como este:

```js
const data = {
  level1: {
    level2: {
      level3: "algún dato"
    }
  }
};
```

Luego, llame a la función `dig` con el objeto JSON y la clave deseada:

```js
dig(data, "level3"); //'algún dato'
dig(data, "level4"); // undefined
```

Estos ejemplos devolverán el valor de la clave `level3` en el objeto `data` y `undefined` para la clave `level4` inexistente.
