# Como Remover Tags HTML/XML de uma String

Para remover tags HTML/XML de uma string, você pode usar uma expressão regular (regular expression). Siga estes passos:

1. Abra o Terminal/SSH
2. Digite `node` para começar a praticar a codificação
3. Use o seguinte código:

```js
const stripHTMLTags = (str) => str.replace(/<[^>]*>/g, "");
```

4. Teste a função com o seguinte exemplo:

```js
stripHTMLTags("<p><em>lorem</em> <strong>ipsum</strong></p>"); // 'lorem ipsum'
```

Isso removerá todas as tags HTML/XML da string de entrada e retornará o texto restante.
