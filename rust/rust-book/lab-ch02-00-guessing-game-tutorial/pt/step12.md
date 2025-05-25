# Atualizando um Crate para Obter uma Nova Versão

Quando você _quiser_ atualizar um crate, o Cargo fornece o comando `update`, que ignorará o arquivo _Cargo.lock_ e descobrirá todas as versões mais recentes que se encaixam em suas especificações em `Cargo.toml`. O Cargo então escreverá essas versões no arquivo _Cargo.lock_. Caso contrário, por padrão, o Cargo só procurará versões maiores que 0.8.5 e menores que 0.9.0. Se o crate `rand` lançou as duas novas versões 0.8.6 e 0.9.0, você veria o seguinte se executasse `cargo update`:

```bash
$ cargo update
Updating crates.io index
Updating rand v0.8.5 - > v0.8.6
```

O Cargo ignora o lançamento 0.9.0. Neste ponto, você também notaria uma mudança em seu arquivo _Cargo.lock_ observando que a versão do crate `rand` que você está usando agora é 0.8.6. Para usar a versão 0.9.0 do `rand` ou qualquer versão da série 0.9.\_x\_, você teria que atualizar o arquivo `Cargo.toml` para que se parecesse com isto:

```rust
[dependencies]
rand = "0.9.0"
```

Na próxima vez que você executar `cargo build`, o Cargo atualizará o registro de crates disponíveis e reavaliará seus requisitos de `rand` de acordo com a nova versão que você especificou.

Há muito mais a dizer sobre o Cargo e seu ecossistema, que discutiremos no Capítulo 14, mas por enquanto, isso é tudo o que você precisa saber. O Cargo torna muito fácil reutilizar bibliotecas, então os Rustaceans são capazes de escrever projetos menores que são montados a partir de vários pacotes.
