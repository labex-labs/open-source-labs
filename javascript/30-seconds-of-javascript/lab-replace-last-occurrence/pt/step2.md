# Implementando a Lógica da Função Principal

Agora que entendemos o problema, vamos implementar a funcionalidade principal da nossa função `replaceLast`. Vamos nos concentrar em lidar com padrões de string primeiro, e depois abordaremos expressões regulares na próxima etapa.

Quando o padrão é uma string, podemos usar o método `lastIndexOf` para encontrar a posição da última ocorrência. Uma vez que sabemos essa posição, podemos usar o método `slice` para reconstruir a string com a substituição inserida.

Atualize sua função `replaceLast` com a seguinte implementação:

```javascript
function replaceLast(str, pattern, replacement) {
  // Ensure inputs are valid
  if (typeof str !== "string") {
    return str;
  }

  if (typeof pattern === "string") {
    // Find the position of the last occurrence
    const lastIndex = str.lastIndexOf(pattern);

    // If pattern not found, return original string
    if (lastIndex === -1) {
      return str;
    }

    // Rebuild the string with the replacement
    const before = str.slice(0, lastIndex);
    const after = str.slice(lastIndex + pattern.length);
    return before + replacement + after;
  }

  // We'll handle regex patterns in the next step
  return str;
}
```

Atualize seus casos de teste para verificar se a função lida corretamente com padrões de string:

```javascript
// Test cases for string patterns
console.log(replaceLast("Hello world world", "world", "JavaScript")); // Should output: "Hello world JavaScript"
console.log(replaceLast("abcabcabc", "abc", "123")); // Should output: "abcabc123"
console.log(replaceLast("abcdef", "xyz", "123")); // Should output: "abcdef" (pattern not found)
```

Execute o código novamente para ver a saída atualizada:

```bash
node replaceLast.js
```

Você deve agora ver a última ocorrência do padrão de string substituída em cada caso de teste. Por exemplo, "Hello world JavaScript" em vez de "Hello world world".
