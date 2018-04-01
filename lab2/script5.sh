#Shell script to create back up of a file.

echo "Enter the file name"
read file1
if [ -f $file1 ];
then
    cp $file1 $file1.backup
    echo "backed up done "
else
    echo "file does not exists"
fi


