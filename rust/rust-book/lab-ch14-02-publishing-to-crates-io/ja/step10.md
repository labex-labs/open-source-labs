# 既存のクレートの新しいバージョンを公開する

クレートに変更を加え、新しいバージョンをリリースする準備ができたら、`Cargo.toml` ファイルで指定されている `version` 値を変更して再公開します。*http://semver.org* のセマンティック バージョニング規則を使用して、行った変更の種類に基づいて、次に適切なバージョン番号を決定します。そして、新しいバージョンをアップロードするために `cargo publish` を実行します。
