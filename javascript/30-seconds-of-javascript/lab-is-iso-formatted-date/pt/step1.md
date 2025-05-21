# Compreendendo o Formato de Data ISO e Objetos Date do JavaScript

Antes de começarmos a codificar, vamos entender o que é o formato de data ISO 8601 e como o JavaScript lida com datas.

## O Formato de Data ISO 8601

O formato ISO 8601 é um padrão internacional para representar datas e horas. O formato ISO estendido simplificado se parece com isto:

```
YYYY-MM-DDTHH:mm:ss.sssZ
```

Onde:

- `YYYY` representa o ano (quatro dígitos)
- `MM` representa o mês (dois dígitos)
- `DD` representa o dia (dois dígitos)
- `T` é um caractere literal que separa a data e a hora
- `HH` representa as horas (dois dígitos)
- `mm` representa os minutos (dois dígitos)
- `ss` representa os segundos (dois dígitos)
- `sss` representa os milissegundos (três dígitos)
- `Z` indica o fuso horário UTC (Tempo Zulu)

Por exemplo, `2023-05-12T14:30:15.123Z` representa 12 de maio de 2023, às 14:30:15.123 UTC.

## O Objeto Date do JavaScript

O JavaScript fornece um objeto `Date` embutido para trabalhar com datas e horas. Quando você cria um novo objeto `Date`, pode passar uma string formatada em ISO para ele:

```javascript
const date = new Date("2023-05-12T14:30:15.123Z");
```

Vamos abrir o terminal e praticar o trabalho com objetos Date:

1. Abra o Terminal clicando no menu Terminal na parte superior do WebIDE
2. Digite `node` e pressione Enter para iniciar o shell interativo do Node.js
3. Crie um novo objeto Date para a hora atual:

```javascript
const now = new Date();
console.log(now);
```

![node-prompt](../assets/screenshot-20250306-odDaT5Rp@2x.png)

4. Converta este objeto Date em uma string ISO:

```javascript
const isoString = now.toISOString();
console.log(isoString);
```

Você deve ver uma saída semelhante a:

```
2023-05-12T14:30:15.123Z
```

5. Crie uma Date a partir de uma string ISO:

```javascript
const dateFromIso = new Date("2023-05-12T14:30:15.123Z");
console.log(dateFromIso);
```

![node-prompt](../assets/screenshot-20250306-dbkCLkf7@2x.png)

Isso demonstra como o JavaScript pode analisar e criar objetos Date a partir de strings formatadas em ISO.
