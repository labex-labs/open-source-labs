# Criando a Função para Minúsculas

Agora que entendemos como acessar as chaves do objeto e usar o método `reduce()`, vamos criar uma função que converte todas as chaves de um objeto para minúsculas.

No seu shell interativo do Node.js, defina a seguinte função:

```javascript
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};
```

Vamos detalhar o que esta função faz:

1. `Object.keys(obj)` obtém todas as chaves do objeto de entrada
2. `.reduce()` transforma essas chaves em um novo objeto
3. Para cada chave, criamos uma nova entrada no objeto acumulador (`acc`) com:
   - A chave convertida para minúsculas usando `key.toLowerCase()`
   - O valor original do objeto de entrada (`obj[key]`)
4. Começamos com um objeto vazio `{}` como o valor inicial para o acumulador
5. Finalmente, retornamos o acumulador, que é nosso novo objeto com chaves em minúsculas

Agora, vamos testar nossa função com o objeto `user` que criamos anteriormente:

```javascript
const lowercaseUser = lowerizeKeys(user);
lowercaseUser;
```

Você deve ver a saída:

```
{ name: 'John', age: 30, email: 'john@example.com' }
```

Perfeito! Todas as chaves agora estão em minúsculas.

Vamos tentar outro exemplo para garantir que nossa função funcione corretamente:

```javascript
const product = {
  ProductID: 101,
  ProductName: "Laptop",
  PRICE: 999.99
};

lowerizeKeys(product);
```

A saída deve ser:

```
{ productid: 101, productname: 'Laptop', price: 999.99 }
```

Nossa função funciona corretamente para diferentes objetos com vários estilos de capitalização de chaves.
