# Começando com Objetos Date do JavaScript

O JavaScript fornece um objeto `Date` embutido que nos permite trabalhar com datas e horas. Antes de calcularmos a diferença entre datas, vamos primeiro entender como criar e trabalhar com objetos Date em JavaScript.

## Iniciando o Ambiente Node.js

Vamos começar abrindo o ambiente interativo Node.js:

1.  Abra o Terminal clicando no menu Terminal na parte superior da WebIDE
2.  Digite o seguinte comando e pressione Enter:

```bash
node
```

Você deve ver o prompt do Node.js (`>`), indicando que você está no ambiente interativo do JavaScript. Isso permite que você execute código JavaScript diretamente no terminal.

![node-prompt](../assets/screenshot-20250306-328ScUbO@2x.png)

## Criando Objetos Date

No JavaScript, podemos criar um novo objeto Date de várias maneiras:

```javascript
// Data e hora atuais
let now = new Date();
console.log(now);

// Data e hora específicas (ano, mês [0-11], dia, hora, minuto, segundo)
let specificDate = new Date(2023, 0, 15, 10, 30, 45); // 15 de janeiro de 2023, 10:30:45
console.log(specificDate);

// Data a partir de uma string
let dateFromString = new Date("2023-01-15T10:30:45");
console.log(dateFromString);
```

Tente digitar cada um desses exemplos no ambiente Node.js e observe a saída.

Observe que no JavaScript, os meses são indexados a partir de zero, o que significa que janeiro é 0, fevereiro é 1 e assim por diante.

## Obtendo Timestamp de Objetos Date

Cada objeto Date no JavaScript armazena internamente o tempo como o número de milissegundos que se passaram desde 1º de janeiro de 1970 (UTC). Isso é conhecido como um timestamp.

```javascript
let now = new Date();
console.log(now.getTime()); // Obtém o timestamp em milissegundos
```

Este timestamp será útil para calcular a diferença entre datas.
