# Condicionais

> Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

Condicionais são estruturas de código usadas para testar se uma expressão retorna verdadeiro (true) ou não. Uma forma muito comum de condicionais é a declaração `if...else`. Por exemplo:

```js
let iceCream = "chocolate";
if (iceCream === "chocolate") {
  console.log("Yay, I love chocolate ice cream!");
} else {
  console.log("Awwww, but chocolate is my favorite…");
}
```

A expressão dentro do `if ()` é o teste. Isso usa o operador de igualdade estrita (strict equality operator), como descrito acima, para comparar a variável `iceCream` com a string `chocolate` para ver se as duas são iguais. Se esta comparação retornar `true`, o primeiro bloco de código é executado. Se a comparação não for verdadeira, o segundo bloco de código — após a declaração `else` — é executado em vez disso.
