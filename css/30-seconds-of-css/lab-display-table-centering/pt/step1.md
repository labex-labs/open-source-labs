# Centralização com Display Table

`index.html` e `style.css` já foram fornecidos na VM.

Para centralizar um elemento filho tanto verticalmente quanto horizontalmente dentro de seu elemento pai, siga estes passos:

1. Adicione um elemento container com `height` e `width` fixos.

```html
<div class="container"></div>
```

2. Adicione o elemento filho dentro do elemento container e dê a ele a classe `.center`.

```html
  <div class="center"><span>Conteúdo centralizado</span></div>
</div>
```

3. No CSS, aplique os seguintes estilos ao elemento container:

- Defina `height` e `width` para os valores fixos desejados.
- Adicione uma borda (opcional).

```css
.container {
  border: 1px solid #9c27b0;
  height: 250px;
  width: 250px;
}
```

4. No CSS, aplique os seguintes estilos ao elemento filho:

- Use `display: table` para fazer com que o elemento `.center` se comporte como um elemento `<table>`.
- Defina `height` e `width` para `100%` para fazer com que o elemento preencha o espaço disponível dentro de seu elemento pai.
- Use `display: table-cell` no elemento filho para fazê-lo se comportar como um elemento `<td>`.
- Use `text-align: center` e `vertical-align: middle` no elemento filho para centralizá-lo horizontalmente e verticalmente.

```css
.center {
  display: table;
  height: 100%;
  width: 100%;
}

.center > span {
  display: table-cell;
  text-align: center;
  vertical-align: middle;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
