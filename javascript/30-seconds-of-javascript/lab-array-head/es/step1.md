# Cómo obtener el primer elemento de un array en JavaScript

Para obtener el primer elemento de un array en JavaScript, puedes usar la función `head`. Aquí te muestra cómo utilizarla:

1. Abre la Terminal/SSH.
2. Escribe `node` para comenzar a practicar la codificación.
3. Utiliza el siguiente código para obtener el primer elemento de un array:

```js
const head = (arr) => (arr && arr.length ? arr[0] : undefined);
```

4. Llama a la función `head` con un array como argumento para obtener el primer elemento. Si el array está vacío o es falso, la función devolverá `undefined`.

Aquí hay algunos ejemplos:

```js
head([1, 2, 3]); // 1
head([]); // undefined
head(null); // undefined
head(undefined); // undefined
```
