# Como Transformar uma String em um Número Usando JavaScript

Para transformar uma string de entrada em um número inteiro usando JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use os métodos `String.prototype.split()` e `Array.prototype.reduce()` para criar um hash da string de entrada, utilizando deslocamento de bits (bit shifting).
3.  Aqui está o código para a função `sdbm` que implementa o algoritmo de hashing:

```js
const sdbm = (str) => {
  let arr = str.split("");
  return arr.reduce(
    (hashCode, currentVal) =>
      (hashCode =
        currentVal.charCodeAt(0) +
        (hashCode << 6) +
        (hashCode << 16) -
        hashCode),
    0
  );
};
```

4.  Para testar a função, chame-a com um argumento string:

```js
sdbm("name"); // -3521204949
```

Isso retornará o valor do hash para a string de entrada "name".
