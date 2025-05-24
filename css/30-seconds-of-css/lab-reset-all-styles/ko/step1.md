# 모든 스타일 재설정

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

모든 스타일을 기본값으로 재설정하려면 `all` 속성을 사용하십시오. 이 속성은 `direction` 및 `unicode-bidi` 속성에는 영향을 미치지 않습니다. 다음은 이를 사용하는 예입니다.

```html
<div class="reset-all-styles">
  <h5>Title</h5>
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure id
    exercitationem nulla qui repellat laborum vitae, molestias tempora velit
    natus. Quas, assumenda nisi. Quisquam enim qui iure, consequatur velit sit?
  </p>
</div>
```

```css
.reset-all-styles {
  all: initial;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
