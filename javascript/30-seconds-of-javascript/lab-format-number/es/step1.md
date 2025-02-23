# Función de formato de números

Para formatear un número utilizando el orden de formato numérico local, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `Number.prototype.toLocaleString()` para convertir un número a utilizar los separadores de formato numérico local.
3. Pase el número que desea formatear como argumento a la función.

A continuación, se muestra una implementación de ejemplo:

```js
const formatNumber = (num) => num.toLocaleString();
```

Y aquí hay algunos ejemplos de cómo utilizar la función:

```js
formatNumber(123456); // '123,456' en `en-US`
formatNumber(15675436903); // '15.675.436.903' en `de-DE`
```
