# Scripts that sould be at the beginning

export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="robbyrussell"

plugins=(
	git 
	asdf 
	yarn 
	zsh-autosuggestions
)
source $ZSH/oh-my-zsh.sh


# Loads all configurations in .zshrc.d
for file in $HOME/.zshrc.d/*; do
  source $file
done

# Scripts that should be at the end
eval "$(zoxide init zsh)"


[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

