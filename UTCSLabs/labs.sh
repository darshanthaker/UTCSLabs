path=~/UTCSLabs/UTCSLabs
echo "Please enter in your UTCS username:"
read username
python $path/labs.py
content=$(cat $path/ssh.txt)
ssh -X $username@$content.cs.utexas.edu
