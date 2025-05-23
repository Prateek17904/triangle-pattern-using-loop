row=5;
for i in range(1,row+1):
    spaces = row - i;
    stars = 2 * i - 1;
    print(" "*spaces,"*"*stars);