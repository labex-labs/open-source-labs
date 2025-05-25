# Construindo para Release

Quando seu projeto estiver finalmente pronto para lançamento (release), você pode usar `cargo build --release` para compilá-lo com otimizações.

```bash
cargo build --release
```

Este comando criará um executável em `target/release` em vez de `target/debug`. As otimizações fazem com que seu código Rust seja executado mais rapidamente, mas ativá-las aumenta o tempo que leva para seu programa compilar. É por isso que existem dois perfis diferentes: um para desenvolvimento, quando você deseja reconstruir de forma rápida e frequente, e outro para construir o programa final que você dará a um usuário que não será reconstruído repetidamente e que será executado o mais rápido possível. Se você estiver fazendo benchmarking do tempo de execução do seu código, certifique-se de executar `cargo build --release` e fazer o benchmarking com o executável em `target/release`.
