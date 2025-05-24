# 배경 이미지 추가하기

다음으로, 이미지를 위한 하위 디렉토리를 생성합니다. `polls/static/polls/` 디렉토리에 `images` 하위 디렉토리를 생성합니다. 이 디렉토리 안에 배경으로 사용하려는 모든 이미지 파일을 추가합니다. 이 튜토리얼의 목적을 위해, 우리는 VM 의 `/tmp/background.png` 디렉토리에서 찾을 수 있는 `background.png`라는 파일을 사용하고 있습니다.

`/tmp/background.png`를 `polls/static/polls/images/background.png`로 복사해야 합니다.

그런 다음, 스타일시트 (`polls/static/polls/style.css`) 에 이미지에 대한 참조를 추가합니다.

```css
body {
  background: white url("images/background.png") no-repeat;
}
```

**Web 8080** 탭을 다시 로드하면 화면 왼쪽 상단에 배경이 로드되는 것을 볼 수 있습니다.

![background image example](../assets/20230908-15-39-41-8dGms0NM.png)

> `{% static %}` 템플릿 태그는 스타일시트와 같이 Django 에서 생성되지 않은 정적 파일에서는 사용할 수 없습니다. 정적 파일을 서로 연결할 때는 항상 **상대 경로 (relative paths)**를 사용해야 합니다. 그러면 정적 파일의 많은 경로를 수정하지 않고도 `STATIC_URL` (URL 을 생성하기 위해 `static` 템플릿 태그에서 사용됨) 을 변경할 수 있습니다.

이것이 **기본 사항 (basics)**입니다. 설정 및 프레임워크에 포함된 기타 세부 정보에 대한 자세한 내용은 `정적 파일 사용 방법 </howto/static-files/index>` 및 `정적 파일 참조 </ref/contrib/staticfiles>`를 참조하십시오. `정적 파일 배포 </howto/static-files/deployment>`는 실제 서버에서 정적 파일을 사용하는 방법을 설명합니다.

정적 파일에 익숙해지면, Django 의 자동 생성된 관리자 사이트를 사용자 정의하는 방법을 배우기 위해 **Django 의 관리자 사이트 사용자 정의하기**를 읽어보세요.
