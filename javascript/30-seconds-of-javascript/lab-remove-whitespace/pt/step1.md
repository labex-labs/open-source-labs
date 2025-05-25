# Função para Remover Espaços em Branco

Para remover espaços em branco de uma string, use a seguinte função.

- Use `String.prototype.replace()` com uma expressão regular para substituir todas as ocorrências de caracteres de espaço em branco por uma string vazia.

```js
const removeWhitespace = (str) => str.replace(/\s+/g, "");
```

## Explicação da Expressão Regular

- `/\s+/g` se decompõe em:
  - `\s`: Corresponde a qualquer caractere de espaço em branco (espaços, tabs, quebras de linha)
  - `+`: Corresponde a uma ou mais ocorrências do caractere anterior
  - `/g`: Flag global - corresponde a todas as ocorrências na string, não apenas a primeira

## Referência Rápida de Regex

Padrões comuns de espaço em branco:

- `\s` - corresponde a qualquer espaço em branco (espaço, tab, nova linha)
- `\t` - corresponde a caracteres de tabulação
- `\n` - corresponde a caracteres de nova linha
- `\r` - corresponde a retornos de carro
- `` (espaço) - corresponde apenas a caracteres de espaço

Por exemplo,

```js
removeWhitespace("Lorem ipsum.\n Dolor sit amet. ");
// 'Loremipsum.Dolorsitamet.'

// Mais exemplos:
removeWhitespace("Hello    World"); // "HelloWorld"
removeWhitespace("Tab\there\nNew line"); // "TabhereNewline"
```

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.
