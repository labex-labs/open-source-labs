# Dependendo de um Pacote Externo em um Workspace

Observe que o workspace tem apenas um arquivo _Cargo.lock_ no nível superior, em vez de ter um _Cargo.lock_ no diretório de cada crate. Isso garante que todos os crates estejam usando a mesma versão de todas as dependências. Se adicionarmos o pacote `rand` aos arquivos _adder/Cargo.toml_ e _add_one/Cargo.toml_, o Cargo resolverá ambos para uma versão de `rand` e registrará isso no único _Cargo.lock_. Fazer com que todos os crates no workspace usem as mesmas dependências significa que os crates sempre serão compatíveis entre si. Vamos adicionar o crate `rand` à seção `[dependencies]` no arquivo _add_one/Cargo.toml_ para que possamos usar o crate `rand` no crate `add_one`:

Nome do arquivo: `add_one/Cargo.toml`

```tomlrust
[dependencies]
rand = "0.8.5"
```

Agora podemos adicionar `use rand;` ao arquivo `add_one/src/lib.rs`, e construir todo o workspace executando `cargo build` no diretório `add` trará e compilará o crate `rand`. Receberemos um aviso porque não estamos nos referindo ao `rand` que trouxemos para o escopo:

```bash
$ cargo build
    Updating crates.io index
  Downloaded rand v0.8.5
   --snip--
   Compiling rand v0.8.5
   Compiling add_one v0.1.0 (file:///projects/add/add_one)
   Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished dev [unoptimized + debuginfo] target(s) in 10.18s
```

O _Cargo.lock_ de nível superior agora contém informações sobre a dependência de `add_one` em `rand`. No entanto, embora `rand` seja usado em algum lugar no workspace, não podemos usá-lo em outros crates no workspace, a menos que adicionemos `rand` aos seus arquivos `Cargo.toml` também. Por exemplo, se adicionarmos `use rand;` ao arquivo `adder/src/main.rs` para o pacote `adder`, receberemos um erro:

```bash
$ cargo build
   --snip--
   Compiling adder v0.1.0 (file:///projects/add/adder)
error[E0432]: unresolved import `rand`
 --> adder/src/main.rs:2:5
  |
2 | use rand;
  |     ^^^^ no external crate `rand`
```

Para corrigir isso, edite o arquivo `Cargo.toml` para o pacote `adder` e indique que `rand` também é uma dependência para ele. Construir o pacote `adder` adicionará `rand` à lista de dependências para `adder` em _Cargo.lock_, mas nenhuma cópia adicional de `rand` será baixada. O Cargo garantiu que cada crate em cada pacote no workspace que usa o pacote `rand` estará usando a mesma versão, economizando espaço e garantindo que os crates no workspace sejam compatíveis entre si.
