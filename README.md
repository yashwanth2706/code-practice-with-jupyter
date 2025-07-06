
Configuration:
If you get a warning from git
"LF will be replaced by CRLF the next time Git touches it"

Configure git to support Unix like systems (Even when there is no warning) (Recommended)

git config --global core.autocrlf false
git config --global core.eol lf

When using .ipynb files in the github, rendering must likly be an UNIX system which might not be able to render the .ipynb file which has windows supporting formatting
