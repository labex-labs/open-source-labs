# Cómo eliminar caracteres no ASCII en JavaScript

Para eliminar caracteres ASCII no imprimibles en JavaScript, puedes seguir estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza el método `String.prototype.replace()` con una expresión regular para eliminar los caracteres ASCII no imprimibles.
3. La expresión regular `/[^\x20-\x7E]/g` coincide con cualquier carácter que no esté en el rango ASCII imprimible (valores decimales del 32 al 126).
4. La bandera `g` se utiliza para realizar una coincidencia global (es decir, reemplazar todas las ocurrencias de caracteres no ASCII en la cadena).
5. Aquí tienes un ejemplo de cómo usar la función `removeNonASCII`:

```js
const removeNonASCII = (str) => str.replace(/[^\x20-\x7E]/g, "");

removeNonASCII("äÄçÇéÉêlorem-ipsumöÖÐþúÚ"); // 'lorem-ipsum'
```

Esto devolverá la cadena con todos los caracteres no ASCII eliminados.
