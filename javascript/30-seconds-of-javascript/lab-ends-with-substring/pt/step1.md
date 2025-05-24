# Uma Função para Verificar se uma String Termina com uma Substring

Para verificar se uma determinada string termina com uma substring de outra string, siga estas etapas:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use um loop `for...in` e `String.prototype.slice()` para obter cada substring da `word` fornecida, começando pelo final.
3.  Use `String.prototype.endsWith()` para verificar a substring atual em relação ao `text`.
4.  Retorne a substring correspondente, se encontrada. Caso contrário, retorne `undefined`.

Aqui está o trecho de código para implementar as etapas acima:

```js
const endsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(0, i + 1);
    if (text.endsWith(substr)) return substr;
  }
  return undefined;
};
```

Você pode testar a função com o seguinte exemplo:

```js
endsWithSubstring("Lorem ipsum dolor sit amet<br /", "<br />"); // '<br /'
```
