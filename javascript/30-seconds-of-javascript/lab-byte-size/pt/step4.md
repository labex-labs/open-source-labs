# Criando um Arquivo de Exemplo Prático

Agora, vamos criar um arquivo JavaScript para implementar nossa função de tamanho em bytes de uma forma mais prática. Isso demonstrará como você pode usar essa função em uma aplicação do mundo real.

1.  Crie um novo arquivo no WebIDE. Clique no ícone "Novo Arquivo" na barra lateral do explorador de arquivos e nomeie-o `byteSizeCalculator.js`.

2.  Adicione o seguinte código ao arquivo:

```javascript
/**
 * Calcula o tamanho em bytes de uma determinada string.
 * @param {string} str - A string para calcular o tamanho em bytes.
 * @returns {number} O tamanho em bytes.
 */
function calculateByteSize(str) {
  return new Blob([str]).size;
}

// Exemplos com diferentes tipos de strings
const examples = [
  "Hello World",
  "😀",
  "The quick brown fox jumps over the lazy dog",
  "123!@#$%^&*()",
  "Hello, 世界！",
  "😀😃😄😁"
];

// Exibe os resultados
console.log("Calculadora de Tamanho em Bytes de String\n");
console.log("String".padEnd(45) + "| Caracteres | Bytes");
console.log("-".repeat(70));

examples.forEach((example) => {
  console.log(
    `"${example}"`.padEnd(45) +
      `| ${example.length}`.padEnd(12) +
      `| ${calculateByteSize(example)}`
  );
});
```

3.  Salve o arquivo pressionando Ctrl+S ou selecionando Arquivo > Salvar no menu.

4.  Execute o arquivo a partir do terminal:

```bash
node byteSizeCalculator.js
```

Você deve ver uma saída semelhante a esta:

```
Calculadora de Tamanho em Bytes de String

String                                      | Caracteres | Bytes
----------------------------------------------------------------------
"Hello World"                               | 11         | 11
"😀"                                        | 1          | 4
"The quick brown fox jumps over the lazy dog" | 43         | 43
"123!@#$%^&*()"                            | 13         | 13
"Hello, 世界!"                              | 10         | 13
"😀😃😄😁"                                  | 4          | 16
```

Esta tabela mostra claramente a diferença entre a contagem de caracteres e o tamanho em bytes para diferentes tipos de strings.

Compreender essas diferenças é crucial ao:

- Definir limites na entrada do usuário em formulários da web
- Calcular os requisitos de armazenamento para dados de texto
- Trabalhar com APIs que têm limitações de tamanho
- Otimizar a transferência de dados em redes
