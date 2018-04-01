#Shell program to count the number of words, characters and lines.

echo "Enter file name"

read file1

echo "Number of word = "
wc -w $file1
echo "Number of characters="
wc -c $file1
echo "Number of lines"
wc -l $file1
