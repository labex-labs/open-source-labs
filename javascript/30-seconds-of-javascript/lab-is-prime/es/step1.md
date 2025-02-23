# Función para comprobar si un número es primo

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. Esta función comprueba si un entero dado es un número primo. Estos son los pasos para comprobar si un número es primo:

1. Comprueba los números desde `2` hasta la raíz cuadrada del número dado.
2. Si alguno de ellos divide al número dado, devuelve `false`.
3. Si ninguno de ellos divide al número dado, devuelve `true`, a menos que el número sea menor que `2`.

Aquí está el código para implementar esta función en JavaScript:

```js
const isPrime = (num) => {
  const boundary = Math.floor(Math.sqrt(num));
  for (let i = 2; i <= boundary; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return num >= 2;
};
```

Puedes probar la función llamándola con un número como argumento:

```js
isPrime(11); // true
```
