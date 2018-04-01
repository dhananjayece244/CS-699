#Shell program to print top 5 frequent word used in a file.
echo "Enter the file name"
read f
tr -c '[:alnum:]' '[\n*]' < $f | sort | uniq -c | sort -nr | head  -5
