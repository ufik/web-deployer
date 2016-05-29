#/bin/bash

fromPath=$1
toPath=$2
server=$3
user=$4

rsync -avzp -e ssh --delete --exclude-from './exclude.txt' $fromPath $user@$server:$toPath # 2> /tmp/deploy_error-$hash.log 1> /tmp/deploy-$hash.log

echo '#EOF#'