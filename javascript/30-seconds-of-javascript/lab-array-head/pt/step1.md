# Como Obter o Primeiro Elemento de um Array em JavaScript

Para obter o primeiro elemento de um array em JavaScript, você pode usar a função `head`. Veja como você pode usá-la:

1.  Abra o Terminal/SSH.
2.  Digite `node` para começar a praticar a codificação.
3.  Use o seguinte código para obter o primeiro elemento (head) de um array:

```js
const head = (arr) => (arr && arr.length ? arr[0] : undefined);
```

4.  Chame a função `head` com um array como seu argumento para obter o primeiro elemento. Se o array estiver vazio ou for falsy, a função retornará `undefined`.

Aqui estão alguns exemplos:

```js
head([1, 2, 3]); // 1
head([]); // undefined
head(null); // undefined
head(undefined); // undefined
```
