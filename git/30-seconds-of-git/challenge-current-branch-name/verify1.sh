cd /home/labex/project/git-playground

# Get the current branch name using different methods
current_branch_rev_parse=$(cat ~/.zsh_history | grep -v grep | grep "git rev-parse" | tail -n 1)
current_branch_abbrev_ref=$(cat ~/.zsh_history | grep -v grep | grep "abbrev-ref" | tail -n 1)
current_branch_show_current=$(cat ~/.zsh_history | grep -v grep | grep "git branch" | grep "show-current" | tail -n 1)
current_branch_symbolic_ref=$(cat ~/.zsh_history | grep -v grep | grep "git symbolic-ref" | grep "short" | tail -n 1)

# Check if any of the methods returned a non-empty result
if [ -n "$current_branch_rev_parse" ] \
  || [ -n "$current_branch_abbrev_ref" ] \
  || [ -n "$current_branch_show_current" ] \
  || [ -n "$current_branch_symbolic_ref" ]; then
  echo "True"
fi
