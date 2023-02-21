#
# ~/.zshrc
#
eval "$(starship init zsh)"
# User configuration
export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="robbyrussell"

plugins=(git docker docker-compose docker-machine docker-compose autoswitch_virtualenv zsh-autosuggestions zsh-syntax-highlighting)

source $ZSH/oh-my-zsh.sh

## Alias
alias composer="php ~/.composer/composer.phar"
alias sail='[ -f sail ] && sh sail || sh vendor/bin/sail'
alias dev="cd ~/Projects"
alias att="yay -Syyuu"

## Poetry
export PATH="/home/johnny/.local/bin:$PATH"

## Doom emacs
export PATH="$HOME/.emacs.d/bin:$PATH"

# opam configuration
[[ ! -r /home/johnny/.opam/opam-init/init.zsh ]] || source /home/johnny/.opam/opam-init/init.zsh  > /dev/null 2> /dev/null
alias ocaml="rlwrap ocaml"
