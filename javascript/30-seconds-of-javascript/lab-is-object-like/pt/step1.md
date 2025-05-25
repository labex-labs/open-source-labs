# Verificando se um Valor é Semelhante a um Objeto

Para verificar se um valor é semelhante a um objeto, siga estes passos:

1.  Abra o Terminal/SSH.
2.  Digite `node` para começar a praticar a codificação.
3.  Verifique se o valor fornecido não é `null` e seu `typeof` é igual a `'object'`.

Aqui está o código que você pode usar:

```js
const isObjectLike = (val) => val !== null && typeof val === "object";
```

Você pode testar esta função com os seguintes exemplos:

```js
isObjectLike({}); // true
isObjectLike([1, 2, 3]); // true
isObjectLike((x) => x); // false
isObjectLike(null); // false
```
