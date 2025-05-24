# 여러 줄 텍스트 자르기

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

한 줄보다 긴 텍스트를 자르려면 다음 단계를 따르세요.

1. `overflow: hidden`을 사용하여 텍스트가 치수를 초과하지 않도록 합니다.
2. 요소가 최소한 하나의 고정된 치수를 갖도록 `width`를 `400px`로 설정합니다.
3. `font-size`, `line-height`, `numberOfLines`를 사용하여 계산된 `height: 109.2px`를 설정합니다 (이 경우 `26 * 1.4 * 3 = 109.2`).
4. HTML 에서 `p` 요소에 클래스 `truncate-text-multiline`을 추가합니다.
5. `.truncate-text-multiline` 클래스에 대한 CSS 에서 `font-size: 26px` 및 `line-height: 1.4`를 설정합니다.
6. 텍스트 스타일을 지정하기 위해 `color: #333` 및 `background: #f5f6f9`를 설정합니다.
7. `transparent`에서 `background-color`로 그라데이션을 만들려면 `.truncate-text-multiline::after` 가상 요소에 다음 CSS 규칙을 추가합니다.

```css
.truncate-text-multiline::after {
  content: "";
  position: absolute;
  bottom: 0;
  right: 0;
  width: 150px;
  height: 36.4px;
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #f5f6f9 50%);
}
```

이렇게 하면 `font-size * line-height` (이 경우 `26 * 1.4 = 36.4`) 공식을 기반으로 그라데이션 컨테이너에 대해 계산된 `36.4px` 높이의 그라데이션 컨테이너가 생성됩니다. `::after` 가상 요소는 `.truncate-text-multiline` 요소의 오른쪽 하단 모서리에 배치됩니다.

웹 서비스를 포트 8080 에서 실행하려면 오른쪽 하단 모서리에 있는 'Go Live'를 클릭하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
