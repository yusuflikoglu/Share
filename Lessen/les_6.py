# ingredients = ['flour', 'sugar', 'butter', 'apples']
#
# def swapFL(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#
# print(swapFL(ingredients)) pi

# def f(x): #tyd6
#     res = x * 2 + 10
#     print (res)
#
# resultaat = f(2)
# print(resultaat)
# 'kbkk kppi

def pay(x, y): #Excersice 3.32
    if y >= 40:
        return(x*y + (y%40) * 1.5)
    else:
        return(x*y)

print(pay(10,45))
