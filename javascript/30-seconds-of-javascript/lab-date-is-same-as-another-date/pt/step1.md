# Verificando se Duas Datas São Iguais

Para verificar se duas datas são iguais, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Date.prototype.toISOString()` e a verificação de igualdade estrita (`===`) para comparar as duas datas.
3.  Aqui está um exemplo de trecho de código:

```js
const isSameDate = (dateA, dateB) =>
  dateA.toISOString() === dateB.toISOString();
```

4.  Teste a função com duas datas como argumentos para ver se elas são iguais:

```js
isSameDate(new Date(2010, 10, 20), new Date(2010, 10, 20)); // true
```

Esta função verifica se as duas datas são iguais comparando suas representações em string ISO.
