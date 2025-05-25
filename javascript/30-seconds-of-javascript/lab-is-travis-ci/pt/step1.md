# Verificando se o Ambiente é Travis CI

Para verificar se você está executando no Travis CI, use a função `isTravisCI()`. Esta função verifica se as variáveis de ambiente `TRAVIS` e `CI` estão presentes.

```js
const isTravisCI = () => "TRAVIS" in process.env && "CI" in process.env;
```

Para começar a codificar no Travis CI, abra o Terminal/SSH e digite `node`.
