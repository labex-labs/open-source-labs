# Padrão de Fundo em Zigue-Zague

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um padrão de fundo em zigue-zague, use as seguintes etapas:

1.  Defina um fundo branco usando `background-color`.
2.  Crie as partes de um padrão em zigue-zague usando `background-image` com quatro valores `linear-gradient()`.
3.  Especifique o tamanho do padrão usando `background-size`.
4.  Posicione as partes do padrão nos locais corretos usando `background-position`.
5.  Para repetir o padrão, use `background-repeat`.
6.  **Nota:** A `height` (altura) e a `width` (largura) do elemento são fixas apenas para fins de demonstração.

Aqui está um trecho de código de exemplo:

```html
<div class="zig-zag"></div>
```

```css
.zig-zag {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(135deg, #000 25%, transparent 25%),
    linear-gradient(225deg, #000 25%, transparent 25%), linear-gradient(
      315deg,
      #000 25%,
      transparent 25%
    ), linear-gradient(45deg, #000 25%, transparent 25%);
  background-position:
    -30px 0,
    -30px 0,
    0 0,
    0 0;
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
