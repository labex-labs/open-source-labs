# はじめに

この実験では、JavaScript を使って循環参照を含む JSON オブジェクトをシリアライズする方法を検討します。カスタムの置換関数と `WeakSet` を使って循環参照を検出し、省略します。この実験が終了するとき、JavaScript で循環データ構造を処理する方法と、それを JSON 形式にシリアライズする方法をより深く理解するようになります。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
これは Guided Lab です。学習と実践を支援するためのステップバイステップの指示を提供します。各ステップを完了し、実践的な経験を積むために、指示に注意深く従ってください。過去のデータによると、この <span class="text-green-600 dark:text-green-400">初級</span> レベルの実験の完了率は <span class="text-green-600 dark:text-green-400">100.00%</span>です。
</div>
