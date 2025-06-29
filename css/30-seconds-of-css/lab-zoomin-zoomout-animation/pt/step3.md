# Criando a Animação Keyframes

As animações CSS funcionam definindo keyframes (quadros-chave) que especificam os estilos que um elemento deve ter em vários pontos durante a sequência de animação. Vamos criar os keyframes para nossa animação de zoom in zoom out.

1. Abra o arquivo `style.css` novamente e adicione o seguinte código no final:

```css
@keyframes zoom-in-zoom-out {
  0% {
    transform: scale(1, 1);
  }
  50% {
    transform: scale(1.5, 1.5);
  }
  100% {
    transform: scale(1, 1);
  }
}
```

2. Vamos entender o que este código faz:
   - `@keyframes` é uma at-rule (regra at) CSS que define os estágios e estilos de uma animação
   - `zoom-in-zoom-out` é o nome que damos à nossa animação (faremos referência a este nome mais tarde)
   - Dentro dos keyframes, definimos o que acontece em diferentes pontos da animação:
     - Em `0%` (o início), o elemento está em seu tamanho normal com `scale(1, 1)`
     - Em `50%` (no meio do caminho), o elemento cresce para 1,5 vezes seu tamanho com `scale(1.5, 1.5)`
     - Em `100%` (o fim), o elemento retorna ao seu tamanho normal
   - A propriedade `transform` com a função `scale()` altera o tamanho do elemento

3. Salve o arquivo `style.css` após adicionar esses keyframes.

Os keyframes definem o que nossa animação fará, mas ainda não a aplicamos ao nosso elemento. Na próxima etapa, conectaremos a animação à nossa caixa.
