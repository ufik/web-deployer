#/bin/bash
database=$1
server=$2
password=`cat ./.password`
pwd

if [ "$database" == "" ]; then
	echo "Add database as a first parameter."
	exit 0
fi

echo "Deploying $database to $server"
mysqldump -u root -p$password $database > /tmp/dump-$database

gzip -c /tmp/dump-$database > /tmp/dump-$database.gz

scp /tmp/dump-$database.gz $server:/tmp/dump-$database.gz

# create database if does not exist
ssh $server 'bash -s' < /usr/bin/remote-create-database.sh $database 
ssh $server 'bash -s' < /usr/bin/remote-import-dump.sh $database

rm -f /tmp/dump-$database.gz /tmp/dump-$database

echo '#EOF#'