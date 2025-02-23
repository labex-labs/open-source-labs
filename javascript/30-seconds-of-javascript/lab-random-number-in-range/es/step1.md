# Cómo generar un número aleatorio en un rango dado utilizando JavaScript

Para generar un número aleatorio en un rango específico utilizando JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `Math.random()` para generar un valor aleatorio.
3. Mapee el valor generado al rango deseado utilizando multiplicación.
4. Utilice el siguiente código para crear una función que genere un número aleatorio en el rango dado:

```js
const randomNumberInRange = (min, max) => Math.random() * (max - min) + min;
```

5. Para utilizar la función, pase los valores mínimo y máximo del rango deseado como argumentos. Por ejemplo:

```js
randomNumberInRange(2, 10); // 6.0211363285087005
```

Siguiendo estos pasos, puede generar fácilmente un número aleatorio en un rango dado utilizando JavaScript.
