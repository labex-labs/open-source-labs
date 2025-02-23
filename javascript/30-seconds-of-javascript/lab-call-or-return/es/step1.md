# Una Función que Llama o Devuelve Otra Función

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

Aquí hay una función llamada `callOrReturn` que toma un argumento y lo llama si es una función, de lo contrario, lo devuelve. Aquí está cómo funciona:

- La función toma dos parámetros: `fn` y `...args`. `fn` es el argumento que se va a comprobar, y `...args` es la lista de argumentos que se pasarán a la función si se llama a ésta.
- Utiliza el operador `typeof` para comprobar si el argumento dado es una función.
- Si el argumento es en efecto una función, la llama utilizando el operador de propagación (`...`) para pasar el resto de los argumentos dados. De lo contrario, simplemente devuelve el argumento.
- Aquí hay un ejemplo de cómo utilizar la función `callOrReturn`:

```js
const callOrReturn = (fn, ...args) =>
  typeof fn === "function" ? fn(...args) : fn;

callOrReturn((x) => x + 1, 1); // 2
callOrReturn(1, 1); // 1
```

En el primer ejemplo, `callOrReturn(x => x + 1, 1)` llama a la función `x => x + 1` con el argumento `1`, lo que devuelve `2`. En el segundo ejemplo, `callOrReturn(1, 1)` simplemente devuelve `1` ya que no es una función.
