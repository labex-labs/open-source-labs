# 기록에서 파일 제거하기

API 키나 비밀번호와 같은 민감한 정보를 포함하는 파일을 실수로 Git 저장소에 커밋했다고 가정해 보겠습니다. 이 파일은 절대 커밋해서는 안 된다는 것을 깨닫고 저장소 기록에서 완전히 제거하려고 합니다. 하지만 파일을 삭제하고 변경 사항을 커밋하는 것만으로는 저장소 기록에서 제거되지 않습니다. 파일은 이전 커밋에서 여전히 액세스할 수 있으며, 이는 보안 위험을 초래할 수 있습니다.

이 랩을 완료하려면 GitHub 계정에서 `git-playground` Git 저장소를 사용합니다. 이 저장소는 `https://github.com/labex-labs/git-playground.git`의 포크에서 가져온 것입니다. 이 저장소에는 절대 커밋해서는 안 되는 `file1.txt`라는 파일이 포함되어 있습니다. 저장소 기록에서 `file1.txt`를 제거하려면 다음 단계를 따르세요.

1. 저장소를 로컬 머신에 복제합니다.

```shell
git clone https://github.com/your-username/git-playground
```

2. 다음 명령을 사용하여 디렉토리로 이동하고 ID 를 구성합니다.

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. 저장소의 인덱스에서 파일을 삭제합니다.

```shell
git rm --cached --ignore-unmatch file1.txt
```

4. 커밋 메시지 "Remove sensitive file1.txt"로 이 변경 사항을 커밋합니다.

```shell
git commit -m "Remove sensitive file1.txt"
```

5. `file1.txt`의 모든 인스턴스를 제거하여 저장소의 기록을 다시 작성합니다.

```shell
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch file1.txt" --prune-empty --tag-name-filter cat -- --all
```

6. 변경 사항을 원격 저장소로 강제 푸시합니다.

```shell
git push origin --force --all
```

이 단계를 완료하면 `file1.txt`가 저장소 기록에서 완전히 제거되고 `git log --remotes`를 실행한 후 `file1.txt`에 대한 커밋이 표시되지 않습니다.
