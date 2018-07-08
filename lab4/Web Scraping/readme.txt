You have been asked to write a program to count the number of occurrences of a given pattern in the discussion pages of of a given course in Moodle. The pattern should occur on a line by itself. The message may contain other text on other lines but pattern will be counted only if occurs on a line by itself.

The program should be generic - should work for any course that you are enrolled for in Moodle, and should take arbitrary text as pattern. You have to decide how to specify the course.

Break the task into a number of sub-steps:

- Take proper command line arguments

- Establish a login session in moodle

- Find the link for the required course on your start page in moodle

- Find the link for Discussion Forum on the course page

- Find the discussion threads links on the discussion page

- For each discussion link, iterate over each post in the link and check if the pattern occurs there

Note that this program can easily be modified to our last week's task - counting on the first thread, or find the first thread that contains the pattern.

The program should be easily modifiable to work for any Course Management System - instead of Moodle, it should work with minimal changes for Piazza or whatever.

Like all submissions, one submission will be due at lab-end. The deadline for final submission will be Saturday 8pm.

You can use the following code as a starting point if you wish:

https://gist.github.com/anonymous/122d1d2965b8e09e97ca9066b4f77ae8






Printing the count of +1 in each discussion thread in News Forum.

a. Location of the page where pattern is present:

Moodle_login_page ==> Course_page ==> CS 699 page ==> News_Forum ==> Discussion

URL: http://moodle.iitb.ac.in/mod/forum/view.php?f=5569

b. Counting the number of +1 done by authors in each discussion page.
pattern = '+1'
Note- count does not include those pattern which are present in between the sentence.

c. Command line arguments : python3 solution.py username password
 eg: python3 solution.py 173050046 xxxxxxx
 

 

