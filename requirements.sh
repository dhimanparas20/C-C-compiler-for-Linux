sudo apt update
sudo apt-get install gcc g++ openjdk-17-jdk-headless
mkdir ~/bin
mv run.py ~/bin/
export PATH="$PATH:$HOME/bin"
echo 'export PATH="$PATH:$HOME/bin"' >> ~/.bashrc
chmod +x ~/bin/run.py
source ~/.bashrc
cd
echo 'alias runf="time python3 ~/bin/run.py -f"' >> .bashrc
