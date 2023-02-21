# My dotfiles

Feel free to use (:


## Manage your dotifles 

### Create a dotfiles repository


``` sh
# Go to your home directory and create a folder to save your dotfiles
cd $HOME
mkdir dotfiles

# Go to folder and start git settings
cd dotfiles

git init
git branch -M main
git remote add origin git@github.com:{your_usarname}/{your_repo_name}.git

# Tell git your worktree starts in your $HOME
git config core.worktree '../../'

# Ignore all
echo '*' >> ../.gitignore


# Now you need to force files to git

git add -f ../.zshrc
git add -f ../.bashrc


# Commit your changes to your repo

git commit -m "first commint"
git push -u origin main
```


# Deploy your dotfiles in a new device

**coming soon**


### Project inspiration
  - [Meleu Gitgub](https://github.com/meleu/.dotfiles)
  - [Meleu page](https://meleu.sh/dotfiles/)
 
