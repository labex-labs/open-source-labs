# Como Gerar um Valor Booleano Aleatório em JavaScript

Para gerar um valor booleano aleatório em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Math.random()` para gerar um número aleatório.
3.  Verifique se o número aleatório é maior ou igual a `0.5`.
4.  Retorne `true` se o número for maior ou igual a `0.5`, caso contrário, retorne `false`.

Aqui está uma implementação concisa do código:

```js
const randomBoolean = () => Math.random() >= 0.5;
```

Você pode testar a função chamando `randomBoolean()`, que retornará `true` ou `false`.
