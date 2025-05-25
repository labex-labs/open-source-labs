# Hello, Cargo

Cargo é o sistema de construção e gerenciador de pacotes do Rust. A maioria dos Rustaceans usa esta ferramenta para gerenciar seus projetos Rust porque o Cargo lida com muitas tarefas para você, como construir seu código, baixar as bibliotecas das quais seu código depende e construir essas bibliotecas. (Chamamos as bibliotecas que seu código precisa de _dependências_.)

Os programas Rust mais simples, como o que escrevemos até agora, não têm nenhuma dependência. Se tivéssemos construído o projeto "Hello, world!" com o Cargo, ele usaria apenas a parte do Cargo que lida com a construção do seu código. À medida que você escreve programas Rust mais complexos, você adicionará dependências, e se você iniciar um projeto usando o Cargo, adicionar dependências será muito mais fácil de fazer.

Como a grande maioria dos projetos Rust usa o Cargo, o restante deste livro assume que você também está usando o Cargo. O Cargo vem instalado com o Rust se você usou os instaladores oficiais discutidos em "Instalação". Se você instalou o Rust por algum outro meio, verifique se o Cargo está instalado digitando o seguinte em seu terminal:

```bash
cargo --version
```

Se você vir um número de versão, você o tem! Se você vir um erro, como `command not found`, consulte a documentação do seu método de instalação para determinar como instalar o Cargo separadamente.
