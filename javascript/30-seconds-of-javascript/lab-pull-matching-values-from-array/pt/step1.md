# Como Extrair Valores Correspondentes de um Array

Para extrair valores específicos de um array usando JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.filter()` e `Array.prototype.includes()` para filtrar os valores que não são necessários e criar um novo array.
3.  Defina `Array.prototype.length` para mutar o array original, redefinindo seu comprimento para `0`.
4.  Use `Array.prototype.push()` para repovoar o array original com apenas os valores extraídos.
5.  Use `Array.prototype.push()` para manter o controle dos valores removidos em um novo array.

Aqui está um exemplo de função que implementa esses passos:

```js
const pullAtValue = (arr, pullArr) => {
  let removed = [],
    pushToRemove = arr.forEach((v, i) =>
      pullArr.includes(v) ? removed.push(v) : v
    ),
    mutateTo = arr.filter((v, i) => !pullArr.includes(v));
  arr.length = 0;
  mutateTo.forEach((v) => arr.push(v));
  return removed;
};
```

Você pode usar esta função para remover valores específicos de um array e retornar os elementos removidos assim:

```js
let myArray = ["a", "b", "c", "d"];
let pulled = pullAtValue(myArray, ["b", "d"]);
// myArray = [ 'a', 'c' ] , pulled = [ 'b', 'd' ]
```
