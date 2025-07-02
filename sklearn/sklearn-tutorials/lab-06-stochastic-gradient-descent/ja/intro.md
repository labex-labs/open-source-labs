# はじめに

確率的勾配降下法（Stochastic Gradient Descent, SGD）は、機械学習でよく使われる最適化アルゴリズムです。これは、各反復で訓練データのランダムに選択されたサブセットを使用する勾配降下法のバリエーションです。このため、計算効率が良く、大規模なデータセットの処理に適しています。この実験（Lab）では、scikit-learn を使用して Python で SGD を実装する手順を説明します。

## VM のヒント

VM の起動が完了したら、左上隅をクリックして **Notebook** タブに切り替え、Jupyter Notebook を開いて練習を行ってください。

場合によっては、Jupyter Notebook の読み込みが完了するまで数秒待つ必要があります。Jupyter Notebook の制限により、操作の検証を自動化することはできません。

学習中に問題が発生した場合は、Labby に質問してください。セッション終了後にフィードバックを提供していただければ、迅速に問題を解決します。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
これは Guided Lab です。学習と実践を支援するためのステップバイステップの指示を提供します。各ステップを完了し、実践的な経験を積むために、指示に注意深く従ってください。過去のデータによると、この <span class="text-green-600 dark:text-green-400">初級</span> レベルの実験の完了率は <span class="text-green-600 dark:text-green-400">82%</span>です。学習者から <span class="text-primary-600 dark:text-primary-400">100%</span> の好評価を得ています。
</div>
