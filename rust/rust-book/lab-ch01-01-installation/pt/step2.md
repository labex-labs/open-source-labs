# Instalando o rustup no Linux ou macOS

Se você estiver usando Linux ou macOS, abra um terminal e insira o seguinte comando:

```bash
curl --proto '=https' --tlsv1.3 https://sh.rustup.rs -sSf | sh
```

O comando baixa um script e inicia a instalação da ferramenta `rustup`, que instala a versão estável mais recente do Rust. Você pode ser solicitado a inserir sua senha. Se a instalação for bem-sucedida, a seguinte linha aparecerá:

```rust
Rust is installed now. Great!
```

Você também precisará de um _linker_ (ligador), que é um programa que o Rust usa para juntar suas saídas compiladas em um único arquivo. É provável que você já tenha um. Se você receber erros de ligador, deverá instalar um compilador C, que normalmente incluirá um ligador. Um compilador C também é útil porque alguns pacotes Rust comuns dependem de código C e precisarão de um compilador C.

Usuários Linux geralmente devem instalar GCC ou Clang, de acordo com a documentação de sua distribuição. Por exemplo, se você usa Ubuntu, pode instalar o pacote `build-essential`.
