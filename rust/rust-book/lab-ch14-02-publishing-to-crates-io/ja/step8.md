# 新しいクレートにメタデータを追加する

公開したいクレートがあるとしましょう。公開する前に、クレートの `Cargo.toml` ファイルの `[package]` セクションにいくつかのメタデータを追加する必要があります。

クレートには一意の名前が必要です。ローカルでクレートを開発している間は、好きな名前を付けることができます。ただし、*https://crates.io* 上のクレート名は、先着順で割り当てられます。クレート名が既に使われている場合、他の誰もその名前でクレートを公開することはできません。クレートを公開しようとする前に、使用したい名前を検索してください。名前が既に使われている場合は、別の名前を見つけて、`[package]` セクションの下の `Cargo.toml` ファイルの `name` フィールドを編集して、公開に使用する新しい名前に変更します。次のようになります。

ファイル名：`Cargo.toml`

```tomlrust
[package]
name = "guessing_game"
```

一意の名前を選んだ場合でも、この時点で `cargo publish` を実行してクレートを公開すると、警告が表示され、その後エラーが表示されます。

```bash
$ cargo publish
    Updating crates.io index
warning: manifest has no description, license, license-file, documentation,
homepage or repository.
See https://doc.rust-lang.org/cargo/reference/manifest.html#package-metadata
for more info.
--snip--
error: failed to publish to registry at https://crates.io

Caused by:
  the remote server responded with an error: missing or empty metadata fields:
description, license. Please see https://doc.rust-
lang.org/cargo/reference/manifest.html for how to upload metadata
```

これがエラーになるのは、重要な情報が不足しているためです。クレートが何を行うか、そしてどの条件で使用できるかを知るためには、説明とライセンスが必要です。`Cargo.toml` では、検索結果にクレートと一緒に表示されるため、1、2 文の説明を追加します。`license` フィールドでは、_ライセンス識別子値_ を指定する必要があります。*http://spdx.org/licenses* の Linux Foundation の Software Package Data Exchange (SPDX) では、この値に使用できる識別子が一覧されています。たとえば、クレートを MIT ライセンスでライセンス付けしたことを指定するには、`MIT` 識別子を追加します。

ファイル名：`Cargo.toml`

```toml
[package]
name = "guessing_game"
license = "MIT"
```

SPDX に表示されていないライセンスを使用したい場合は、そのライセンスのテキストをファイルに置き、プロジェクトにそのファイルを含め、その後 `license-file` を使用してそのファイル名を指定して、`license` キーを使用しないようにします。

あなたのプロジェクトに適したライセンスに関するガイダンスは、この本の範囲外です。Rust コミュニティの多くの人は、`MIT OR Apache-2.0` のデュアルライセンスを使用することで、Rust と同じように彼らのプロジェクトをライセンス付けています。この慣行は、プロジェクトに複数のライセンスを持たせるために、`OR` で区切られた複数のライセンス識別子を指定することもできることを示しています。

一意の名前、バージョン、説明、およびライセンスが追加された状態で、公開準備ができているプロジェクトの `Cargo.toml` ファイルは、次のようになるかもしれません。

ファイル名：`Cargo.toml`

```toml
[package]
name = "guessing_game"
version = "0.1.0"
edition = "2021"
description = "A fun game where you guess what number the
computer has chosen."
license = "MIT OR Apache-2.0"

[dependencies]
```

*https://doc.rust-lang.org/cargo* の Cargo のドキュメントでは、他の人があなたのクレートをより簡単に見つけて使用できるようにするために指定できる他のメタデータについて説明されています。
