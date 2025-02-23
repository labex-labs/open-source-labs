# Generar un código de color hexadecimal aleatorio en Terminal/SSH

Para generar un código de color hexadecimal aleatorio en Terminal/SSH, siga los pasos siguientes:

1. Abra la Terminal/SSH.
2. Escriba `node`.
3. Utilice el siguiente código para generar un número hexadecimal aleatorio de 24 bits (6 \* 4 bits):

```js
const randomHexColorCode = () => {
  let n = (Math.random() * 0xfffff * 1000000).toString(16);
  return "#" + n.slice(0, 6);
};
```

4. Para generar un código de color hexadecimal aleatorio, llame a la función `randomHexColorCode()`.

Ejemplo:

```js
randomHexColorCode(); // '#e34155'
```

Esto generará un código de color hexadecimal aleatorio que puede utilizar en sus proyectos de codificación.
