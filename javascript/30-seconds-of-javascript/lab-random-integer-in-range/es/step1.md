# Cómo generar un número entero aleatorio en un rango específico usando JavaScript

Para generar un número entero aleatorio en un rango específico usando JavaScript, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza el método `Math.random()` para generar un número aleatorio entre 0 y 1.
3. Mapea el número aleatorio al rango deseado multiplicándolo por la diferencia entre los valores máximo y mínimo del rango y luego sumando el valor mínimo al resultado.
4. Utiliza el método `Math.floor()` para redondear hacia abajo el resultado al entero más cercano.

A continuación, se muestra un fragmento de código de ejemplo que implementa los pasos anteriores:

```js
const randomIntegerInRange = (min, max) =>
  Math.floor(Math.random() * (max - min + 1)) + min;
```

Luego, puedes llamar a la función `randomIntegerInRange()` con los valores mínimo y máximo deseados para generar un número entero aleatorio dentro de ese rango. Por ejemplo:

```js
randomIntegerInRange(0, 5); // 2
```
