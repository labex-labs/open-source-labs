# まとめ

Signals 実験では、チャネルを使って Go プログラムで Unix シグナルを扱う方法を示します。`os.Signal` の通知を受け取るためのバッファ付きチャネルを作成し、`signal.Notify` を使って指定されたシグナルの通知を受け取るようにチャネルを登録することで、期待されるシグナルを受け取ったときにシグナルを円滑に処理してプログラムを終了することができます。
