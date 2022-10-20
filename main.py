fibo_list = [0, 1]



x1,x2 = 0, 1



for i in range(15):

    x = x2 + x1

    x1 = x2

    x2 = x

    fibo_list.append(x)
print(fibo_list)