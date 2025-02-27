# Creating a Constructor for Config

До сих пор мы извлекли логику, отвечающую за разбор аргументов командной строки из `main` и поместили ее в функцию `parse_config`. Это помогло нам понять, что значения `query` и `file_path` связаны, и эта связь должна быть передана в нашем коде. Затем мы добавили структуру `Config`, чтобы дать имена связанным целям `query` и `file_path` и чтобы иметь возможность возвращать имена значений в виде имен полей структуры из функции `parse_config`.

Так что теперь цель функции `parse_config` — создать экземпляр `Config`, мы можем изменить `parse_config` из простой функции в функцию с именем `new`, которая будет связана с структурой `Config`. Это изменение сделает код более идиоматичным. Мы можем создавать экземпляры типов из стандартной библиотеки, таких как `String`, вызывая `String::new`. Аналогично, заменив `parse_config` на функцию `new`, связанную с `Config`, мы сможем создавать экземпляры `Config`, вызывая `Config::new`. Listing 12-7 показывает изменения, которые нам нужно сделать.

Filename: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

  1 let config = Config::new(&args);

    --snip--
}

--snip--

2 impl Config {
  3 fn new(args: &[String]) -> Config {
        let query = args[1].clone();
        let file_path = args[2].clone();

        Config { query, file_path }
    }
}
```

Listing 12-7: Changing `parse_config` into `Config::new`

Мы обновили `main`, где мы вызывали `parse_config`, и заменили вызов на `Config::new` \[1\]. Мы изменили имя `parse_config` на `new` \[3\] и переместили его внутри блока `impl` \[2\], который связывает функцию `new` с `Config`. Попробуйте скомпилировать этот код снова, чтобы убедиться, что он работает.
