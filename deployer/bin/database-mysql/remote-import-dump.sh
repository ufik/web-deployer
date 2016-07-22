#/bin/bash
database=$1
password=`cat ./.password`

gunzip /tmp/dump-$database.gz /tmp/dump-$database 2> /dev/null
mysql -u root -p$password $database < /tmp/dump-$database

rm -f /tmp/dump-$database.gz /tmp/dump-$database

echo 'remote> Database deployed.'