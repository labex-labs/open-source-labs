# Padrão de Fundo de Bolinhas (Polka Dot)

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um padrão de fundo de bolinhas (polka dot), você pode seguir estes passos:

1.  Defina a propriedade `background-color` para preto.
2.  Use a propriedade `background-image` com dois valores `radial-gradient()` para criar duas bolinhas.
3.  Especifique o tamanho do padrão usando a propriedade `background-size`. Use `background-position` para posicionar adequadamente os dois gradientes.
4.  Defina `background-repeat` para `repeat`.
5.  Observe que a `height` e `width` fixas do elemento são apenas para fins de demonstração.

Aqui está um exemplo de código HTML para um elemento div com a classe `polka-dot`:

```html
<div class="polka-dot"></div>
```

E aqui está o código CSS correspondente:

```css
.polka-dot {
  width: 240px;
  height: 240px;
  background-color: #000;
  background-image:
    radial-gradient(#fff 10%, transparent 11%),
    radial-gradient(#fff 10%, transparent 11%);
  background-size: 60px 60px;
  background-position:
    0 0,
    30px 30px;
  background-repeat: repeat;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
