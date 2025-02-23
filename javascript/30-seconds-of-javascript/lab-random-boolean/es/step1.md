# Cómo generar un valor booleano aleatorio en JavaScript

Para generar un valor booleano aleatorio en JavaScript, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza el método `Math.random()` para generar un número aleatorio.
3. Verifica si el número aleatorio es mayor o igual a `0.5`.
4. Devuelve `true` si el número es mayor o igual a `0.5`, de lo contrario devuelve `false`.

A continuación, se muestra una implementación concisa del código:

```js
const randomBoolean = () => Math.random() >= 0.5;
```

Puedes probar la función llamando a `randomBoolean()`, lo que devolverá `true` o `false`.
