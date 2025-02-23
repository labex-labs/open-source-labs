# Cómo crear una función con un número específico de argumentos

Para crear una función que acepte un número específico de argumentos y ignore cualquier argumento adicional, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.

2. Utilice el siguiente código para crear su función:

```js
const ary =
  (fn, n) =>
  (...args) =>
    fn(...args.slice(0, n));
```

3. Llame a la función que acaba de crear, `ary`, con dos argumentos: la función para la que desea limitar los argumentos (`fn`) y el número de argumentos hasta el que desea limitarla (`n`).

4. Ahora puede usar la nueva función para limitar el número de argumentos de cualquier función que desee. Para hacer esto, llame a su nueva función con el operador de propagación (`...`) y los argumentos que desea limitar.

A continuación, se muestra un ejemplo de cómo usar su nueva función:

```js
const firstTwoMax = ary(Math.max, 2);
[[2, 6, "a"], [6, 4, 8], [10]].map((x) => firstTwoMax(...x)); // [6, 6, 10]
```

En este ejemplo, `firstTwoMax` es una nueva función que limita la función `Math.max` a solo aceptar los primeros dos argumentos. El método `map` se utiliza para aplicar la nueva función a cada matriz en la matriz externa, devolviendo el máximo de los primeros dos elementos de cada matriz interna.
