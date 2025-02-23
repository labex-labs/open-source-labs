# Funciones

> La `index.html` ya se ha proporcionado en la máquina virtual.

Las [Funciones](https://developer.mozilla.org/en-US/docs/Glossary/Function) son una forma de empaquetar funcionalidad que desees reutilizar. Es posible definir un bloque de código como una función que se ejecuta cuando llamas al nombre de la función en tu código. Esta es una buena alternativa a escribir repetidamente el mismo código. Ya has visto algunos usos de funciones.

Por ejemplo:

```js
let myVariable = document.querySelector("h1");
```

```js
alert("hello!");
```

Estas funciones, `document.querySelector` y `alert`, están integradas en el navegador.

> Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.

Si ves algo que parece un nombre de variable, pero está seguido de paréntesis — `()` — es probable que sea una función. Las funciones a menudo toman [argumentos](https://developer.mozilla.org/en-US/docs/Glossary/Argument): trozos de datos que necesitan para hacer su trabajo. Los argumentos van dentro de los paréntesis, separados por comas si hay más de un argumento.

Por ejemplo, la función `alert()` hace que aparezca una caja emergente dentro de la ventana del navegador, pero necesitamos darle una cadena como argumento para decirle a la función qué mensaje mostrar.

También puedes definir tus propias funciones.

En el siguiente ejemplo, creamos una función simple que toma dos números como argumentos y los multiplica:

> Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.

```js
function multiply(num1, num2) {
  let result = num1 * num2;
  return result;
}
```

Pruebe a ejecutar esto en la consola; luego pruebe con varios argumentos. Por ejemplo:

```js
multiply(4, 7);
multiply(20, 20);
multiply(0.5, 3);
```

> **Nota:** La declaración [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return) le dice al navegador que devuelva la variable `result` fuera de la función para que esté disponible para su uso. Esto es necesario porque las variables definidas dentro de las funciones solo están disponibles dentro de esas funciones. Esto se llama alcance de variables. (Lea más sobre [alcance de variables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variable_scope).)
