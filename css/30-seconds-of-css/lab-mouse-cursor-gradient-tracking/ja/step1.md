# マウスカーソルのグラデーション追跡

`index.html` と `style.css` はすでに仮想マシン (VM) 内に用意されています。

グラデーションがマウスカーソルを追跡するホバーエフェクトを作成するには、以下の手順に従ってください。

1. ボタン上のマウスの位置を追跡するために、2 つの CSS 変数 `--x` と `--y` を宣言します。
2. グラデーションの寸法を変更するために、CSS 変数 `--size` を宣言します。
3. `background: radial-gradient(circle closest-side, pink, transparent)` を使用して、正しい位置にグラデーションを作成します。
4. `Document.querySelector()` と `EventTarget.addEventListener()` を使用して、`'mousemove'` イベントのハンドラーを登録します。
5. `Element.getBoundingClientRect()` と `CSSStyleDeclaration.setProperty()` を使用して、`--x` と `--y` の CSS 変数の値を更新します。

以下はボタンの HTML コードです。

```html
<button class="mouse-cursor-gradient-tracking">
  <span>Hover me</span>
</button>
```

以下は CSS コードです。

```css
.mouse-cursor-gradient-tracking {
  position: relative;
  background: #7983ff;
  padding: 0.5rem 1rem;
  font-size: 1.2rem;
  border: none;
  color: white;
  cursor: pointer;
  outline: none;
  overflow: hidden;
}

.mouse-cursor-gradient-tracking span {
  position: relative;
}

.mouse-cursor-gradient-tracking::before {
  --size: 0;
  content: "";
  position: absolute;
  left: var(--x);
  top: var(--y);
  width: var(--size);
  height: var(--size);
  background: radial-gradient(circle closest-side, pink, transparent);
  transform: translate(-50%, -50%);
  transition:
    width 0.2s ease,
    height 0.2s ease;
}

.mouse-cursor-gradient-tracking:hover::before {
  --size: 200px;
}
```

最後に、以下は JavaScript コードです。

```js
let btn = document.querySelector(".mouse-cursor-gradient-tracking");
btn.addEventListener("mousemove", (e) => {
  let rect = e.target.getBoundingClientRect();
  let x = e.clientX - rect.left;
  let y = e.clientY - rect.top;
  btn.style.setProperty("--x", x + "px");
  btn.style.setProperty("--y", y + "px");
});
```

右下隅にある「Go Live」をクリックして、ポート 8080 で Web サービスを起動してください。その後、**Web 8080** タブを更新すると、Web ページをプレビューできます。
