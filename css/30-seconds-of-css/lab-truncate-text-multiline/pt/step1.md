# Truncar Texto Multilinha

`index.html` e `style.css` já foram fornecidos na VM.

Para truncar texto que é maior que uma linha, siga estes passos:

1.  Use `overflow: hidden` para evitar que o texto transborde suas dimensões.
2.  Defina uma `width` fixa de `400px` para garantir que o elemento tenha pelo menos uma dimensão constante.
3.  Defina `height: 109.2px` calculado a partir do `font-size`, usando a fórmula `font-size * line-height * numberOfLines` (neste caso, `26 * 1.4 * 3 = 109.2`).
4.  Adicione a classe `truncate-text-multiline` ao elemento `p` no seu HTML.
5.  Defina `font-size: 26px` e `line-height: 1.4` no CSS para a classe `.truncate-text-multiline`.
6.  Defina `color: #333` e `background: #f5f6f9` para estilizar o texto.
7.  Para criar um gradiente de `transparent` para o `background-color`, adicione as seguintes regras CSS ao pseudo-elemento `.truncate-text-multiline::after`:

```css
.truncate-text-multiline::after {
  content: "";
  position: absolute;
  bottom: 0;
  right: 0;
  width: 150px;
  height: 36.4px;
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #f5f6f9 50%);
}
```

Isso criará um contêiner de gradiente com uma altura de `36.4px`, calculado para o contêiner de gradiente, com base na fórmula `font-size * line-height` (neste caso, `26 * 1.4 = 36.4`). O pseudo-elemento `::after` é posicionado no canto inferior direito do elemento `.truncate-text-multiline`.

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
