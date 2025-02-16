# There are some books on the table. 
# If you group them by 3, you get some number of full groups and 2 books remain; 
# if you group them by 4, you get some number of full groups and 3 books remain; 
# if you group them by 5, you get some number of full groups and 4 books remain. 
# What is the number of books on the table, if it is less than 100?


for n in range(1, 100):
    if n % 3 == 2 and n % 4 == 3 and n % 5 == 4:
        print(n)