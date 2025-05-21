# Criando uma Aplicação Prática

Agora que temos uma função funcional para calcular a diferença entre datas em segundos, vamos criar uma aplicação mais prática. Vamos construir um cronômetro simples que calcula quanto tempo se passou desde que o iniciamos.

## Criando uma Aplicação de Cronômetro

Crie um novo arquivo chamado `timer.js` na WebIDE:

1.  Clique no ícone "Explorer" na barra lateral esquerda
2.  Clique com o botão direito no explorador de arquivos e selecione "New File" (Novo Arquivo)
3.  Nomeie o arquivo `timer.js` e pressione Enter
4.  Adicione o seguinte código ao arquivo:

```javascript
// Função para calcular a diferença entre duas datas em segundos
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;

// Tempo de início - quando o script começa a ser executado
const startTime = new Date();
console.log(`Cronômetro iniciado em: ${startTime.toLocaleTimeString()}`);

// Função para atualizar e exibir o tempo decorrido
function updateTimer() {
  const currentTime = new Date();
  const elapsedSeconds = getSecondsDiffBetweenDates(startTime, currentTime);

  // Formata o tempo como horas:minutos:segundos
  const hours = Math.floor(elapsedSeconds / 3600);
  const minutes = Math.floor((elapsedSeconds % 3600) / 60);
  const seconds = Math.floor(elapsedSeconds % 60);

  const formattedTime = `${hours.toString().padStart(2, "0")}:${minutes
    .toString()
    .padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;

  // Limpa o console e exibe o tempo atualizado
  console.clear();
  console.log(`Cronômetro iniciado em: ${startTime.toLocaleTimeString()}`);
  console.log(`Tempo decorrido: ${formattedTime}`);
}

// Atualiza o cronômetro a cada segundo
console.log("Cronômetro em execução... Pressione Ctrl+C para parar.");
const timerInterval = setInterval(updateTimer, 1000);

// Mantém o script em execução
setTimeout(() => {
  clearInterval(timerInterval);
  console.log("\nCronômetro parado após 1 minuto.");
}, 60000); // Executa por 1 minuto
```

Salve o arquivo pressionando Ctrl+S ou clicando em File > Save (Arquivo > Salvar).

## Executando a Aplicação de Cronômetro

Para executar a aplicação de cronômetro, use o seguinte comando no terminal:

```bash
node timer.js
```

O cronômetro iniciará e atualizará a cada segundo, mostrando quanto tempo se passou desde que foi iniciado. O cronômetro parará automaticamente após 1 minuto, ou você pode pará-lo antes pressionando Ctrl+C.

## Compreendendo a Aplicação de Cronômetro

Vamos detalhar como a aplicação de cronômetro funciona:

1.  Definimos a função `getSecondsDiffBetweenDates` para calcular a diferença de tempo em segundos.
2.  Registramos o tempo de início quando o script começa a ser executado.
3.  Definimos uma função `updateTimer` que:
    - Obtém o tempo atual
    - Calcula quantos segundos se passaram desde o tempo de início
    - Formata o tempo decorrido como horas:minutos:segundos
    - Exibe o tempo formatado
4.  Usamos `setInterval` para executar a função `updateTimer` a cada 1000 milissegundos (1 segundo).
5.  Usamos `setTimeout` para parar o cronômetro após 60000 milissegundos (1 minuto).

Esta aplicação demonstra um uso prático de nossa função de diferença de data para criar um cronômetro em tempo real.
