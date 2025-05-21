# Criando uma Função para Validar Strings de Data Formatadas em ISO

Nesta etapa, criaremos uma função JavaScript que verifica se uma determinada string está em formato ISO 8601 válido.

## Criando a Função de Validação

Vamos criar um novo arquivo JavaScript para nosso validador de data ISO:

1. No WebIDE, clique no ícone Explorer na barra lateral esquerda
2. Clique com o botão direito no explorador de arquivos e selecione "Novo Arquivo"
3. Nomeie o arquivo `isISODate.js` e pressione Enter
4. Adicione o seguinte código ao arquivo:

```javascript
/**
 * Checks if a string is a valid ISO 8601 formatted date string
 * @param {string} val - The string to check
 * @return {boolean} - Returns true if the string is in ISO format, false otherwise
 */
const isISOString = (val) => {
  // Create a Date object from the input string
  const d = new Date(val);

  // Check if the date is valid (not NaN) and if the ISO string matches the original
  return !Number.isNaN(d.valueOf()) && d.toISOString() === val;
};

// Export the function so we can use it elsewhere
module.exports = isISOString;
```

Vamos examinar como esta função funciona:

1. `new Date(val)` cria um objeto Date a partir da string de entrada
2. `d.valueOf()` retorna o valor numérico do timestamp (milissegundos desde 1º de janeiro de 1970)
3. `Number.isNaN(d.valueOf())` verifica se a data é inválida (NaN significa "Not a Number")
4. `d.toISOString() === val` verifica se a conversão da Date de volta para uma string ISO corresponde à entrada original

## Testando Nossa Função

Agora, vamos criar um arquivo de teste simples para testar nossa função:

1. Crie outro arquivo chamado `testISO.js`
2. Adicione o seguinte código:

```javascript
// Import our isISOString function
const isISOString = require("./isISODate");

// Test with a valid ISO formatted date
console.log("Testing a valid ISO date:");
console.log("2020-10-12T10:10:10.000Z");
console.log("Result:", isISOString("2020-10-12T10:10:10.000Z"));
console.log();

// Test with an invalid format
console.log("Testing a non-ISO date:");
console.log("2020-10-12");
console.log("Result:", isISOString("2020-10-12"));
```

3. Execute o arquivo de teste usando Node.js:

```bash
node testISO.js
```

Você deve ver uma saída semelhante a:

```
Testing a valid ISO date:
2020-10-12T10:10:10.000Z
Result: true

Testing a non-ISO date:
2020-10-12
Result: false
```

Isso mostra que nossa função identifica corretamente que "2020-10-12T10:10:10.000Z" é uma data formatada em ISO válida, enquanto "2020-10-12" não é.
