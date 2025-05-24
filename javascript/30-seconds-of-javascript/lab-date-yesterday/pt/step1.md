# Obtendo a Data de Ontem no Formato yyyy-mm-dd

Para obter a data de ontem no formato `yyyy-mm-dd`, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use o construtor `Date` para obter a data atual.
3. Decremente a data em um dia usando `Date.prototype.getDate()`.
4. Defina a data decrementada usando `Date.prototype.setDate()`.
5. Use `Date.prototype.toISOString()` para retornar uma string no formato `yyyy-mm-dd`.
6. Chame a função `yesterday()` para obter a data de ontem.

```js
const yesterday = () => {
  let d = new Date();
  d.setDate(d.getDate() - 1);
  return d.toISOString().split("T")[0];
};

yesterday(); // returns "2018-10-17" (if current date is 2018-10-18)
```

Seguindo estes passos, você será capaz de recuperar a data de ontem de maneira clara e concisa.
