# Como Extrair Valores de um Array em JavaScript

Para extrair valores específicos de um array em JavaScript, você pode usar os métodos `Array.prototype.filter()` e `Array.prototype.includes()`. Veja como você pode fazer isso:

```js
const pull = (arr, ...args) => {
  let argState = Array.isArray(args[0]) ? args[0] : args;
  let pulled = arr.filter((v) => !argState.includes(v));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
};
```

A função `pull` recebe um array e um ou mais argumentos que representam os valores a serem removidos. A função então cria um novo array filtrando os valores especificados usando `Array.prototype.filter()`. Em seguida, ela muta o array original, redefinindo seu comprimento para `0` e repovoando-o apenas com os valores extraídos usando `Array.prototype.push()`.

Aqui está um exemplo de como você pode usar a função `pull`:

```js
let myArray = ["a", "b", "c", "a", "b", "c"];
pull(myArray, "a", "c"); // myArray = [ 'b', 'b' ]
```

Neste exemplo, a função `pull` remove todas as ocorrências de `'a'` e `'c'` do array `myArray` e retorna um novo array com apenas os valores `'b'` e `'b'`.
