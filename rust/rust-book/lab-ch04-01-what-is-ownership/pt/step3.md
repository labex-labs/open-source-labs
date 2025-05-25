# Escopo de Variáveis

Agora que já passamos pela sintaxe básica do Rust, não incluiremos todo o código `fn main() {` nos exemplos, então, se você estiver acompanhando, certifique-se de colocar os exemplos a seguir dentro de uma função `main` manualmente. Como resultado, nossos exemplos serão um pouco mais concisos, permitindo-nos focar nos detalhes reais em vez do código _boilerplate_ (código repetitivo).

Como um primeiro exemplo de _ownership_, vamos analisar o _escopo_ de algumas variáveis. Um escopo é o intervalo dentro de um programa para o qual um item é válido. Considere a seguinte variável:

```rust
let s = "hello";
```

A variável `s` se refere a um literal de _string_ (cadeia de caracteres), onde o valor da _string_ é codificado no texto do nosso programa. A variável é válida a partir do ponto em que é declarada até o final do _escopo_ atual. A Listagem 4-1 mostra um programa com comentários anotando onde a variável `s` seria válida.

    {                      // s não é válido aqui, pois ainda não foi declarado
        let s = "hello";   // s é válido a partir deste ponto

        // faça algo com s
    }                      // este escopo acabou, e s não é mais válido

Listagem 4-1: Uma variável e o escopo em que ela é válida

Em outras palavras, existem dois pontos importantes no tempo aqui:

- Quando `s` _entra_ no escopo, ele é válido.
- Ele permanece válido até que _saia_ do escopo.

Neste ponto, a relação entre escopos e quando as variáveis são válidas é semelhante à de outras linguagens de programação. Agora, construiremos sobre essa compreensão introduzindo o tipo `String`.
