# Compreendendo Objetos em JavaScript

Antes de começarmos a converter as chaves de objetos para minúsculas, vamos entender o que são objetos JavaScript e como podemos trabalhar com eles.

Em JavaScript, um objeto é uma coleção de pares chave-valor. As chaves são strings (ou Symbols), e os valores podem ser de qualquer tipo de dado, incluindo outros objetos.

Vamos começar abrindo o shell interativo do Node.js:

1. Abra o terminal no seu WebIDE
2. Digite `node` e pressione Enter

Você deve agora ver o prompt do Node.js (`>`), que permite que você digite código JavaScript diretamente.

Vamos criar um objeto simples com chaves em caixa mista:

```javascript
const user = {
  Name: "John",
  AGE: 30,
  Email: "john@example.com"
};
```

Digite este código no prompt do Node.js e pressione Enter. Para ver o objeto, simplesmente digite `user` e pressione Enter:

```javascript
user;
```

Você deve ver a saída:

```
{ Name: 'John', AGE: 30, Email: 'john@example.com' }
```

Como você pode ver, este objeto tem chaves com diferentes estilos de capitalização. No próximo passo, aprenderemos como acessar essas chaves e convertê-las para minúsculas.
