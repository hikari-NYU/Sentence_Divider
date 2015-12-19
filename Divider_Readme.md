#Sentence Divider
####Weicheng Ma
========================================================================================================================

######Description
------------------------------------------------------------------------------------------------------------------------
This program is for dividing a string of words without whitespaces into readable format.
The dictionary used is CMUDICT from NLTK.
Used maximum match method so in some cases the results may be weird.


######Introduction
------------------------------------------------------------------------------------------------------------------------
To run the program, simply type the instruction
 &lt; python Word_Divider.py 
You will see instructions asking for user input,
which being the sentence to divide.
In order to exit, type EXIT(Capitalized).



######Package dependencies:
------------------------------------------------------------------------------------------------------------------------
>The program depend only on NLTK.corpus.cmudict as the dictionary for the words to divide.



######Approach:
------------------------------------------------------------------------------------------------------------------------
1. The program takes the input sentence.
2. The sentence is turned into purely lower case words.
3. Starting from the last letter, the program recursively tries to combine the tail with the letter right in front of it.
4. Once a combination is not found in the dictionary, stop and insert the tail part into a new list.
5. Delete the tail part from the original sentence.
6. Start over from step 3, till the beginning of sentence.
