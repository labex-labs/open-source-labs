# match のアーム

第 6 章で説明したように、`match` 式のアームでパターンを使用します。形式的には、`match` 式はキーワード `match`、照合対象の値、および 1 つ以上のマッチ アームで構成されます。マッチ アームは、パターンと、値がそのアームのパターンに一致した場合に実行する式です。次のようになります。

    match VALUE {
        PATTERN => EXPRESSION,
        PATTERN => EXPRESSION,
        PATTERN => EXPRESSION,
    }

たとえば、次はリスト 6-5 の `match` 式で、変数 `x` の `Option<i32>` 値を照合しています。

    match x {
        None => None,
        Some(i) => Some(i + 1),
    }

この `match` 式のパターンは、各矢印の左側の `None` と `Some(i)` です。

`match` 式の要件の 1 つは、`match` 式の値のすべての可能性を網羅するという意味で、網羅的である必要があることです。すべての可能性を網羅したことを確認する 1 つの方法は、最後のアームに catchall パターンを持つことです。たとえば、任意の値と一致する変数名は失敗することがないため、残りのすべてのケースを網羅します。

特定のパターン `_` は何でも一致しますが、変数にバインドすることはありません。したがって、最後のマッチ アームでよく使用されます。たとえば、指定されていない値を無視したい場合、`_` パターンは便利です。「パターン内の値の無視」で `_` パターンについて詳しく説明します。
