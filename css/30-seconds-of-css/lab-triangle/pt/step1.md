# Triângulo

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma forma triangular com CSS puro, siga estes passos:

1. Use três bordas com a mesma `border-width` (`20px`) para criar a forma do triângulo.
2. Defina a `border-color` do lado oposto de onde o triângulo aponta para a cor desejada. As bordas adjacentes devem ter uma `border-color` de `transparent`.
3. Para ajustar o tamanho do triângulo, altere os valores de `border-width`.

Aqui está um exemplo de trecho de código:

```html
<div class="triangle"></div>
```

```css
.triangle {
  width: 0;
  height: 0;
  border-top: 20px solid #9c27b0;
  border-left: 20px solid transparent;
  border-right: 20px solid transparent;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
