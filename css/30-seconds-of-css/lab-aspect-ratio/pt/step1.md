# Proporção (Aspect Ratio)

`index.html` e `style.css` já foram fornecidos na VM.

Este código cria um container responsivo com uma proporção específica usando propriedades customizadas CSS e a função `calc()`. Siga estes passos para conseguir isso:

1.  Defina a proporção desejada usando uma propriedade customizada CSS, `--aspect-ratio`.
2.  Defina a propriedade `position` do elemento container para `relative` e sua propriedade `height` para `0`.
3.  Calcule a altura do elemento container usando a função `calc()` e a propriedade customizada `--aspect-ratio`, e defina-a como a propriedade `padding-bottom`.
4.  Defina o filho direto do elemento container para `position: absolute`, `top: 0`, `left: 0`, `width: 100%` e `height: 100%`.
5.  Mantenha a proporção do elemento filho definindo sua propriedade `object-fit` para `cover`.

Use o seguinte código HTML e CSS para criar o container:

```html
<div class="container">
  <img src="https://picsum.photos/id/119/800/450" />
</div>
```

```css
.container {
  --aspect-ratio: 16/9;
  position: relative;
  height: 0;
  padding-bottom: calc(100% / var(--aspect-ratio));
}

.container > * {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
