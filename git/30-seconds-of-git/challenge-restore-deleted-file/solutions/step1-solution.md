```shell
git checkout <commit>^ -- <file>
```

```shell
echo "This is an example file" > example.txt
git add example.txt
git commit -m "Add example.txt file"
rm example.txt
git log --oneline
# "example.txt" was deleted in the commit `0ed86a3`
git checkout 0ed86a3^ -- example.txt
# Restores the example.txt file
```
