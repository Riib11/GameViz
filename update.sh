#
# update git
#
echo \>\>\> updating git...
git fetch ~/git/GameViz
git pull ~/git/GameViz

#
# update python
#
echo \>\>\> updating python3...
pip3 install -e src

#
# update bash command
#
echo \>\>\> updating bash...
cp ~/git/GameViz/gameviz.sh /usr/local/bin/gameviz
chmod +x /usr/local/bin/gameviz
chmod +x ~/git/GameViz/install.sh