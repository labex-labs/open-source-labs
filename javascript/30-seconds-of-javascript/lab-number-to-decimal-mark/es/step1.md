# Cómo convertir un número al formato de separador decimal

Para convertir un número al formato de separador decimal, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Number.prototype.toLocaleString()` para convertir el número al formato de separador decimal.
3. El siguiente código se puede utilizar para este proceso:

```js
const toDecimalMark = (num) => num.toLocaleString("en-US");
```

Aquí hay un ejemplo de cómo utilizar esta función:

```js
toDecimalMark(12305030388.9087); // '12,305,030,388.909'
```

Esto convertirá el número `12305030388.9087` a la cadena con formato de separador decimal `'12,305,030,388.909'`.
