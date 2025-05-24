# Usando a Função `When` para Aplicar Condições

Para aplicar uma função quando uma determinada condição for atendida, use a função `when`. Para começar, abra o Terminal/SSH e digite `node`.

A função `when` retorna uma nova função que recebe um argumento e executa um _callback_ se o argumento for _truthy_, ou retorna o argumento se for _falsy_. A função espera um único valor, `x`, e retorna o valor apropriado com base no parâmetro `pred`.

Aqui está um exemplo de implementação da função `when`:

```js
const when = (pred, whenTrue) => (x) => (pred(x) ? whenTrue(x) : x);
```

Você pode usar a função `when` para criar uma nova função que dobra números pares:

```js
const doubleEvenNumbers = when(
  (x) => x % 2 === 0,
  (x) => x * 2
);
doubleEvenNumbers(2); // 4
doubleEvenNumbers(1); // 1
```
