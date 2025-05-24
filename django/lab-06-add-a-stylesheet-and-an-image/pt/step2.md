# Adicionando uma imagem de fundo

Em seguida, criaremos um subdiretório para imagens. Crie um subdiretório `images` no diretório `polls/static/polls/`. Dentro deste diretório, adicione qualquer arquivo de imagem que você gostaria de usar como fundo. Para os propósitos deste tutorial, estamos usando um arquivo chamado `background.png`, que você pode encontrar no diretório `/tmp/background.png` na VM.

Você precisa copiar o `/tmp/background.png` para `polls/static/polls/images/background.png`.

Em seguida, adicione uma referência à sua imagem em sua folha de estilo (`polls/static/polls/style.css`):

```css
body {
  background: white url("images/background.png") no-repeat;
}
```

Recarregue a aba **Web 8080** e você deverá ver o fundo carregado no canto superior esquerdo da tela.

![background image example](../assets/20230908-15-39-41-8dGms0NM.png)

> A tag de template `{% static %}` não está disponível para uso em arquivos estáticos que não são gerados pelo Django, como sua folha de estilo. Você sempre deve usar **caminhos relativos** para vincular seus arquivos estáticos entre si, porque então você pode alterar `STATIC_URL` (usado pela tag de template `static` para gerar suas URLs) sem ter que modificar um monte de caminhos em seus arquivos estáticos também.

Estes são os **básicos**. Para mais detalhes sobre configurações e outros bits incluídos com o framework, consulte `o howto de arquivos estáticos </howto/static-files/index>` e `a referência de arquivos estáticos </ref/contrib/staticfiles>`. `Implantando arquivos estáticos </howto/static-files/deployment>` discute como usar arquivos estáticos em um servidor real.

Quando você estiver confortável com os arquivos estáticos, leia **Personalizando o Site de Administração do Django** para aprender como personalizar o site de administração gerado automaticamente pelo Django.
