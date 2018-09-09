#!/bin/bash

# Modifyied from: https://gist.github.com/igorkosta/02aa04d3fe82267962579b863a8ed48a#file-deploy-sh
# Deploys Vue static page to AWS s3

# make file executable
set -e

instructions ()
{
  echo "*********************************************"
  echo "Run this script as an npm task              *"
  echo "$ npm run deploy <bucket_name>              *"
  echo "env: eg. static                             *"
  echo "for example: $ npm run deploy static        *"
  echo "*********************************************"
}
if [ $# -eq 0 ]; then
  instructions
  exit 1
fi
BUCKET="$1"
DIST="dist"
TMP="tmp"

echo "Remove tmp directory created previously"
rm -rf $TMP

echo "Create a tmp directory and copy all the files there"
rsync -avz --exclude '*.map'  dist tmp

echo "Clean the bucket"
aws s3 rm s3://$BUCKET --recursive

echo "Copying files over to S3"
aws s3 sync ./$TMP/$DIST s3://$BUCKET --acl public-read

echo "🚀 🚀 🚀 🚀 🚀 "
