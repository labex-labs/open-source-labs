# Solutions

```shell
git log [--since= [--until= < date-from > ] < date-to > ]

git log --since='Apr 25 2023' --until='Apr 27 2023'
# commit c191f90c7766ee6d5f24e90b552a6d446f0d02e4
# Author: labex
# Date: Tue Apr 6 11:11:08 2023 +0300
# [...]

git log --since='12 weeks ago'
# commit c191f90c7766ee6d5f24e90b552a6d446f0d02e4
# Author: labex
# Date: Tue Apr 6 11:11:08 2023 +0300
# [...]
```

```shell
cd git-playground
git log --since='Apr 25 2023' --until='Apr 27 2023'
git log --since='12 weeks ago'
```
