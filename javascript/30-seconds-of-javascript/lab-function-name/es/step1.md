# Cómo obtener el nombre de una función en JavaScript

Para obtener el nombre de una función de JavaScript, siga estos pasos:

1. Abra la Terminal o SSH.
2. Escriba `node` para comenzar a practicar la codificación.
3. Utilice `console.debug()` y la propiedad `name` de la función pasada para registrar el nombre de la función en el canal `debug` de la consola.
4. Devuelva la función `fn` dada.

A continuación, se muestra un fragmento de código de ejemplo que demuestra cómo obtener el nombre de una función en JavaScript:

```js
const functionName = (fn) => (console.debug(fn.name), fn);

let m = functionName(Math.max)(5, 6);
// El nombre de la función'max' se registra en el canal debug de la consola.
// m = 6
```

En este ejemplo, la función `functionName` registra el nombre de la función pasada en el canal `debug` de la consola y devuelve la función misma. La propiedad `name` de la función se utiliza para obtener su nombre.
