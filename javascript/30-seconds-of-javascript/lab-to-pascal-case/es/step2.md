# Trabajar con Expresiones Regulares para Dividir Palabras

Para convertir una cadena de texto (string) a Pascal Case, el primer paso es dividir la cadena en palabras individuales. Podemos utilizar expresiones regulares (regex) para identificar los límites de las palabras independientemente del delimitador utilizado (espacios, guiones, guiones bajos, etc.).

En JavaScript, las expresiones regulares se encierran entre barras inclinadas (`/patrón/`). Exploremos cómo usar regex para dividir una cadena de texto en palabras.

1. En su sesión de Node.js, intentemos primero un ejemplo sencillo. Escriba el siguiente código:

```javascript
let str = "hello_world-example";
let words = str.split(/[-_]/);
console.log(words);
```

La salida debería ser:

```
[ 'hello', 'world', 'example' ]
```

Esta regex `/[-_]/` coincide con un guión o un guión bajo, y `split()` utiliza estas coincidencias como separadores.

2. Ahora, intentemos una cadena de texto y una regex más complejas. Escriba:

```javascript
let complexStr = "hello_WORLD-example phrase";
let regex =
  /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g;
let matches = complexStr.match(regex);
console.log(matches);
```

La salida debería ser:

```
[ 'hello', 'WORLD', 'example', 'phrase' ]
```

Desglosemos esta regex:

- `/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)/`: Coincide con secuencias de letras mayúsculas.
- `/[A-Z]?[a-z]+[0-9]*/`: Coincide con palabras que pueden comenzar con una letra mayúscula.
- `/[A-Z]/`: Coincide con letras mayúsculas individuales.
- `/[0-9]+/`: Coincide con secuencias de números.
- La bandera `g` hace que la coincidencia sea global (encuentra todas las coincidencias).

El método `match()` devuelve una matriz (array) de todas las coincidencias encontradas en la cadena de texto. Esto será esencial para nuestro convertidor a Pascal Case, ya que puede identificar palabras en casi cualquier formato.
