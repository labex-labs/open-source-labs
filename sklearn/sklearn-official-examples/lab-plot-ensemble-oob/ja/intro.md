# はじめに

この実験では、Pythonのscikit - learnライブラリを使ってランダムフォレストモデルのアウトオブバッグ（OOB）エラー率を測定する方法を示します。OOBエラー率は、それぞれのブートストラップサンプルにその観測値を含まない木の予測値を使って計算される各訓練観測値の平均エラーです。これにより、ランダムフォレストモデルを訓練中にフィットさせて検証することができます。

## VMのヒント

VMの起動が完了したら、左上隅をクリックして**ノートブック**タブに切り替えて、Jupyter Notebookを使った練習にアクセスします。

時々、Jupyter Notebookが読み込み終了するまで数秒待つ必要があります。Jupyter Notebookの制限により、操作の検証を自動化することはできません。

学習中に問題に遭遇した場合は、Labbyにお問い合わせください。セッション後にフィードバックを提供してください。すぐに問題を解決いたします。
