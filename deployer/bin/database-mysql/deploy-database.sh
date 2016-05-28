#/bin/bash
database=$1
server=$2
password=`cat ./.password`

if [ "$database" == "" ]; then
	echo "Add database as a first parameter."
	exit 0
fi

echo "Deploying $database"
mysqldump -u root -p$password $database > /tmp/dump-$database
gzip /tmp/dump-$database /tmp/dump-$database.gz

scp /tmp/dump-$database.gz $server:/tmp/dump-$database.gz

# create database if does not exist
ssh $server 'bash -s' < ./remote-create-database $database 
ssh $server 'bash -s' < ./remote-import-dump $database

rm -f /tmp/dump-$database.gz /tmp/dump-$database
echo "DONE."