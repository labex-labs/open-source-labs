# はじめに

このチュートリアルでは、Matplotlib を使ってサンプルの経験的累積分布関数（ECDF：Empirical Cumulative Distribution Function）と理論的な CDF をプロットする方法を示します。ECDF は、工学において「超えない」曲線としても知られており、与えられた x 値に対する y 値は、サンプルからの観測値がその x 値未満である確率を表します。逆に、経験的な補完累積分布関数（ECCDF：Empirical Complementary Cumulative Distribution Function、または「超過」曲線）は、サンプルからの観測値が値 x を超える確率 y を示します。

## VM のヒント

VM の起動が完了したら、左上隅をクリックして**ノートブック**タブに切り替え、Jupyter Notebook を使って練習しましょう。

時々、Jupyter Notebook が読み込み終わるまで数秒待つ必要があります。Jupyter Notebook の制限により、操作の検証は自動化できません。

学習中に問題がある場合は、Labby にお問い合わせください。セッション後にフィードバックを提供してください。すぐに問題を解決いたします。
