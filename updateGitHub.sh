#!/bin/sh

echo "----Adding files..."
git add Readme.txt
git add graphicInterface.py
git add main.py
git add mySqlDBInterface.py
git add scheduler.py
git add updateGitHub.sh
git add ./start_date.cfg
echo "----Making the commit $1..."
git commit -m $1
echo "----Pushing..."
git push origin master
# cum rezolv faza cu credentialele...?
echo "----Git Hub updated succesfully!"

