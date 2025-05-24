# 시스템 폰트 스택 (System Font Stack)

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

네이티브 앱 (native app) 과 같은 느낌을 얻으려면 운영 체제의 네이티브 폰트를 사용하십시오. `font-family`를 사용하여 폰트 목록을 정의합니다. 브라우저는 각 폰트를 순차적으로 찾으며, 가능한 경우 첫 번째 폰트를 선호하고, 폰트를 찾을 수 없는 경우 (시스템 또는 CSS 에 정의된 경우) 다음 폰트로 대체합니다. iOS 및 macOS (Chrome 제외) 의 San Francisco 에는 `-apple-system`을 사용하고, macOS Chrome 의 San Francisco 에는 `BlinkMacSystemFont`를 사용합니다. Windows 10 의 경우 `'Segoe UI'`를 사용하고, Android 의 경우 `Roboto`를 사용하며, KDE 가 있는 Linux 의 경우 `Oxygen-Sans`를 사용하고, Ubuntu (모든 변형) 의 경우 `Ubuntu`를 사용하며, GNOME Shell 이 있는 Linux 의 경우 `Cantarell`을 사용합니다. macOS 10.10 이하의 경우 `'Helvetica Neue'` 및 `Helvetica`를 사용합니다. 모든 운영 체제에서 널리 지원되는 대체 sans serif 폰트의 경우 `Arial`을 사용합니다. 특정 텍스트에 시스템 폰트를 적용하려면 다음 HTML 및 CSS 를 사용하십시오.

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

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
