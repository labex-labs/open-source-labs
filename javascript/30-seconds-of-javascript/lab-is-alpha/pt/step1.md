# Função para Verificar se uma String é Alfa

Para verificar se uma string contém apenas caracteres alfabéticos:

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- Use `RegExp.prototype.test()` para verificar se a string fornecida corresponde ao padrão de expressão regular alfabético.
- A função `isAlpha` recebe uma string como argumento e retorna `true` se a string contiver apenas caracteres alfabéticos e `false` caso contrário.

Aqui está um exemplo:

```js
const isAlpha = (str) => /^[a-zA-Z]*$/.test(str);
```

```js
isAlpha("sampleInput"); // true
isAlpha("this Will fail"); // false
isAlpha("123"); // false
```
