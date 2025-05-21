# Usando Blob para Calcular o Tamanho em Bytes de uma String

Agora que entendemos a representação de strings, vamos aprender como calcular o tamanho real em bytes de uma string usando o objeto `Blob`.

Um `Blob` (Binary Large Object) representa um objeto semelhante a um arquivo de dados brutos e imutáveis. Ao converter nossa string em um Blob, podemos acessar sua propriedade `size` para determinar o tamanho em bytes.

No console do Node.js, vamos criar uma função para calcular o tamanho em bytes:

```javascript
const byteSize = (str) => new Blob([str]).size;
```

Esta função recebe uma string como entrada, a converte em um Blob e retorna seu tamanho em bytes.

Vamos testar esta função com um exemplo simples:

```javascript
byteSize("Hello World");
```

Você deve ver a saída:

```
11
```

Neste caso, a contagem de caracteres e o tamanho em bytes são os mesmos porque "Hello World" contém apenas caracteres ASCII, cada um representado por um único byte.

Agora vamos tentar com um caractere não-ASCII:

```javascript
byteSize("😀");
```

Você deve ver a saída:

```
4
```

Isso mostra que, embora o emoji apareça como um único caractere, ele realmente ocupa 4 bytes de armazenamento.
