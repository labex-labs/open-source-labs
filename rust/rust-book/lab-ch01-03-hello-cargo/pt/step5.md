# Cargo como Convenção

Com projetos simples, o Cargo não oferece muito valor em comparação com o uso direto do `rustc`, mas provará seu valor à medida que seus programas se tornarem mais complexos. Uma vez que os programas crescem para múltiplos arquivos ou precisam de uma dependência, é muito mais fácil deixar o Cargo coordenar a construção.

Embora o projeto `hello_cargo` seja simples, ele agora usa grande parte das ferramentas reais que você usará no restante de sua carreira em Rust. Na verdade, para trabalhar em quaisquer projetos existentes, você pode usar os seguintes comandos para verificar o código usando o Git, mudar para o diretório desse projeto e construir:

```bash
git clone example.org/someproject
cd someproject
cargo build
```

Para mais informações sobre o Cargo, consulte sua documentação em *https://doc.rust-lang.org/cargo*.
