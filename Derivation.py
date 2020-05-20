delta = float(input("Delta değeri : ")) # The amount of change in x
degree = int(input("Fonksiyonun en büyük derecesini giriniz")) +1 # function degree
point = float(input("X değeri : ")) # The x point

weights_list = [] # to storage the weights

for i in range(degree):
    weights_list.append(float(input("Fonksiyonun X üzeri {}. ağırlığı".format(i)))) # inputing the weights , first one bias

fx = 0

def f(degree,fx,weights_list,point):
    for i in range(degree):
        fx = fx + weights_list[i] * (point ** i)
    return fx

central_derivation = (f(degree,fx,weights_list,(point+delta)) - f(degree,fx,weights_list,(point-delta)))/2*delta
print(central_derivation)

forward_derivation = (f(degree,fx,weights_list,(point+delta)) - f(degree,fx,weights_list,point))/delta
print(forward_derivation)

backward_derivation = (f(degree,fx,weights_list,point) - f(degree,fx,weights_list,(point-delta)))/delta
print(backward_derivation)

