#!python3
 
"""
Assignment 5:
Make a Mad Lib

Ask the user to enter a number of words, one for each of the underscored words in the following paragraph.  Once they have finished, display the following story to them with the replacements made in the Mad Lib

Today we picked apple from _PERSON_'s Orchard. I had no idea there were so many different varieties of apples. I ate _ADJECTIVE_ apples straight off the tree that tasted like _FOOD_. Then there was a _ADJECTIVE_ apple that looked like a _NOUN_.  When our bag was full, we went on a free hay ride to _PLACE_ and back. It ended at a hay pile where we got to _VERB_ _ADVERB_. I can hardly wait to get home and cook with the apples. We are going to make apple _FOOD_ and _THINGS_ pies!
"""
p = input("Please enter a name of a person")
a = input("Please input an adjective")
f = input("Please input a food item")
aj = input("Please input another adjective")
n = input("Please input a noun")
pl = input("Please input a place")
v = input ("Please input a verb")
ad = input ("Please input an adverb")
fo = input ("Please input another food")
t = input ("Please input a thing")
print(f"Today we picked apple from {p}s Orchard. I had no idea there were so many different varieties of apples. I ate {a} apples straight off the tree that tasted like {f}. Then there was a {ad} apple that looked like a {n}.  When our bag was full, we went on a free hay ride to {pl} and back. It ended at a hay pile where we got to {v} {ad}. I can hardly wait to get home and cook with the apples. We are going to make apple {fo} and {t} pies!")