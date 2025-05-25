# Convertendo Números para Notação de Ponto Fixo

Para converter um número para notação de ponto fixo sem zeros à direita, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `Number.prototype.toFixed()` para converter o número em uma string de notação de ponto fixo.
3. Use `Number.parseFloat()` para converter a string de notação de ponto fixo de volta para um número, removendo os zeros à direita.
4. Use uma template literal para converter o número em uma string.

Código de exemplo:

```js
const toOptionalFixed = (num, digits) =>
  `${Number.parseFloat(num.toFixed(digits))}`;
```

Você pode testar a função com diferentes entradas:

```js
toOptionalFixed(1, 2); // '1'
toOptionalFixed(1.001, 2); // '1'
toOptionalFixed(1.5, 2); // '1.5'
```
