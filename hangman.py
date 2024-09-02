import random
from hangman_word import word_list
from hangman_art import stages,logo
print(logo)
word_generated=random.choice(word_list)
number_of_blank=len(word_generated)
blank_printed=[]
for i in word_generated:
    blank_printed.append("_")
number_lives = len(stages)-1
while number_lives>0 and number_of_blank>0:
 user_input=input("\nguess word: ")
 j=0
 k=0
 while j<len(word_generated):
   if user_input==word_generated[j]:
      blank_printed[j]=user_input
      k+=1
      number_of_blank-=1
   j+=1
 if k==0:
    number_lives-=1
 print(stages[number_lives])   
 for i in range(0,len(word_generated)):  
    print(blank_printed[i], end='')
if number_of_blank==0:
   print("\nyou won")
print("\ngame over")
