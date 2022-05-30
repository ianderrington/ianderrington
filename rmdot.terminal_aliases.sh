echo "Loading functionality from ~/.terminal_aliases"
#bind '"\e[A":history-search-backward'
#bind '"\e[B":history-search-forward'
bindkey '\e[A' history-search-backward
bindkey '\e[B' history-search-forward

alias gsc2="ssh -AY derringi@gsimc2" 
alias ssh_merge1="ssh -AY genia@merge1" 
alias sm1="ssh -A m1" 
alias sg1="ssh -A gm1" 
alias gv1="ssh vis1" 
alias ssh_vis1="ssh -Y genia@10.21.61.94" 
alias sc1="ssh -Y ian@10.21.56.21" 
alias ssh_simc1="ssh -Y ian@10.21.56.21" 
alias sc2="ssh -Y simc2" 
alias slock="ssh -Y ian@10.21.50.124" 
alias dt="ls -ltr" 
alias ga="git add" 
alias glh="git log | head -1 | cut -f2 -d' '" 
alias glhc="glh | pbcopy" 
alias gd="git diff" 
alias gdn="git diff --name-only" 
alias pull="git pull; python setup.py develop" 
alias dev="python setup.py develop" 
alias nosetests="nosetests --logging-level=WARNING" 
alias gd="git diff" 
alias gp="git pull" 
alias gb="git branch" 
alias subl="/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl" 
alias jpn="jupyter notebook" 
alias gb="git branch" 
alias gpush="git push" 
alias gpull="git pull" 
alias gf="git fetch" 
alias gcam="git commit -am" 
alias gs="git status" 
alias gco="git checkout" 
alias gdmno="git diff master --name-only" 
alias gl="git log" 
alias v="vim" 
alias ca="conda activate" 
alias cda="conda deactivate"


mkcd ()
{
    mkdir -p -- "$1" &&
       cd -P -- "$1"
}
