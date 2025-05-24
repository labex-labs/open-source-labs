# Fallback (Alternativa) para Imagens que Falham ao Carregar

`index.html` e `style.css` já foram fornecidos na VM (Máquina Virtual).

Quando uma imagem falha ao carregar, exiba uma mensagem de erro para o usuário. Para fazer isso, aplique estilos ao elemento `img` como se fosse um contêiner de texto, definindo seu `display` para `block` e sua `width` para 100%. Use os pseudo-elementos `::before` e `::after` para exibir, respectivamente, a mensagem de erro e a URL da imagem. Esses elementos serão exibidos somente se a imagem falhar ao carregar.

Aqui está um exemplo de trecho de código:

```html
<img src="https://nowhere.to.be/found.jpg" />
```

```css
img {
  display: block;
  width: 100%;
  height: auto;
  line-height: 2;
  position: relative;
  text-align: center;
  font-family: sans-serif;
  font-weight: 300;
}

img::before {
  content: "Sorry, this image is unavailable.";
  display: block;
  margin-bottom: 8px;
}

img::after {
  content: "(url: " attr(src) ")";
  display: block;
  font-size: 12px;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
