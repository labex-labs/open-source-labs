# Funções (Functions)

> `index.html` já foi fornecido na VM.

[Funções (Functions)](https://developer.mozilla.org/en-US/docs/Glossary/Function) são uma forma de empacotar funcionalidades que você deseja reutilizar. É possível definir um corpo de código como uma função que é executada quando você chama o nome da função em seu código. Esta é uma boa alternativa para escrever repetidamente o mesmo código. Você já viu alguns usos de funções.

Por exemplo:

```js
let myVariable = document.querySelector("h1");
```

```js
alert("hello!");
```

Essas funções, `document.querySelector` e `alert`, são embutidas no navegador.

> Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.

Se você vir algo que se parece com um nome de variável, mas é seguido por parênteses — `()` — é provável que seja uma função. Funções frequentemente recebem [argumentos (arguments)](https://developer.mozilla.org/en-US/docs/Glossary/Argument): pedaços de dados que elas precisam para fazer seu trabalho. Argumentos vão dentro dos parênteses, separados por vírgulas se houver mais de um argumento.

Por exemplo, a função `alert()` faz uma caixa pop-up aparecer dentro da janela do navegador, mas precisamos fornecer a ela uma string como argumento para dizer à função qual mensagem exibir.

Você também pode definir suas próprias funções.

No próximo exemplo, criamos uma função simples que recebe dois números como argumentos e os multiplica:

> Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

```js
function multiply(num1, num2) {
  let result = num1 * num2;
  return result;
}
```

Tente executar isso no console; então teste com vários argumentos. Por exemplo:

```js
multiply(4, 7);
multiply(20, 20);
multiply(0.5, 3);
```

> **Nota:** A declaração [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return) diz ao navegador para retornar a variável `result` da função para que ela esteja disponível para uso. Isso é necessário porque as variáveis definidas dentro das funções estão disponíveis apenas dentro dessas funções. Isso é chamado de escopo de variável (variable scoping). (Leia mais sobre [escopo de variável (variable scoping)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variable_scope).)
