# Fixup 커밋 생성하기

여러 명의 개발자와 함께 프로젝트를 진행하는 중, 며칠 전에 생성된 커밋에서 작은 오류를 발견했다고 가정해 봅시다. 오류를 수정하고 싶지만, 새로운 커밋을 생성하여 다른 개발자의 작업에 지장을 주고 싶지 않습니다. 이럴 때 fixup 커밋이 유용합니다. Fixup 커밋을 생성하면 새로운 커밋을 생성하지 않고도 필요한 변경 사항을 적용할 수 있으며, fixup 커밋은 다음 rebase 작업 중에 자동으로 원래 커밋과 병합됩니다.

예를 들어, `hello.txt` 파일에 문자열 "hello,world"를 쓰고, "Added file1.txt"라는 메시지가 있는 커밋에 "fixup" 커밋으로 추가하여, 후속 rebase 작업에서 자동으로 병합되도록 하는 것이 목표입니다.

이 랩에서는 `https://github.com/labex-labs/git-playground`의 저장소를 사용해 보겠습니다.

1. 저장소를 복제하고, 디렉토리로 이동한 후, 신원을 구성합니다.

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. `hello.txt` 파일을 생성하고, "hello,world"를 작성한 후, 스테이징 영역에 추가합니다.

```shell
echo "hello,world" > hello.txt
git add .
```

3. fixup 커밋을 생성하려면, `git commit --fixup <commit>` 명령을 사용할 수 있습니다.

```shell
git commit --fixup cf80005
# This is the hash of the commit message "Added file1.txt".
```

이렇게 하면 지정된 커밋에 대한 fixup 커밋이 생성됩니다. fixup 커밋을 생성하기 전에 변경 사항을 스테이징해야 합니다.

4. fixup 커밋을 생성한 후, `git rebase --interactive --autosquash` 명령을 사용하여 다음 rebase 작업 중에 fixup 커밋을 원래 커밋과 자동으로 병합할 수 있습니다. 예를 들어:

```shell
git rebase --interactive --autosquash HEAD~3
```

대화형 편집기를 열 때, 텍스트를 변경할 필요 없이 저장하고 종료하면 됩니다. 이렇게 하면 마지막 3 개의 커밋에 대해 rebase 가 수행되고, 모든 fixup 커밋이 해당 원래 커밋과 자동으로 병합됩니다.

`git show HEAD~1` 명령을 실행한 결과는 다음과 같습니다.

```shell
[object Object]
```
