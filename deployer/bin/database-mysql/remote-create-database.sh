#/bin/bash
database=$1
password=`cat ~/.password`

if ! mysql -u root -p$password -e "use $database" 2> /dev/null; then
	echo "Database $database does not exist, creating..."
	mysqladmin -u root -p$password create $database
fi