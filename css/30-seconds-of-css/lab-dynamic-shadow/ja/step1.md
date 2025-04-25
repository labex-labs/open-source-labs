# 動的な影

VM 内には既に`index.html`と`style.css`が用意されています。

要素の色に基づく影を作成するには、次の手順に従ってください。

1. `position: absolute`を使用し、`width`と`height`を`100%`に設定した`::after`疑似要素を使用して、親要素内の利用可能なスペースを埋めます。
2. `background: inherit`を使用して、親要素の`background`を継承します。
3. `top`を使用して疑似要素をわずかにオフセットします。その後、`filter: blur()`を使用して影を作成し、`opacity`を設定して半透明にします。
4. `z-index: -1`を設定することで疑似要素を親要素の後ろに配置します。親要素には`z-index: 1`を設定します。

以下は、HTML と CSS のコードの例です。

```html
<div class="dynamic-shadow"></div>
```

```css
.dynamic-shadow {
  position: relative;
  width: 10rem;
  height: 10rem;
  background: linear-gradient(75deg, #6d78ff, #00ffb8);
  z-index: 1;
}

.dynamic-shadow::after {
  content: "";
  width: 100%;
  height: 100%;
  position: absolute;
  background: inherit;
  top: 0.5rem;
  filter: blur(0.4rem);
  opacity: 0.7;
  z-index: -1;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
