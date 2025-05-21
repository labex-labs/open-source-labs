# Compreendendo a Representação de Strings em JavaScript

Antes de calcular o tamanho em bytes de strings, é importante entender como as strings são representadas em JavaScript.

Em JavaScript, strings são sequências de unidades de código UTF-16. Isso significa que caracteres como emojis ou certos símbolos podem levar mais de um byte para serem representados. Por exemplo, uma simples letra em inglês ocupa 1 byte, mas um emoji pode ocupar 4 bytes.

Vamos começar lançando o Node.js no terminal:

1.  Abra o Terminal clicando no ícone do terminal na interface WebIDE
2.  Digite o seguinte comando e pressione Enter:

```bash
node
```

Você deve estar agora no console interativo do Node.js, que se parece com isto:

```
Welcome to Node.js v14.x.x.
Type ".help" for more information.
>
```

![Abra o node](../assets/screenshot-20250306-cFJ9GgLX@2x.png)

Neste console, podemos experimentar o código JavaScript diretamente. Tente digitar o seguinte comando para ver o comprimento de uma string:

```javascript
"Hello World".length;
```

Você deve ver a saída:

```
11
```

Isso nos dá a contagem de caracteres, mas não o tamanho real em bytes. A contagem de caracteres e o tamanho em bytes podem ser diferentes, especialmente com caracteres especiais. Vamos explorar isso mais a fundo no próximo passo.
