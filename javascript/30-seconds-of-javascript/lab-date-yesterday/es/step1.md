# Obtener la fecha de ayer en formato aaaa - mm - dd

Para obtener la fecha de ayer en formato `aaaa - mm - dd`, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza el constructor `Date` para obtener la fecha actual.
3. Decrementa la fecha en uno utilizando `Date.prototype.getDate()`.
4. Establece la fecha decrementada utilizando `Date.prototype.setDate()`.
5. Utiliza `Date.prototype.toISOString()` para devolver una cadena en formato `aaaa - mm - dd`.
6. Llama a la función `ayer()` para obtener la fecha de ayer.

```js
const ayer = () => {
  let d = new Date();
  d.setDate(d.getDate() - 1);
  return d.toISOString().split("T")[0];
};

ayer(); // devuelve "2018-10-17" (si la fecha actual es 2018-10-18)
```

Siguiendo estos pasos, podrás recuperar la fecha de ayer de manera clara y concisa.
