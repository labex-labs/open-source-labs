# バイナリプロジェクトの関心事の分離

複数のタスクの責任を`main`関数に割り当てるという組織的な問題は、多くのバイナリプロジェクトに共通しています。その結果、Rust コミュニティは、`main`が大きくなり始めたときにバイナリプログラムの個別の関心事を分割するためのガイドラインを開発しました。このプロセスには次のステップがあります。

- プログラムを`main.rs`ファイルと`lib.rs`ファイルに分割し、プログラムのロジックを`lib.rs`に移動します。
- コマンドライン解析ロジックが小さければ、`main.rs`に残しておくことができます。
- コマンドライン解析ロジックが複雑になり始めたときに、それを`main.rs`から抽出して`lib.rs`に移動します。

このプロセスの後、`main`関数に残る責任は以下のものに限定されるはずです。

- 引数値でコマンドライン解析ロジックを呼び出すこと
- その他の設定を行うこと
- `lib.rs`内の`run`関数を呼び出すこと
- `run`がエラーを返した場合のエラー処理を行うこと

このパターンは関心事の分離に関するものです。`main.rs`はプログラムの実行を担当し、`lib.rs`は手元のタスクのすべてのロジックを担当します。`main`関数を直接テストすることができないため、この構造により、プログラムのすべてのロジックを`lib.rs`内の関数に移動することでテストすることができます。`main.rs`に残るコードは十分に小さく、読むことでその正しさを検証することができます。このプロセスに従ってプログラムを再構築しましょう。
