# はじめに

この実験では、JavaScript における浅いクローンの概念を探ります。浅いクローンは、元のオブジェクトのすべてのプロパティを持つ新しいオブジェクトを作成しますが、プロパティ自体はクローンされません。代わりに、参照によってコピーされます。これは、元のオブジェクトのプロパティに対して行われた変更が、クローンされたオブジェクトにも反映されることを意味します。この実験を通じて、JavaScript の `Object.assign()` メソッドを使用してオブジェクトの浅いクローンを作成する方法を理解します。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
これは Guided Lab です。学習と実践を支援するためのステップバイステップの指示を提供します。各ステップを完了し、実践的な経験を積むために、指示に注意深く従ってください。過去のデータによると、この <span class="text-green-600 dark:text-green-400">初級</span> レベルの実験の完了率は <span class="text-green-600 dark:text-green-400">100%</span>です。
</div>
