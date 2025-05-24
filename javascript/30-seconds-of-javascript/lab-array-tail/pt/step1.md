# Como Obter a "Tail" de um Array em JavaScript

Para obter todos os elementos de um array, exceto o primeiro, você pode usar o método `Array.prototype.slice()`. Se o comprimento do array for maior que 1, use `slice(1)` para retornar o array sem o primeiro elemento. Caso contrário, retorne o array inteiro.

Embora o "slicing" negativo (como `slice(-4)`) seja possível em JavaScript e fatias a partir do final, usamos `slice(1)` aqui porque:

1.  Comunica claramente nossa intenção de pular o primeiro elemento.
2.  Funciona consistentemente, independentemente do comprimento do array.
3.  O "slicing" negativo exigiria conhecer o comprimento do array para obter o mesmo resultado.

Aqui está um exemplo de código:

```js
const tail = (arr) => (arr.length > 1 ? arr.slice(1) : arr);
```

Agora você pode usar a função `tail()` para obter a "tail" do array:

```js
tail([1, 2, 3]); // [2, 3]
tail([1]); // [1]
```
