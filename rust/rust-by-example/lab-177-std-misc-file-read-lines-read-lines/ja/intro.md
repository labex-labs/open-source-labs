# はじめに

この実験では、Rust でファイルから行を読み取るための単純な実装と、より効率的な実装が与えられます。単純なアプローチでは、`read_to_string` を使ってファイルを 1 つの文字列に読み込み、その後にそれを行に分割します。一方、より効率的なアプローチでは、`BufReader` を使ってファイルを 1 行ずつ読み取り、全体の内容をメモリに読み込まないようにします。

> **注：** 実験でファイル名が指定されていない場合、好きなファイル名を使うことができます。たとえば、`main.rs` を使って、`rustc main.rs &&./main` でコンパイルして実行することができます。
