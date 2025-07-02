# はじめに

この実験では、機械学習において大規模かつ疎な問題を解くために一般的に使用される強力な最適化アルゴリズムである確率的勾配降下法（Stochastic Gradient Descent：SGD）を検討します。scikit-learn ライブラリの SGDClassifier と SGDRegressor クラスを使用して線形分類器と回帰器を訓練する方法を学びます。

## VM のヒント

VM の起動が完了したら、左上隅をクリックして**ノートブック**タブに切り替え、Jupyter Notebook を使って練習しましょう。

Jupyter Notebook の読み込みには数秒かかる場合があります。Jupyter Notebook の制限により、操作の検証を自動化することはできません。

学習中に問題がある場合は、Labby にお問い合わせください。セッション後にフィードバックを提供してください。すぐに問題を解決いたします。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
これは Guided Lab です。学習と実践を支援するためのステップバイステップの指示を提供します。各ステップを完了し、実践的な経験を積むために、指示に注意深く従ってください。過去のデータによると、この <span class="text-green-600 dark:text-green-400">初級</span> レベルの実験の完了率は <span class="text-green-600 dark:text-green-400">92%</span>です。学習者から <span class="text-primary-600 dark:text-primary-400">86%</span> の好評価を得ています。
</div>
