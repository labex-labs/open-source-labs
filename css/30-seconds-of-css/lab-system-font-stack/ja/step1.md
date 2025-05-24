# システムフォントスタック

VM には既に `index.html` と `style.css` が用意されています。

ネイティブアプリの感じを実現するには、オペレーティングシステムのネイティブフォントを使用します。`font-family` を使ってフォントのリストを定義します。ブラウザは順に各フォントを探し、可能な限り最初のフォントを優先し、そのフォントが見つからない場合（システム上または CSS で定義されていない場合）は次のフォントに切り替えます。iOS と macOS では San Francisco 用に `-apple-system` を使用します（Chrome ではなく）、macOS Chrome では San Francisco 用に `BlinkMacSystemFont` を使用します。Windows 10 では `'Segoe UI'` を使用し、Android では `Roboto` を使用し、KDE を搭載した Linux では `Oxygen-Sans` を使用し、Ubuntu（すべてのバリアント）では `Ubuntu` を使用し、GNOME Shell を搭載した Linux では `Cantarell` を使用します。macOS 10.10 以下では `'Helvetica Neue'` と `Helvetica` を使用します。すべてのオペレーティングシステムで広くサポートされているフォールバックのサンセリフフォントとして `Arial` を使用します。特定のテキストにシステムフォントを適用するには、次の HTML と CSS を使用します。

```html
<p class="system-font-stack">This text uses the system font.</p>
```

```css
.system-font-stack {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", Helvetica, Arial,
    sans-serif;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
