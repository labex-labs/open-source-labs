# Criando um Módulo Reutilizável

Agora que temos funções funcionando, vamos criar um arquivo de módulo JavaScript reutilizável que podemos importar em outros projetos.

Primeiro, vamos sair do shell interativo do Node.js pressionando Ctrl+C duas vezes ou digitando `.exit` e pressionando Enter.

Agora, crie um novo arquivo chamado `object-utils.js` no diretório do projeto:

1. No WebIDE, navegue até o painel do explorador de arquivos à esquerda
2. Clique com o botão direito no diretório do projeto e selecione "Novo Arquivo"
3. Nomeie o arquivo `object-utils.js`
4. Adicione o seguinte código ao arquivo:

```javascript
/**
 * Converts all keys of an object to lowercase
 * @param {Object} obj - The input object
 * @returns {Object} A new object with all keys in lowercase
 */
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};

/**
 * Recursively converts all keys of an object and its nested objects to lowercase
 * @param {Object} obj - The input object
 * @returns {Object} A new object with all keys in lowercase (including nested objects)
 */
const deepLowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    const value = obj[key];
    // Check if the value is an object and not null
    const newValue =
      value && typeof value === "object" && !Array.isArray(value)
        ? deepLowerizeKeys(value)
        : value;

    acc[key.toLowerCase()] = newValue;
    return acc;
  }, {});
};

// Export the functions
module.exports = {
  lowerizeKeys,
  deepLowerizeKeys
};
```

Agora, vamos criar um arquivo de teste para verificar se nosso módulo funciona corretamente. Crie um novo arquivo chamado `test.js`:

1. No WebIDE, navegue até o painel do explorador de arquivos à esquerda
2. Clique com o botão direito no diretório do projeto e selecione "Novo Arquivo"
3. Nomeie o arquivo `test.js`
4. Adicione o seguinte código ao arquivo:

```javascript
// Import the functions from our module
const { lowerizeKeys, deepLowerizeKeys } = require("./object-utils");

// Test with a simple object
const user = {
  Name: "John",
  AGE: 30,
  Email: "john@example.com"
};

console.log("Original object:");
console.log(user);

console.log("\nObject with lowercase keys:");
console.log(lowerizeKeys(user));

// Test with a nested object
const nestedObject = {
  User: {
    Name: "John",
    Contact: {
      EMAIL: "john@example.com",
      PHONE: "123-456-7890"
    }
  }
};

console.log("\nNested object:");
console.log(nestedObject);

console.log("\nNested object with lowercase keys (shallow):");
console.log(lowerizeKeys(nestedObject));

console.log("\nNested object with lowercase keys (deep):");
console.log(deepLowerizeKeys(nestedObject));
```

Agora, vamos executar o arquivo de teste:

```bash
node test.js
```

Você deve ver uma saída semelhante a:

```
Original object:
{ Name: 'John', AGE: 30, Email: 'john@example.com' }

Object with lowercase keys:
{ name: 'John', age: 30, email: 'john@example.com' }

Nested object:
{
  User: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Nested object with lowercase keys (shallow):
{
  user: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Nested object with lowercase keys (deep):
{
  user: {
    name: 'John',
    contact: { email: 'john@example.com', phone: '123-456-7890' }
  }
}
```

Parabéns! Você criou com sucesso um módulo JavaScript reutilizável com funções para converter chaves de objeto para minúsculas. Este módulo agora pode ser importado em qualquer um de seus projetos JavaScript.
