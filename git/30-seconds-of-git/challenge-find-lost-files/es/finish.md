# Resumen

Usar Git para encontrar archivos y commits perdidos puede ser una salvación cuando se está trabajando en un proyecto. Al ejecutar el comando `git fsck --lost-found`, se pueden identificar cualquier objeto colgante y extraerlos al directorio `.git/lost-found`. A partir de ahí, se pueden revisar los archivos para determinar si son los archivos que faltan.
