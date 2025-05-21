# Compreendendo Pascal Case e Configurando o Ambiente

Pascal case é uma convenção de nomenclatura onde:

- A primeira letra de cada palavra é capitalizada
- Não são usados espaços, hífens ou underscores entre as palavras
- Todas as outras letras são minúsculas

Por exemplo:

- "hello world" → "HelloWorld"
- "user_name" → "UserName"
- "first-name" → "FirstName"

Vamos começar configurando nosso ambiente de desenvolvimento.

1. Abra o Terminal da interface WebIDE clicando em "Terminal" na barra de menu superior.

2. Inicie uma sessão interativa do Node.js digitando o seguinte comando no Terminal e pressionando Enter:

```bash
node
```

Você deve ver o prompt do Node.js (`>`) aparecer, indicando que você está agora no ambiente interativo do Node.js.

3. Vamos tentar uma manipulação simples de string para aquecer. Digite o seguinte código no prompt do Node.js:

```javascript
let name = "john doe";
let capitalizedFirstLetter = name.charAt(0).toUpperCase() + name.slice(1);
console.log(capitalizedFirstLetter);
```

A saída deve ser:

```
John doe
```

Este exemplo simples demonstra como capitalizar a primeira letra de uma string. Usamos:

- `charAt(0)` para obter o primeiro caractere
- `toUpperCase()` para convertê-lo para maiúsculas
- `slice(1)` para obter o restante da string
- Concatenação com `+` para combiná-los

Esses métodos de string serão úteis à medida que construímos nosso conversor para Pascal case.
