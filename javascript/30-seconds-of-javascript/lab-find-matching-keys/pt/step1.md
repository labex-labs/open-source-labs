# Encontrar Chaves Correspondentes

Para encontrar todas as chaves em um objeto que correspondem a um determinado valor, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Object.keys()` para obter todas as propriedades do objeto.
3.  Use `Array.prototype.filter()` para testar cada par chave-valor e retornar todas as chaves que são iguais ao valor fornecido.

Aqui está um exemplo de função que implementa essa lógica:

```js
const findKeys = (obj, val) =>
  Object.keys(obj).filter((key) => obj[key] === val);
```

Você pode usar esta função da seguinte forma:

```js
const ages = {
  Leo: 20,
  Zoey: 21,
  Jane: 20
};
findKeys(ages, 20); // [ 'Leo', 'Jane' ]
```
