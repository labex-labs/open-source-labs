# Git Cherry-Pick

개발자로서 여러 브랜치가 있는 프로젝트에서 작업하고 있습니다. 이전 커밋에서 이루어진 특정 변경 사항을 현재 브랜치에 적용하고 싶지만, 필요하지 않은 다른 변경 사항이 포함되어 있으므로 전체 브랜치를 병합하고 싶지 않습니다. 이 시나리오에서는 `git cherry-pick` 명령을 사용하여 특정 변경 사항을 현재 브랜치에 적용할 수 있습니다.

이 랩에서는 `https://github.com/labex-labs/git-playground`의 저장소를 사용해 보겠습니다. 다음 단계를 따라 챌린지를 완료하십시오.

1. 저장소를 복제하고, 디렉토리로 이동하여 ID 를 구성합니다.

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. `one-branch`라는 브랜치를 생성하고 전환한 다음, `hello.txt` 파일을 생성하고 "hello,world"를 작성하고, 스테이징 영역에 추가하고 "add hello.txt" 메시지로 커밋합니다.

```shell
git checkout -b one-branch
echo "hello,world" > hello.txt
git add .
git commit -m "add hello.txt"
```

3. 이전 단계에서 생성된 커밋의 해시를 식별하여 `master` 브랜치에 적용합니다.

```shell
git log
```

4. `master` 브랜치를 체크아웃하고 변경 사항을 `master` 브랜치에 적용합니다.

```shell
git checkout master
git cherry-pick 1609c283ec86ee4
```

5. 변경 사항이 `master` 브랜치에 적용되었는지 확인합니다.

```shell
git log
```

다음은 `master` 브랜치에서 `git log`를 실행한 결과입니다.

```shell
ADD hello.txt
```
