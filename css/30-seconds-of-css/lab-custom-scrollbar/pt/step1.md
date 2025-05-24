# Barra de Rolagem Personalizada

`index.html` e `style.css` já foram fornecidos na VM.

Para personalizar o estilo da barra de rolagem para elementos com overflow rolável, você pode usar `::-webkit-scrollbar` para estilizar o elemento da barra de rolagem, `::-webkit-scrollbar-track` para estilizar a trilha (track) da barra de rolagem (o fundo da barra de rolagem) e `::-webkit-scrollbar-thumb` para estilizar o indicador (thumb) da barra de rolagem (o elemento arrastável). No entanto, observe que esta técnica só funciona em navegadores baseados em WebKit, e a estilização da barra de rolagem não está em nenhuma trilha de padrões. Aqui está um exemplo de como usar esses seletores em HTML e CSS:

```html
<div class="custom-scrollbar">
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit?
  </p>
</div>
```

```css
.custom-scrollbar {
  height: 70px;
  overflow-y: scroll;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 8px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #1e3f20;
  border-radius: 12px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #4a7856;
  border-radius: 12px;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
