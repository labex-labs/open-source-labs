# Comprobar si los argumentos del proceso contienen banderas

Para comprobar si los argumentos del proceso actual contienen banderas específicas, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.every()` y `Array.prototype.includes()` para comprobar si `process.argv` contiene todas las banderas especificadas.
3. Utilice una expresión regular para probar si las banderas especificadas están prefijadas con `-` o `--` y prefíjelas en consecuencia.

A continuación, se muestra un fragmento de código que demuestra cómo implementar esto:

```js
const hasFlags = (...flags) =>
  flags.every((flag) =>
    process.argv.includes(/^-{1,2}/.test(flag) ? flag : "--" + flag)
  );
```

Puede probar la función con diferentes banderas de la siguiente manera:

```js
// node myScript.js -s --test --cool=true
hasFlags("-s"); // true
hasFlags("--test", "cool=true", "-s"); // true
hasFlags("special"); // false
```
