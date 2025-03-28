# はじめに

この実験では、投票回帰器を使って患者の糖尿病の進行を予測します。データの予測には、勾配ブースティング回帰器、ランダムフォレスト回帰器、線形回帰の3つの異なる回帰器を使います。そして、上記の3つの回帰器を投票回帰器に使用します。最後に、すべてのモデルによって行われた予測をプロットして比較します。

糖尿病患者のコホートから収集された10個の特徴から構成される糖尿病データセットを使用します。目的は、ベースラインから1年後の病気の進行の定量的な測定です。

## VMのヒント

VMの起動が完了したら、左上隅をクリックして**ノートブック**タブに切り替えて、Jupyter Notebookを使って練習します。

時々、Jupyter Notebookが読み込み終了するまで数秒待つ必要があります。Jupyter Notebookの制限により、操作の検証は自動化できません。

学習中に問題に直面した場合は、Labbyにお問い合わせください。セッション後にフィードバックを提供してください。すぐに問題を解決いたします。
