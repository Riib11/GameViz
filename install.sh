#
# install python
#
echo \>\>\> installing python3 module
pip3 install -e src

#
# install bash command
#
echo \>\>\> install bash commands
cp ~/git/GameViz/gameviz.sh /usr/local/bin/gameviz
chmod +x /usr/local/bin/gameviz
chmod +x ~/git/GameViz/install.sh