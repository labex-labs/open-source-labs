# Función para convertir una cadena en una matriz de palabras

Para convertir una cadena dada en una matriz de palabras, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `String.prototype.split()` con un `patrón` suministrado (por defecto es no alfanumérico como una expresión regular) para convertir en una matriz de cadenas.
3. Utilice el método `Array.prototype.filter()` para eliminar cualquier cadena vacía.
4. Omita el segundo argumento, `patrón`, para utilizar la expresión regular predeterminada.

Aquí hay una función que implementa estos pasos:

```js
const words = (str, pattern = /[^a-zA-Z-]+/) =>
  str.split(pattern).filter(Boolean);
```

Puede utilizar la función `words()` con diferentes cadenas para convertirlas en matrices de palabras:

```js
words("I love javaScript!!"); // ['I', 'love', 'javaScript']
words("python, javaScript & coffee"); // ['python', 'javaScript', 'coffee']
```
