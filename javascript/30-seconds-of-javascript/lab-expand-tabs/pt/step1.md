# Como Converter Tabulações em Espaços em JavaScript

Para converter caracteres de tabulação em espaços ao codificar, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `String.prototype.replace()` com uma expressão regular e `String.prototype.repeat()` para substituir cada caractere de tabulação pelo número desejado de espaços.
3.  O trecho de código abaixo mostra como usar a função `expandTabs` para substituir tabulações por espaços:

```js
const expandTabs = (str, count) => str.replace(/\t/g, " ".repeat(count));

expandTabs("\t\tlorem", 3); // '      lorem'
```

No exemplo acima, a função `expandTabs` recebe dois argumentos: uma string `str` que contém tabulações e um número `count` que representa o número de espaços para substituir cada caractere de tabulação. A função usa o método `String.prototype.replace()` com uma expressão regular (`/\t/g`) para encontrar todos os caracteres de tabulação na string de entrada e substituí-los pelo número desejado de espaços usando o método `String.prototype.repeat()`.
