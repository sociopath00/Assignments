# Assignments

#Assignment 1
First Assignment (100 marks) 

Problem statement: Write a python script for finding the maximum semantic similarity between the following word pairs (total 50 pairs). Use various semantic similarity packages available in nltk wordnet library to get the maximum similarity. Similarity should be in the range of 0 to 1. (Refer nltk wordnet demo file which is already shared in the first lecture)


(sr no)  (word1)     (word2)         (path_simi) (lch_simi) (wup_simi) (max_simi)

1	computer	keyboard         ?
2	Jerusalem	Israel           ?
.
.
.
50 psychology	cognition


#Assignment 2
Second Assignment (100 marks)

Problem statement: Write a python script using regular expression for extracting the date,  from a text.

Date pattern should consider valid name of months, number of days (1 to 31), number of months (1 to 12) and different styles of writing date patterns.   

Correct date patterns:
        15 November 1989
        October 2013
        16/11/2016
        16.11.2016
        16-11-2016
        2016-11-16,
        9.9.1994
		6.02.2006
    
Incorrect date patterns:
		02-29-2011  ---- (months should be between 1 to 12)
		32-12-2011  ---- (day should be between 1 to 31)
		01@11@2011  ---- (we don't use special symbols like @,#,$,%,^,&,*,*! for writing date pattern)
		Cricket 2013 ---- (cricket is not a month name here)
