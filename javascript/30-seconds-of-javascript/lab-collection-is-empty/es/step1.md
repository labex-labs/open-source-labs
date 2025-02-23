# Comprobando si una colección está vacía

Para comprobar si una colección está vacía, puedes abrir la Terminal/SSH y escribir `node`. Este programa comprueba si un valor es un objeto/colección vacío, no tiene propiedades enumerables o es cualquier tipo que no se considere una colección.

Para usar el programa, comprueba si el valor proporcionado es `null` o si su `length` es igual a `0`. Aquí hay un ejemplo de código:

```js
const isEmpty = (val) => val == null || !(Object.keys(val) || val).length;
```

Luego puedes probar el programa usando los siguientes códigos:

```js
isEmpty([]); // true
isEmpty({}); // true
isEmpty(""); // true
isEmpty([1, 2]); // false
isEmpty({ a: 1, b: 2 }); // false
isEmpty("text"); // false
isEmpty(123); // true - el tipo no se considera una colección
isEmpty(true); // true - el tipo no se considera una colección
```
