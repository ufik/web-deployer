#/bin/bash

fromPath=$1
toPath=$2
server=$3
user=$4
hash=$5

rsync -avzp -e ssh --delete --exclude-from './exclude.txt' $fromPath $user@$server:$toPath 2> /tmp/deploy_error-$hash.log 1> /tmp/deploy-$hash.log

# move like application specific scripts (template script)
# ssh $server 'bash -s' < /home/voslar/sync_scripts/modpagespeed-clean-cache
# ssh $server 'bash -s' < /home/voslar/sync_scripts/update-database $2 > /home/voslar/sync_scripts/updatedb.log 2> /home/voslar/sync_scripts/updatedb_error.log