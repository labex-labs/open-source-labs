# はじめに

この実験では、scikit-learn の線形モデルを調べます。線形モデルは、回帰と分類タスクに使用される一連の手法です。これらのモデルは、目的変数が特徴量の線形結合であると仮定しています。これらのモデルは、単純さと解釈可能性のため、機械学習で広く使用されています。

以下のトピックを扱います。

- 最小二乗法
- リッジ回帰
- Lasso
- ロジスティック回帰
- 確率的勾配降下法
- パーセプトロン

> 機械学習の経験がない場合は、[教師あり学習：回帰](https://labex.io/courses/supervised-learning-regression)から始めてください。

## VM のヒント

VM の起動が完了したら、左上隅をクリックして **ノートブック** タブに切り替え、Jupyter Notebook を使って練習しましょう。

Jupyter Notebook の読み込みには数秒かかる場合があります。Jupyter Notebook の制限により、操作の検証は自動化できません。

学習中に問題がある場合は、Labby にお問い合わせください。セッション後にフィードバックを提供してください。すぐに問題を解決いたします。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
これは Guided Lab です。学習と実践を支援するためのステップバイステップの指示を提供します。各ステップを完了し、実践的な経験を積むために、指示に注意深く従ってください。過去のデータによると、この <span class="text-orange-600 dark:text-orange-400">中級</span> レベルの実験の完了率は <span class="text-orange-600 dark:text-orange-400">57.85%</span>です。学習者から <span class="text-primary-600 dark:text-primary-400">94%</span> の好評価を得ています。
</div>
