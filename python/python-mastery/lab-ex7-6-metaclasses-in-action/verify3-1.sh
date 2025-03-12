#!/bin/bash
grep -q "class StructureMeta" /home/labex/project/structure.py && grep -q "metaclass=StructureMeta" /home/labex/project/structure.py
exit $?
