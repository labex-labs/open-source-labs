# はじめに

このチュートリアルでは、Matplotlibを使ってサンプルの経験的累積分布関数（ECDF：Empirical Cumulative Distribution Function）と理論的なCDFをプロットする方法を示します。ECDFは、工学において「超えない」曲線としても知られており、与えられたx値に対するy値は、サンプルからの観測値がそのx値未満である確率を表します。逆に、経験的な補完累積分布関数（ECCDF：Empirical Complementary Cumulative Distribution Function、または「超過」曲線）は、サンプルからの観測値が値xを超える確率yを示します。

## VMのヒント

VMの起動が完了したら、左上隅をクリックして**ノートブック**タブに切り替え、Jupyter Notebookを使って練習しましょう。

時々、Jupyter Notebookが読み込み終わるまで数秒待つ必要があります。Jupyter Notebookの制限により、操作の検証は自動化できません。

学習中に問題がある場合は、Labbyにお問い合わせください。セッション後にフィードバックを提供してください。すぐに問題を解決いたします。
