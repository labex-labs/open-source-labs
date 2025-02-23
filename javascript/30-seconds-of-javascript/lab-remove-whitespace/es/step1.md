# Función para eliminar espacios en blanco

Para eliminar los espacios en blanco de una cadena, utiliza la siguiente función.

- Utiliza `String.prototype.replace()` con una expresión regular para reemplazar todas las ocurrencias de caracteres de espacio en blanco con una cadena vacía.

```js
const removeWhitespace = (str) => str.replace(/\s+/g, "");
```

## Explicación de la expresión regular

- `/\s+/g` se descompone como:
  - `\s`: Coincide con cualquier carácter de espacio en blanco (espacios, tabulaciones, saltos de línea)
  - `+`: Coincide con una o más ocurrencias del carácter anterior
  - `/g`: Banderas globales - coincide con todas las ocurrencias en la cadena, no solo con la primera

## Referencia rápida de expresiones regulares

Patrones de espacio en blanco comunes:

- `\s` - coincide con cualquier espacio en blanco (espacio, tabulación, retorno de carro)
- `\t` - coincide con caracteres de tabulación
- `\n` - coincide con caracteres de nueva línea
- `\r` - coincide con retornos de carro
- (espacio) - coincide solo con caracteres de espacio

Por ejemplo,

```js
removeWhitespace("Lorem ipsum.\n Dolor sit amet. ");
// 'Loremipsum.Dolorsitamet.'

// Más ejemplos:
removeWhitespace("Hello    World"); // "HelloWorld"
removeWhitespace("Tab\there\nNew line"); // "TabhereNewline"
```

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.
