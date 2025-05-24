# 마지막 커밋 수정하기

Git 저장소 (repository) 에 변경 사항을 커밋 (commit) 했는데, 파일 추가를 잊었거나 작은 변경 사항을 적용하지 않았다는 것을 깨달았습니다. 이 작은 변경 사항만을 위해 새로운 커밋을 생성하고 싶지는 않지만, 커밋 메시지 (commit message) 를 변경하고 싶지도 않습니다. 메시지를 변경하지 않고 마지막 커밋을 수정하려면 어떻게 해야 할까요?

마지막 커밋을 수정하는 방법을 보여주기 위해 `https://github.com/labex-labs/git-playground`의 저장소를 사용해 보겠습니다.

1. 저장소를 복제 (clone) 하고, 디렉토리로 이동하여 신원을 구성합니다.

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. 파일 추가를 잊었거나 작은 변경 사항을 적용하지 않았다는 것을 깨달았습니다. `README.md` 파일의 끝에 "New content" 텍스트를 추가합니다. 메시지를 변경하지 않고 마지막 커밋에 스테이징된 (staged) 변경 사항을 추가합니다.

```shell
echo "New content" >> README.md
git add README.md
git commit --amend --no-edit
```

3. 마지막 커밋에 변경 사항이 포함되었는지 확인합니다.

```shell
git show HEAD
```

다음은 마지막 커밋의 내용입니다.
![Updated commit contents display](../assets/challenge-update-commit-contents.png)
