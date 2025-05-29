# 지그재그 배경 패턴

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

지그재그 배경 패턴을 만들려면 다음 단계를 따르세요.

1. `background-color`를 사용하여 흰색 배경을 설정합니다.
2. 네 개의 `linear-gradient()` 값을 사용하여 `background-image`로 지그재그 패턴의 부분을 만듭니다.
3. `background-size`를 사용하여 패턴의 크기를 지정합니다.
4. `background-position`을 사용하여 패턴의 부분을 올바른 위치에 배치합니다.
5. 패턴을 반복하려면 `background-repeat`를 사용합니다.
6. **참고:** 요소의 `height` 및 `width`는 데모 목적으로만 고정되어 있습니다.

다음은 코드 스니펫 예시입니다.

```html
<div class="zig-zag"></div>
```

```css
.zig-zag {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image:
    linear-gradient(135deg, #000 25%, transparent 25%),
    linear-gradient(225deg, #000 25%, transparent 25%),
    linear-gradient(315deg, #000 25%, transparent 25%),
    linear-gradient(45deg, #000 25%, transparent 25%);
  background-position:
    -30px 0,
    -30px 0,
    0 0,
    0 0;
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
