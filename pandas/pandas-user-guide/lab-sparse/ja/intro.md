# はじめに

この実験では、pandas ライブラリで疎データ構造を使用する方法について説明します。これは、大量のデータがあり、その大部分が同じ（ゼロや NaN など）場合に役立ち、メモリ内でより効率的に表現できます。`SparseArray`、`SparseDtype`、疎アクセサ、疎計算、および scipy 疎行列との相互作用について学びます。

## VM のヒント

VM の起動が完了したら、左上隅をクリックして **ノートブック** タブに切り替え、Jupyter Notebook を使用して練習します。

場合によっては、Jupyter Notebook が読み込み終わるまで数秒待つ必要があります。Jupyter Notebook の制限により、操作の検証を自動化できません。

学習中に問題が発生した場合は、Labby にお問い合わせください。セッション後にフィードバックを提供してください。すぐに問題を解決いたします。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
これは Guided Lab です。学習と実践を支援するためのステップバイステップの指示を提供します。各ステップを完了し、実践的な経験を積むために、指示に注意深く従ってください。過去のデータによると、この <span class="text-green-600 dark:text-green-400">初級</span> レベルの実験の完了率は <span class="text-green-600 dark:text-green-400">100%</span>です。学習者から <span class="text-primary-600 dark:text-primary-400">71%</span> の好評価を得ています。
</div>
