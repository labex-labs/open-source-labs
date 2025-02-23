# Función para Copiar el Signo de un Número a Otro

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

La función `copySign` devuelve el valor absoluto del primer número, pero con el signo del segundo número. Para lograr esto:

1. Utiliza `Math.sign()` para comprobar si los dos números tienen el mismo signo.
2. Devuelve `x` si es así, `-x` en caso contrario.

Aquí está el código para la función `copySign`:

```js
const copySign = (x, y) => (Math.sign(x) === Math.sign(y) ? x : -x);
```

Puedes probar la función utilizando el siguiente código:

```js
copySign(2, 3); // 2
copySign(2, -3); // -2
copySign(-2, 3); // 2
copySign(-2, -3); // -2
```
