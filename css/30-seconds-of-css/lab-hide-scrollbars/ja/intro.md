# はじめに

この実験では、CSS を使って要素にスクロールバーを非表示にしながら、依然としてスクロール可能にするという概念を探ります。スクロールを有効にするために`overflow: auto`プロパティを使い、Firefox では`scrollbar-width: none`を使ってスクロールバーを非表示にし、WebKit ブラウザでは`::-webkit-scrollbar`疑似要素に`display: none`を使ってスクロールバーを非表示にします。この実験では、この CSS テクニックを実装して、スクロール可能な要素のユーザーエクスペリエンスを向上させるための実践的な経験を提供します。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
これは Guided Lab です。学習と実践を支援するためのステップバイステップの指示を提供します。各ステップを完了し、実践的な経験を積むために、指示に注意深く従ってください。過去のデータによると、この <span class="text-green-600 dark:text-green-400">初級</span> レベルの実験の完了率は <span class="text-green-600 dark:text-green-400">100.00%</span>です。
</div>
