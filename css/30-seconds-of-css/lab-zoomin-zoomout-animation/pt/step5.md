# Experimentando com Propriedades de Animação

Vamos personalizar nossa animação experimentando diferentes propriedades de animação. Isso ajudará você a entender como essas propriedades afetam o comportamento da animação.

1. Abra o arquivo `style.css` e modifique o seletor `.zoom-in-out-box` para testar diferentes propriedades de animação:

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 2s ease-in-out infinite;
  /* Add a slight rotation during the animation */
  border-radius: 10px;
}
```

2. Vamos entender o que mudamos:
   - Estendemos a duração da animação para `2s` (2 segundos)
   - Mudamos a função de temporização para `ease-in-out`, o que torna o início e o fim da animação suaves
   - Adicionamos um `border-radius` de 10px para arredondar os cantos da nossa caixa

3. Vamos também modificar nossos keyframes para adicionar um efeito de rotação:

```css
@keyframes zoom-in-zoom-out {
  0% {
    transform: scale(1, 1) rotate(0deg);
  }
  50% {
    transform: scale(1.5, 1.5) rotate(45deg);
    background-color: #2196f3;
  }
  100% {
    transform: scale(1, 1) rotate(0deg);
  }
}
```

4. Nesta definição de keyframes atualizada:
   - Adicionamos uma função `rotate()` à propriedade transform
   - Na marca de 50%, o elemento agora gira 45 graus enquanto aumenta a escala
   - Também mudamos a cor de fundo para azul na marca de 50%

5. Salve o arquivo `style.css` após fazer essas alterações.

6. Atualize a aba **Web 8080** para ver sua animação aprimorada.

Sua animação agora deve ser mais lenta (2 segundos por ciclo), ter cantos arredondados, girar enquanto aumenta o zoom e mudar de cor no meio da animação. Isso demonstra como as animações CSS podem combinar múltiplas mudanças de propriedade para efeitos visuais ricos.

Sinta-se à vontade para experimentar mais com diferentes propriedades e valores para ver como eles afetam sua animação.
