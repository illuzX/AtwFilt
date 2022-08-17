if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/illuzX/AtwFilt /AtwFilt
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /AtwFilt
fi
cd /AtwFilt
pip3 install -U -r requirements.txt
echo "AtwFilt bot runing...."
python3 main.py
