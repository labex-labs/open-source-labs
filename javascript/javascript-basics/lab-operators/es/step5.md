# No, No es igual

Esto devuelve el valor lógicamente opuesto de lo que le precede. Convierte un `true` en un `false`, etc. Cuando se utiliza junto con el operador de igualdad, el operador de negación prueba si dos valores no son iguales.

Para "No", la expresión básica es verdadera, pero la comparación devuelve `false` porque la negamos:

```js
// Not(!)
let myVariable = 3;
!(myVariable === 3);
```

"No es igual" da básicamente el mismo resultado con una sintaxis diferente. Aquí estamos probando "¿`myVariable` no es igual a 3?". Esto devuelve `false` porque `myVariable` ES igual a 3:

```js
// Does-not-equal(!==)
let myVariable = 3;
myVariable !== 3;
```

Hay muchos más operadores para explorar, pero esto es suficiente por ahora. Consulte [Expresiones y operadores](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators) para obtener una lista completa.

> **Nota:** Mezclar tipos de datos puede dar lugar a algunos resultados extraños al realizar cálculos. Tenga cuidado de referirse correctamente a sus variables y obtener los resultados que espera. Por ejemplo, escriba `'35' + '25'` en su consola. ¿Por qué no obtiene el resultado que esperaba? Porque las comillas simples convierten los números en cadenas, por lo que ha terminado concatenando cadenas en lugar de sumar números. Si escribe `35 + 25` obtendrá la suma de los dos números.
