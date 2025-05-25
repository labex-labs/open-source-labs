# Como Remover Caracteres Não-ASCII em JavaScript

Para remover caracteres ASCII não imprimíveis em JavaScript, você pode seguir estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `String.prototype.replace()` com uma expressão regular para remover caracteres ASCII não imprimíveis.
3.  A expressão regular `/[^\x20-\x7E]/g` corresponde a qualquer caractere que não esteja no intervalo ASCII imprimível (valores decimais de 32 a 126).
4.  A flag `g` é usada para realizar uma correspondência global (ou seja, substituir todas as ocorrências de caracteres não-ASCII na string).
5.  Aqui está um exemplo de como usar a função `removeNonASCII`:

```js
const removeNonASCII = (str) => str.replace(/[^\x20-\x7E]/g, "");

removeNonASCII("äÄçÇéÉêlorem-ipsumöÖÐþúÚ"); // 'lorem-ipsum'
```

Isso retornará a string com todos os caracteres não-ASCII removidos.
