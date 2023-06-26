#!/bin/zsh

cd ~/project
git diff | grep 'scipy'
git diff | grep 'random'
git diff | grep 'csr_matrix'
git diff | grep 'from_spmatrix'
git diff | grep 'to_coo'
