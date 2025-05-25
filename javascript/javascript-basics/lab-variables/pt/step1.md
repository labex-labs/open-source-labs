# Variáveis

> Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

Variáveis são contêineres que armazenam valores. Você começa declarando uma variável com a palavra-chave `let`, seguida pelo nome que você dá à variável:

```js
let myVariable;
```

Um ponto e vírgula no final de uma linha indica onde uma instrução termina. Ele só é necessário quando você precisa separar instruções em uma única linha. No entanto, algumas pessoas acreditam que é uma boa prática ter pontos e vírgulas no final de cada instrução. Existem outras regras sobre quando você deve e não deve usar pontos e vírgulas.

Você pode nomear uma variável quase qualquer coisa, mas existem algumas restrições. Se você não tiver certeza, pode [verificar o nome da sua variável](https://mothereff.in/js-variables) para ver se é válido.

JavaScript é _case sensitive_ (sensível a maiúsculas e minúsculas). Isso significa que `myVariable` não é o mesmo que `myvariable`. Se você tiver problemas no seu código, verifique o _case_!

Depois de declarar uma variável, você pode dar a ela um valor:

```js
myVariable = "Bob";
```

Além disso, você pode fazer ambas as operações na mesma linha:

```js
let myVariable = "Bob";
```

Você recupera o valor chamando o nome da variável:

```js
myVariable;
```

Depois de atribuir um valor a uma variável, você pode alterá-lo mais tarde no código:

```js
let myVariable = "Bob";
myVariable = "Steve";
```

Observe que as variáveis podem conter valores que têm diferentes [tipos de dados](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures):

| Variável                                                             | Explicação                                                                                                                              | Exemplo                                                                                                               |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| [String](https://developer.mozilla.org/en-US/docs/Glossary/String)   | Esta é uma sequência de texto conhecida como _string_. Para indicar que o valor é uma _string_, inclua-o entre aspas simples ou duplas. | `let myVariable = 'Bob';` ou `let myVariable = "Bob";`                                                                |
| [Number](https://developer.mozilla.org/en-US/docs/Glossary/Number)   | Este é um número. Os números não têm aspas ao seu redor.                                                                                | `let myVariable = 10;`                                                                                                |
| [Boolean](https://developer.mozilla.org/en-US/docs/Glossary/Boolean) | Este é um valor Verdadeiro/Falso. As palavras `true` e `false` são palavras-chave especiais que não precisam de aspas.                  | `let myVariable = true;`                                                                                              |
| [Array](https://developer.mozilla.org/en-US/docs/Glossary/Array)     | Esta é uma estrutura que permite armazenar vários valores em uma única referência.                                                      | `let myVariable = [1,'Bob','Steve',10];` Consulte cada membro da matriz assim: `myVariable[0]`, `myVariable[1]`, etc. |
| [Object](https://developer.mozilla.org/en-US/docs/Glossary/Object)   | Isso pode ser qualquer coisa. Tudo em JavaScript é um objeto e pode ser armazenado em uma variável. Tenha isso em mente ao aprender.    | `let myVariable = document.querySelector('h1');` Todos os exemplos acima também.                                      |

Então, por que precisamos de variáveis? As variáveis são necessárias para fazer qualquer coisa interessante em programação. Se os valores não pudessem mudar, você não poderia fazer nada dinâmico, como personalizar uma mensagem de saudação ou alterar uma imagem exibida em uma galeria de imagens.
