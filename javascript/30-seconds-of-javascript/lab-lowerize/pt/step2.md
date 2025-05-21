# Acessando as Chaves do Objeto

Antes de podermos transformar as chaves do objeto, precisamos entender como acessá-las. JavaScript fornece o método `Object.keys()`, que retorna um array contendo todas as chaves de um objeto.

No seu shell interativo do Node.js, tente o seguinte:

```javascript
Object.keys(user);
```

Você deve ver uma saída como esta:

```
[ 'Name', 'AGE', 'Email' ]
```

Agora, vamos tentar converter cada chave para minúsculas usando o método `toLowerCase()`. Podemos usar o método `map()` para transformar cada chave:

```javascript
Object.keys(user).map((key) => key.toLowerCase());
```

A saída deve ser:

```
[ 'name', 'age', 'email' ]
```

Ótimo! Agora temos um array com todas as chaves convertidas para minúsculas. No entanto, ainda precisamos criar um novo objeto com essas chaves em minúsculas e os valores originais. Para isso, usaremos o método `reduce()` no próximo passo.

Vamos entender o método `reduce()` antes de prosseguir. Este método executa uma função redutora em cada elemento do array, resultando em um único valor de saída.

Aqui está um exemplo simples de `reduce()`:

```javascript
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((accumulator, currentValue) => {
  return accumulator + currentValue;
}, 0);

sum;
```

A saída será `10`, que é a soma de todos os números no array. O `0` no método `reduce()` é o valor inicial do acumulador.
