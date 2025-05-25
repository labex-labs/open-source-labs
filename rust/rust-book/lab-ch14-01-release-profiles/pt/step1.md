# Customizando Builds com Perfis de Release

No Rust, _perfis de release_ são perfis predefinidos e personalizáveis com diferentes configurações que permitem ao programador ter mais controle sobre várias opções para compilar o código. Cada perfil é configurado independentemente dos outros.

O Cargo possui dois perfis principais: o perfil `dev` que o Cargo usa quando você executa `cargo build`, e o perfil `release` que o Cargo usa quando você executa `cargo build --release`. O perfil `dev` é definido com bons padrões para desenvolvimento, e o perfil `release` tem bons padrões para builds de release.

Esses nomes de perfil podem ser familiares na saída de seus builds:

```bash
$ cargo build
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
$ cargo build --release
    Finished release [optimized] target(s) in 0.0s
```

`dev` e `release` são esses diferentes perfis usados pelo compilador.

O Cargo possui configurações padrão para cada um dos perfis que se aplicam quando você não adicionou explicitamente nenhuma seção `[profile.*]` no arquivo `Cargo.toml` do projeto. Ao adicionar seções `[profile.*]` para qualquer perfil que você deseja personalizar, você substitui qualquer subconjunto das configurações padrão. Por exemplo, aqui estão os valores padrão para a configuração `opt-level` para os perfis `dev` e `release`:

Nome do arquivo: `Cargo.toml`

```tomltoml
[profile.dev]
opt-level = 0

[profile.release]
opt-level = 3
```

A configuração `opt-level` controla o número de otimizações que o Rust aplicará ao seu código, com uma faixa de 0 a 3. Aplicar mais otimizações estende o tempo de compilação, então, se você estiver em desenvolvimento e compilando seu código com frequência, você vai querer menos otimizações para compilar mais rápido, mesmo que o código resultante seja executado mais lentamente. O `opt-level` padrão para `dev` é, portanto, `0`. Quando você estiver pronto para lançar seu código, é melhor gastar mais tempo compilando. Você só compilará no modo release uma vez, mas executará o programa compilado muitas vezes, então o modo release troca um tempo de compilação mais longo por um código que roda mais rápido. É por isso que o `opt-level` padrão para o perfil `release` é `3`.

Você pode substituir uma configuração padrão adicionando um valor diferente para ela em `Cargo.toml`. Por exemplo, se quisermos usar o nível de otimização 1 no perfil de desenvolvimento, podemos adicionar estas duas linhas ao arquivo `Cargo.toml` do nosso projeto:

Nome do arquivo: `Cargo.toml`

```tomltoml
[profile.dev]
opt-level = 1
```

Este código substitui a configuração padrão de `0`. Agora, quando executarmos `cargo build`, o Cargo usará os padrões para o perfil `dev` mais nossa personalização para `opt-level`. Como definimos `opt-level` como `1`, o Cargo aplicará mais otimizações do que o padrão, mas não tantas quanto em um build de release.

Para obter a lista completa de opções de configuração e padrões para cada perfil, consulte a documentação do Cargo em *https://doc.rust-lang.org/cargo/reference/profiles.html*.
