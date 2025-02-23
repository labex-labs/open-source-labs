# Cómo convertir una cadena en una matriz de caracteres en JavaScript

Para convertir una cadena en una matriz de caracteres en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el operador de propagación (`...`) para convertir la cadena en una matriz de caracteres.
3. Defina una función llamada `toCharArray` que tome una cadena como argumento y devuelva una matriz de sus caracteres.
4. Llame a la función `toCharArray` con la cadena que desea convertir como argumento.
5. La función devolverá una matriz de caracteres.

Aquí está el código:

```js
const toCharArray = (s) => [...s];

toCharArray("hello"); // ['h', 'e', 'l', 'l', 'o']
```
