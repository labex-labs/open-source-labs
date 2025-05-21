# Trabalhando com Expressões Regulares para Separação de Palavras

Para converter uma string para Pascal case, o primeiro passo é dividir a string em palavras individuais. Podemos usar expressões regulares (regex) para identificar limites de palavras, independentemente do delimitador usado (espaços, hífens, underscores, etc.).

Em JavaScript, as expressões regulares são delimitadas por barras (`/pattern/`). Vamos explorar como usar regex para dividir uma string em palavras.

1. Em sua sessão do Node.js, vamos tentar um exemplo simples primeiro. Digite o seguinte código:

```javascript
let str = "hello_world-example";
let words = str.split(/[-_]/);
console.log(words);
```

A saída deve ser:

```
[ 'hello', 'world', 'example' ]
```

Esta regex `/[-_]/` corresponde a um hífen ou um underscore, e `split()` usa essas correspondências como separadores.

2. Agora, vamos tentar uma string e regex mais complexas. Digite:

```javascript
let complexStr = "hello_WORLD-example phrase";
let regex =
  /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g;
let matches = complexStr.match(regex);
console.log(matches);
```

A saída deve ser:

```
[ 'hello', 'WORLD', 'example', 'phrase' ]
```

Vamos detalhar esta regex:

- `/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)/`: Corresponde a sequências de letras maiúsculas
- `/[A-Z]?[a-z]+[0-9]*/`: Corresponde a palavras que podem começar com uma letra maiúscula
- `/[A-Z]/`: Corresponde a letras maiúsculas únicas
- `/[0-9]+/`: Corresponde a sequências de números
- A flag `g` torna a correspondência global (encontra todas as correspondências)

O método `match()` retorna um array de todas as correspondências encontradas na string. Isso será essencial para nosso conversor para Pascal case, pois ele pode identificar palavras em quase qualquer formato.
