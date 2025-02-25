# matplotlibrc ファイルの変更

`matplotlibrc` ファイルは、Matplotlib のあらゆる種類のプロパティをカスタマイズするための設定ファイルです。このファイルは、グラフのサイズ、線幅、色、フォントなどのプロパティの既定値を制御します。好みに応じて Matplotlib をカスタマイズするには、`matplotlibrc` ファイルを変更します。このファイルはシステム内のさまざまな場所にあり、Matplotlib は特定の順序でそれを探します。`matplotlibrc` ファイルが見つかると、他の設定よりも優先されます。現在アクティブな `matplotlibrc` ファイルのパスを表示するには、`matplotlib.matplotlib_fname()` 関数を使用します。
