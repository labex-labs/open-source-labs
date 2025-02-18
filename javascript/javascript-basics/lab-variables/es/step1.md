# Variables

> Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.

Las variables son contenedores que almacenan valores. Comienza declarando una variable con la palabra clave `let`, seguida del nombre que le das a la variable:

```js
let myVariable;
```

Un punto y coma al final de una línea indica donde termina una declaración. Solo es necesario cuando necesitas separar declaraciones en una sola línea. Sin embargo, algunas personas creen que es una buena práctica tener puntos y comas al final de cada declaración. Hay otras reglas sobre cuándo se debe y no se debe usar puntos y comas.

Puedes nombrar una variable casi como quieras, pero hay algunas restricciones. Si no estás seguro, puedes [verificar el nombre de tu variable](https://mothereff.in/js-variables) para ver si es válido.

JavaScript distingue entre mayúsculas y minúsculas. Esto significa que `myVariable` no es lo mismo que `myvariable`. Si tienes problemas en tu código, ¡verifica las mayúsculas y minúsculas!

Después de declarar una variable, puedes darle un valor:

```js
myVariable = "Bob";
```

También, puedes hacer ambas operaciones en la misma línea:

```js
let myVariable = "Bob";
```

Recuperas el valor llamando al nombre de la variable:

```js
myVariable;
```

Después de asignar un valor a una variable, puedes cambiarlo más adelante en el código:

```js
let myVariable = "Bob";
myVariable = "Steve";
```

Ten en cuenta que las variables pueden contener valores que tienen diferentes [tipos de datos](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures):

| Variable                                                                        | Explicación                                                                                                                                | Ejemplo                                                                                                                   |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| [Cadena (String)](https://developer.mozilla.org/en-US/docs/Glossary/String)     | Esta es una secuencia de texto conocida como cadena. Para indicar que el valor es una cadena, enciérralo entre comillas simples o dobles.  | `let myVariable = 'Bob';` o `let myVariable = "Bob";`                                                                     |
| [Número (Number)](https://developer.mozilla.org/en-US/docs/Glossary/Number)     | Este es un número. Los números no tienen comillas alrededor.                                                                               | `let myVariable = 10;`                                                                                                    |
| [Booleano (Boolean)](https://developer.mozilla.org/en-US/docs/Glossary/Boolean) | Este es un valor Verdadero/Falso. Las palabras `true` y `false` son palabras clave especiales que no necesitan comillas.                   | `let myVariable = true;`                                                                                                  |
| [Arreglo (Array)](https://developer.mozilla.org/en-US/docs/Glossary/Array)      | Esta es una estructura que te permite almacenar múltiples valores en una sola referencia.                                                  | `let myVariable = [1,'Bob','Steve',10];` Referirse a cada miembro del arreglo así: `myVariable[0]`, `myVariable[1]`, etc. |
| [Objeto (Object)](https://developer.mozilla.org/en-US/docs/Glossary/Object)     | Esto puede ser cualquier cosa. Todo en JavaScript es un objeto y se puede almacenar en una variable. Ten esto en cuenta mientras aprendes. | `let myVariable = document.querySelector('h1');` Todos los ejemplos anteriores también.                                   |

Entonces, ¿por qué necesitamos variables? Las variables son necesarias para hacer cualquier cosa interesante en la programación. Si los valores no pudieran cambiar, entonces no podrías hacer nada dinámico, como personalizar un mensaje de saludo o cambiar una imagen mostrada en una galería de imágenes.
