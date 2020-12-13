# crie um programa que leia um numero e mostre a sua tabuada
print("-" * 12)
num = int(input("Digite um número: "))
for i in range(1, 13):
    print("\33[1;31m{}\33[m X \33[1;32m{:2}\33[m = \33[1;33m{}\33[m".format(num, i, num * i))
print("-" * 12)
