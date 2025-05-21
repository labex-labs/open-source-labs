# Implementando a Função de Diferença de Data Usando Arrow Functions

Agora que entendemos como calcular diferenças de data, vamos implementar uma versão mais concisa de nossa função usando arrow functions.

## Arrow Functions em JavaScript

Arrow functions fornecem uma sintaxe mais curta para escrever funções em JavaScript. Veja como podemos reescrever nossa função de diferença de data usando a sintaxe de arrow function:

```javascript
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;
```

Esta função faz exatamente a mesma coisa que nossa função anterior, mas com uma sintaxe mais limpa e concisa.

## Criando um Arquivo JavaScript

Vamos criar um arquivo JavaScript para armazenar e testar nossa função. Saia do ambiente Node.js pressionando Ctrl+D ou digitando `.exit` e pressionando Enter.

Agora, crie um novo arquivo chamado `dateDifference.js` na WebIDE:

1.  Clique no ícone "Explorer" na barra lateral esquerda
2.  Clique com o botão direito no explorador de arquivos e selecione "New File" (Novo Arquivo)
3.  Nomeie o arquivo `dateDifference.js` e pressione Enter
4.  Adicione o seguinte código ao arquivo:

```javascript
// Função para calcular a diferença entre duas datas em segundos
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;

// Exemplos de teste
console.log("Example 1:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:15"),
    new Date("2020-12-24 00:00:17")
  )
); // Saída esperada: 2

console.log("\nExample 2:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:00"),
    new Date("2020-12-24 00:01:00")
  )
); // Saída esperada: 60

console.log("\nExample 3:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:00"),
    new Date("2020-12-24 01:00:00")
  )
); // Saída esperada: 3600
```

Salve o arquivo pressionando Ctrl+S ou clicando em File > Save (Arquivo > Salvar).

## Executando o Arquivo JavaScript

Para executar o arquivo que acabamos de criar, use o seguinte comando no terminal:

```bash
node dateDifference.js
```

Você deve ver a seguinte saída:

```
Example 1:
2

Example 2:
60

Example 3:
3600
```

Isso confirma que nossa função está funcionando corretamente:

- Primeiro exemplo: A diferença entre 00:00:15 e 00:00:17 é 2 segundos
- Segundo exemplo: A diferença entre 00:00:00 e 00:01:00 é 60 segundos (1 minuto)
- Terceiro exemplo: A diferença entre 00:00:00 e 01:00:00 é 3600 segundos (1 hora)
