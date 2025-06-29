# Compreendendo o Problema e Configurando

Antes de começarmos a codificar, vamos entender o que nossa função `replaceLast` deve fazer:

1. Aceitar três parâmetros:
   - `str`: A string de entrada a ser modificada
   - `pattern`: A substring ou expressão regular a ser pesquisada
   - `replacement`: A string para substituir a última ocorrência

2. Retornar uma nova string com a última ocorrência do padrão substituída.

Vamos criar um arquivo JavaScript para implementar nossa função:

1. Navegue até o diretório do projeto no explorador de arquivos do WebIDE.
2. Crie um novo arquivo chamado `replaceLast.js` no diretório `replace-last`.
3. Adicione a seguinte estrutura básica ao arquivo:

```javascript
// Function to replace the last occurrence of a pattern in a string
function replaceLast(str, pattern, replacement) {
  // Our implementation will go here
  return str;
}

// We will add test cases here later
```

Para verificar se tudo está configurado corretamente, vamos adicionar um teste simples:

```javascript
// Example usage
console.log(replaceLast("Hello world world", "world", "JavaScript"));
```

Agora, vamos executar nosso código para ver a saída atual:

1. Abra o Terminal no WebIDE
2. Navegue até o diretório `replace-last`:
   ```bash
   cd ~/project/replace-last
   ```
3. Execute o arquivo JavaScript usando Node.js:
   ```bash
   node replaceLast.js
   ```

Você deve ver `Hello world world` na saída porque nossa função atualmente apenas retorna a string original sem fazer nenhuma alteração.
