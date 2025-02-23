# Obtener la URL base

Para obtener la URL base a partir de una URL dada, siga estos pasos:

1. Abra la Terminal/SSH.
2. Escriba `node` para comenzar a practicar la codificación.
3. Utilice la siguiente función de JavaScript para obtener la URL actual sin ningún parámetro o identificador de fragmento:

```js
const getBaseURL = (url) => url.replace(/[?#].*$/, "");
```

4. Reemplace `url` con la URL de la que desea obtener la URL base.
5. La función eliminará todo lo que venga después de `'?'` o `'#'`, si los encuentra, y devolverá la URL base.
6. Aquí hay un ejemplo:

```js
getBaseURL("http://url.com/page?name=Adam&surname=Smith");
// 'http://url.com/page'
```
