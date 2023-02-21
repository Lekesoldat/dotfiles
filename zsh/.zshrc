# fpath=($HOME/.zshrc.f $fpath)
for function in $HOME/.zshrc.f/*; do
  autoload $function
done

# Loads all configurations in .zshrc.d
for file in $HOME/.zshrc.d/*; do
  source $file
done