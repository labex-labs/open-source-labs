# Función para calcular la suma de potencias en un rango dado

Para calcular la suma de las potencias de todos los números dentro de un rango especificado (incluyendo ambos extremos), utiliza la siguiente función:

```js
const sumPower = (end, power = 2, start = 1) =>
  Array(end + 1 - start)
    .fill(0)
    .map((x, i) => (i + start) ** power)
    .reduce((a, b) => a + b, 0);
```

Así es como puedes utilizar esta función:

- Llama a `sumPower(end)` para calcular la suma de los cuadrados de todos los números del 1 al `end`.
- Llama a `sumPower(end, power)` para calcular la suma de las potencias `power`-ésimas de todos los números del 1 al `end`.
- Llama a `sumPower(end, power, start)` para calcular la suma de las potencias `power`-ésimas de todos los números de `start` a `end`.

Tenga en cuenta que los segundos y terceros argumentos (`power` y `start`) son opcionales y por defecto valen `2` y `1` respectivamente si no se proporcionan.

Ejemplo:

```js
sumPower(10); // Devuelve 385 (suma de cuadrados de números del 1 al 10)
sumPower(10, 3); // Devuelve 3025 (suma de cubos de números del 1 al 10)
sumPower(10, 3, 5); // Devuelve 2925 (suma de cubos de números del 5 al 10)
```
