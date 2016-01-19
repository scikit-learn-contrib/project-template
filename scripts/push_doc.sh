#!/bin/bash
# This script is meant to be called in the "deploy" step defined in 
# circle.yml. See https://circleci.com/docs/ for more details.
# The behavior of the script is controlled by environment variable defined
# in the circle.yml in the top level folder of the project.


if [ -z $CIRCLE_PROJECT_USERNAME ];
then USERNAME="sklearn-ci";
else USERNAME=$CIRCLE_PROJECT_USERNAME;
fi

DOC_REPO="sklearn-stub"
DOC_URL="docs/"

MSG="Pushing the docs for revision for branch: $CIRCLE_BRANCH, commit $CIRCLE_SHA1"

cd $HOME
rm -rf tmp
mkdir tmp
cp -R $HOME/sklearn-stub/doc/_build/html/* ./tmp/ 
find tmp/
if [ ! -d $DOC_REPO ];
    then git clone "git@github.com:vighneshbirodkar/"$DOC_REPO".git";
fi
cd $DOC_REPO
git checkout -f gh-pages
git reset --hard origin/gh-pages
git clean -f
echo 'Echoing dir structure'
find 
git rm -rf * $DOC_URL && rm -rf $DOC_URL
mkdir $DOC_URL
cp -R $HOME/tmp/* ./$DOC_URL/
git config --global user.email "vnb222+ci@nyu.edu"
git config --global user.name $USERNAME
git add -f ./$DOC_URL/
git commit -m "$MSG"
git push origin gh-pages

echo $MSG 
