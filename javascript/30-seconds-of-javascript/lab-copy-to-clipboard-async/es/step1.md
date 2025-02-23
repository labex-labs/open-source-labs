# Función para copiar una cadena al portapapeles

Para copiar una cadena al portapapeles, utiliza la función `copyToClipboardAsync`. La función devuelve una promesa que se resuelve cuando el contenido del portapapeles se ha actualizado. Aquí están los pasos:

1. Comprueba si la API de Portapapeles está disponible verificando si `Navigator`, `Navigator.clipboard` y `Navigator.clipboard.writeText` son verdaderos utilizando una declaración `if`.
2. Si la API de Portapapeles está disponible, utiliza `Clipboard.writeText()` para escribir el valor dado, `str`, en el portapapeles.
3. Devuelve el resultado de `Clipboard.writeText()`, que es una promesa que se resuelve cuando el contenido del portapapeles se ha actualizado.
4. Si la API de Portapapeles no está disponible, rechaza la promesa con un mensaje de error adecuado utilizando `Promise.reject()`.
5. Si necesitas admitir navegadores antiguos, utiliza `Document.execCommand()` en lugar de `Clipboard.writeText()`. Puedes obtener más información sobre ello en el fragmento `copyToClipboard`.

Aquí está la función `copyToClipboardAsync`:

```js
const copyToClipboardAsync = (str) => {
  if (navigator && navigator.clipboard && navigator.clipboard.writeText) {
    return navigator.clipboard.writeText(str);
  }
  return Promise.reject("The Clipboard API is not available.");
};
```

Para utilizar la función, llama a `copyToClipboardAsync` con la cadena que quieres copiar como argumento, así:

```js
copyToClipboardAsync("Lorem ipsum"); // 'Lorem ipsum' copiado al portapapeles.
```
