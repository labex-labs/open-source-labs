# Squiggle Link Hover Effect (물결 링크 호버 효과)

`index.html` 및 `style.css`는 이미 VM 에 제공되어 있습니다.

링크 위에 마우스를 올렸을 때 물결 효과를 만들려면 다음 단계를 따르세요.

1. `linear-gradient`를 사용하여 링크에 대한 반복 배경을 만듭니다.

```css
a.squiggle {
  background: linear-gradient(to bottom, #0087ca 0%, #0087ca 100%);
  background-position: 0 100%;
  background-repeat: repeat-x;
  background-size: 2px 2px;
  color: inherit;
  text-decoration: none;
}
```

2. 물결 모양 경로와 애니메이션이 포함된 SVG 를 포함하는 데이터 URL 의 `background-image`를 사용하여 링크에 대한 `:hover` 상태를 만듭니다.

```css
a.squiggle:hover {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 4'%3E%3Cstyle type='text/css'%3E.squiggle{animation:shift .3s linear infinite;}@keyframes shift {from {transform:translateX(0);}to {transform:translateX(-15px);}}%3C/style%3E%3Cpath fill='none' stroke='%230087ca' stroke-width='2' class='squiggle' d='M0,3.5 c 5,0,5,-3,10,-3 s 5,3,10,3 c 5,0,5,-3,10,-3 s 5,3,10,3'/%3E%3C/svg%3E");
  background-size: auto 4px;
}
```

3. 페이지에 링크를 추가하려면 아래 HTML 코드를 사용합니다.

```html
<p>
  The <a class="squiggle" href="#">magnificent octopus</a> swam along
  gracefully.
</p>
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
