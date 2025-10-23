#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""
prices = input("Please enter the prices of the 5 items")
fir = 11.99
sec = 14.76
thir = 12.99
four = 15.98
fifth = 7.99
subtotal = fir + sec + thir + four + fifth
taxtotal = subtotal * 0.12
taxtotal = round(taxtotal,2) 
total = subtotal + taxtotal
total = round(total,2)
print (subtotal)
print (taxtotal)
print (total)