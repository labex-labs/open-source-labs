# ホバー時のシャドウボックスアニメーション

VM には既に `index.html` と `style.css` が用意されています。

テキストの周りにホバー時にシャドウボックスを作成するには、次の手順に従います。

1. `transform: perspective(1px)` を設定して、Z 平面とユーザーの間の距離に影響を与えることで要素に 3D 空間を与え、`translateZ(0)` を使って 3D 空間内で `p` 要素を z 軸に沿って再配置します。
2. `box-shadow` を使ってボックスを透明にします。
3. `transition-property` プロパティを使って、`box-shadow` と `transform` の両方にトランジションを有効にします。
4. `:hover`、`:active`、`:focus` の疑似クラスセレクタを使って、新しい `box-shadow` と `transform: scale(1.2)` を適用してテキストのスケールを変更します。
5. `p` 要素に `hover-shadow-box-animation` クラスを追加します。

以下が HTML コードです。

```html
<p class="hover-shadow-box-animation">Box it!</p>
```

以下が CSS コードです。

```css
.hover-shadow-box-animation {
  display: inline-block;
  vertical-align: middle;
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px transparent;
  margin: 10px;
  transition:
    box-shadow 0.3s,
    transform 0.3s;
}

.hover-shadow-box-animation:hover,
.hover-shadow-box-animation:focus,
.hover-shadow-box-animation:active {
  box-shadow: 1px 10px 10px -10px rgba(0, 0, 24, 0.5);
  transform: scale(1.2);
}
```

右下隅の「Go Live」をクリックして 8080 ポートで Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
