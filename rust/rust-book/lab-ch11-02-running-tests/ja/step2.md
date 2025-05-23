# 並列または連続でテストを実行する

複数のテストを実行する場合、既定ではスレッドを使って並列に実行されます。つまり、実行が早く終了し、より速くフィードバックを得られます。テストが同時に実行されるため、テスト同士や、共有状態（現在の作業ディレクトリや環境変数などの共有環境を含む）に依存しないようにする必要があります。

たとえば、各テストがディスク上に _test-output.txt_ という名前のファイルを作成し、そのファイルにデータを書き込むコードを実行するとします。そして各テストはそのファイルのデータを読み取り、そのファイルに特定の値が含まれていることをアサートします。この値は各テストで異なります。テストが同時に実行されるため、あるテストが別のテストが書き込んだ後、読み取るまでの間にファイルを上書きする可能性があります。そうすると、2 番目のテストは失敗します。コードが誤っているわけではなく、並列実行中にテスト同士が干渉したためです。1 つの解決策は、各テストが別のファイルに書き込むようにすることです。もう 1 つの解決策は、テストを 1 つずつ実行することです。

並列でテストを実行したくない場合や、使用するスレッド数をより細かく制御したい場合、`--test-threads` フラグと使用したいスレッド数をテストバイナリに渡すことができます。次の例を見てください。

```bash
cargo test -- --test-threads=1
```

テストスレッド数を `1` に設定しています。これにより、プログラムに並列処理を使わないように指示しています。1 つのスレッドを使ってテストを実行すると、並列で実行するよりも時間がかかりますが、共有状態を持つ場合でもテスト同士が干渉しなくなります。
