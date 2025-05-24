# Função para Testar se Todos os Elementos do Array São Falsos

Para testar se todos os elementos em um array são falsos, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.some()` para testar se algum elemento na coleção retorna `true` com base na função predicado fornecida.
3.  Se você omitir o segundo argumento, `fn`, a função usará `Boolean` como padrão.
4.  A função retorna `true` se todos os elementos no array são falsos e `false` caso contrário.

Aqui está um exemplo de implementação da função:

```js
const none = (arr, fn = Boolean) => !arr.some(fn);
```

Você pode usar a função da seguinte forma:

```js
none([0, 1, 3, 0], (x) => x == 2); // true
none([0, 0, 0]); // true
```
