# 統合テスト

Rust では、統合テストはライブラリの完全に外部にあります。それらは他のコードと同じ方法でライブラリを使用します。つまり、ライブラリのパブリック API の一部である関数のみを呼び出すことができます。その目的は、ライブラリの多くの部分が正しく一緒に機能するかどうかをテストすることです。個別には正しく機能するコードのユニットは、統合された場合に問題が発生する可能性があるため、統合されたコードのテストカバレッジも重要です。統合テストを作成するには、まず `tests` ディレクトリが必要です。
