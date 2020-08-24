# Contents
1. [Change last commit with adding new or changed files](https://github.com/AlekseiBulygin/Python/tree/master/git#change-last-commit-with-adding-new-or-changed-files-local-repo-only)

#### Change last commit with adding new or changed files (local repo only)  
Note! Local repo only. You can use this approach when you have merged commits

Optional step in case when commit is not last:  
`git reset --soft {SHA}` - reset HEAD to the desired commit, doesn't change local directory files  

`git add all/changed/new/files`  
`git commit --amend` - will open text editor for changing commit message  
