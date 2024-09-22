input_num = int(input('Enter a number to print its Math table:'))

for i in range(1,21) :
    print('%d * %-2d = %-3d'%(input_num,i,input_num*i))