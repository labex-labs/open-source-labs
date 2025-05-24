# Como Verificar se uma Data é Anterior a Outra em JavaScript

Para verificar se uma data é anterior a outra em JavaScript, você pode usar o operador "menor que" (`<`). Aqui está um exemplo de função que recebe duas datas e retorna um valor booleano indicando se a primeira data é anterior à segunda:

```js
const isBeforeDate = (dateA, dateB) => dateA < dateB;
```

Você pode usar esta função para verificar se uma data específica é anterior a outra, passando dois objetos `Date` como argumentos. Por exemplo:

```js
isBeforeDate(new Date(2010, 10, 20), new Date(2010, 10, 21)); // true
```
