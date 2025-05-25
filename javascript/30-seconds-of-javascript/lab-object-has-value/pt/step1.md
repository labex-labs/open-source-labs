# Função para Verificar se um Objeto Contém um Valor Específico

Para verificar se um objeto contém um valor específico, use a seguinte função:

```js
const hasValue = (obj, value) => Object.values(obj).includes(value);
```

Para usar esta função, passe o objeto que você deseja pesquisar e o valor alvo como argumentos. A função retornará `true` se o objeto contiver o valor e `false` se não contiver.

Aqui está um exemplo:

```js
const obj = { a: 100, b: 200 };
console.log(hasValue(obj, 100)); // true
console.log(hasValue(obj, 999)); // false
```

Para começar a codificar, abra o Terminal/SSH e digite `node`.
