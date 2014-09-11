echo "Please enter in your UTCS username:"
read username
python ~/UTCSLabs/labs.py
content=$(cat ~/UTCSLabs/ssh.txt)
ssh -X $username@$content.cs.utexas.edu
