# Testando com Diferentes Tipos de Strings

Vamos explorar como diferentes tipos de caracteres afetam o tamanho em bytes de uma string.

No console do Node.js, vamos testar nossa função `byteSize` com várias strings:

1.  Texto em inglês simples:

```javascript
byteSize("The quick brown fox jumps over the lazy dog");
```

Saída esperada:

```
43
```

2.  Números e caracteres especiais:

```javascript
byteSize("123!@#$%^&*()");
```

Saída esperada:

```
13
```

3.  Uma mistura de caracteres ASCII e não-ASCII:

```javascript
byteSize("Hello, 世界！");
```

Saída esperada:

```
13
```

4.  Múltiplos emojis:

```javascript
byteSize("😀😃😄😁");
```

Saída esperada:

```
16
```

Observe que com os tipos de caracteres mistos, especialmente com caracteres não-ASCII como caracteres chineses e emojis, o tamanho em bytes é maior do que a contagem de caracteres.

Isso é importante para entender ao trabalhar com dados que podem conter caracteres internacionais ou símbolos especiais, pois afeta os requisitos de armazenamento e os tamanhos de transferência de dados.

Vamos sair do console do Node.js digitando:

```javascript
.exit
```

Isso o retornará ao prompt normal do terminal.
