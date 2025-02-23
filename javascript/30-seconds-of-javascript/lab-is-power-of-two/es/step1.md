# Comprobar si un número es una potencia de dos

Para comprobar si un número es una potencia de dos, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el operador AND binario bit a bit (`&`) para determinar si el número (`n`) es una potencia de `2`.
3. Además, compruebe que `n` no es falso.
4. El siguiente código comprueba funcionalmente si `n` es una potencia de dos:

```js
const isPowerOfTwo = (n) => !!n && (n & (n - 1)) == 0;
```

A continuación, se presentan algunos ejemplos de cómo utilizar la función `isPowerOfTwo`:

```js
isPowerOfTwo(0); // false
isPowerOfTwo(1); // true
isPowerOfTwo(8); // true
```
