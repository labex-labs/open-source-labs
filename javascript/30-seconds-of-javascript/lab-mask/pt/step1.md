# Como Mascar um Valor em JavaScript

Para mascarar um valor em JavaScript, você pode usar a função `mask()`. Siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `String.prototype.slice()` para pegar a porção dos caracteres que permanecerão sem máscara.
3. Use `String.prototype.padStart()` para preencher o início da string com o caractere de `mask` até o comprimento original.
4. Se você quiser excluir caracteres do final da string, use um valor negativo para `num`.
5. Se você não especificar um valor para `num`, a função usará por padrão os últimos 4 caracteres sem máscara.
6. Se você não especificar um valor para `mask`, a função usará por padrão o caractere `'*'` para a máscara.

Aqui está o código para a função `mask()`:

```js
const mask = (cc, num = 4, mask = "*") =>
  `${cc}`.slice(-num).padStart(`${cc}`.length, mask);
```

E aqui estão alguns exemplos de como usar a função `mask()`:

```js
mask(1234567890); // '******7890'
mask(1234567890, 3); // '*******890'
mask(1234567890, -4, "$"); // '$$$$567890'
```
