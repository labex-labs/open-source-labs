# Aplicando a Animação

Agora que definimos nossos keyframes, precisamos aplicar a animação ao nosso elemento de caixa.

1. Abra o arquivo `style.css` novamente e modifique o seletor `.zoom-in-out-box` da seguinte forma:

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 1s ease infinite;
}
```

2. Vamos entender a propriedade `animation` que adicionamos:

   - `animation` é uma propriedade abreviada (shorthand property) que define múltiplas propriedades de animação de uma vez
   - `zoom-in-zoom-out` é o nome da nossa animação de keyframes
   - `1s` especifica que um ciclo da animação dura 1 segundo
   - `ease` é a função de temporização (timing function) que faz com que a animação comece lentamente, acelere e depois desacelere novamente
   - `infinite` significa que a animação se repetirá para sempre

3. Salve o arquivo `style.css` após fazer essas alterações.

4. Se o servidor web já estiver em execução, simplesmente atualize a aba **Web 8080**. Caso contrário, clique em "Go Live" no canto inferior direito para iniciar o servidor e, em seguida, abra a aba **Web 8080**.

Você deve ver agora seu quadrado rosa aumentando e diminuindo suavemente em uma animação contínua. O quadrado cresce até atingir 1,5 vezes seu tamanho original e, em seguida, encolhe de volta ao normal. Este ciclo se repete infinitamente.
