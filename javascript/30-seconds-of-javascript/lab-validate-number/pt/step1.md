# Função de Validação de Número

Para validar se uma entrada fornecida é um número, siga estes passos:

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- Use `parseFloat()` para tentar converter a entrada em um número.
- Use `Number.isNaN()` e o operador lógico de negação (`!`) para verificar se a entrada é um número.
- Use `Number.isFinite()` para verificar se a entrada é finita.
- Use `Number` e o operador de igualdade solta (`==`) para verificar se a coerção (coercion) é válida.

Aqui está o código para a função `validateNumber`:

```js
const validateNumber = (input) => {
  const num = parseFloat(input);
  return !Number.isNaN(num) && Number.isFinite(num) && Number(input) == input;
};
```

Você pode usar a função `validateNumber` da seguinte forma:

```js
validateNumber("10"); // true
validateNumber("a"); // false
```
