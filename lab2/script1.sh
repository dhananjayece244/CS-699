#Shell program to print all folder name and files in the current directories.
echo " Following are the folders present in the current directories"
for item in *
do
	if [ -d $item ]
	then 
		echo $item
	fi
done
echo " Following are the files present in the current directories"
for item in *
do
	if [ -f $item ]
	then 
		echo $item
	fi
done
