#!/bin/bash

git checkout gh-pages

gauge docs spectacle specs

cp -r ./docs/html/* ./

rm -rf ./docs

git add .

git commit -m "Update gh-pages."

git push origin gh-pages

git checkout master