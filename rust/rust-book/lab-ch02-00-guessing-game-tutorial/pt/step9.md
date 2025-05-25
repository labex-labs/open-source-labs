# Gerando um Número Secreto

Em seguida, precisamos gerar um número secreto que o usuário tentará adivinhar. O número secreto deve ser diferente a cada vez para que o jogo seja divertido de jogar mais de uma vez. Usaremos um número aleatório entre 1 e 100 para que o jogo não seja muito difícil. O Rust ainda não inclui a funcionalidade de número aleatório em sua biblioteca padrão. No entanto, a equipe Rust fornece um crate `rand` em *https://crates.io/crates/rand* com essa funcionalidade.
