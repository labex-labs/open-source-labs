# Separador de Formas

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um elemento separador entre dois blocos diferentes usando uma forma SVG, siga estes passos:

1. Use o pseudo-elemento `::after`.
2. Adicione a forma SVG (um triângulo de 24x12) via um data URI usando a propriedade `background-image`. A imagem de fundo irá repetir por padrão e cobrir toda a área do pseudo-elemento.
3. Defina a cor desejada para o separador usando a propriedade `background` do elemento pai.

Use o seguinte código HTML:

```html
<div class="shape-separator"></div>
```

E aplique as seguintes regras CSS:

```css
.shape-separator {
  position: relative;
  height: 48px;
  background: #9c27b0;
}

.shape-separator::after {
  content: "";
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 12'%3E%3Cpath d='m12 0l12 12h-24z' fill='transparent'/%3E%3C/svg%3E");
  position: absolute;
  width: 100%;
  height: 12px;
  bottom: 0;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
