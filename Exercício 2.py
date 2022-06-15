
print ('-' * 30)
print ('Sequência de Fibonacci')
print ('-' * 30)
n = int (input ('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print ('~' * 30)
print ('A sequência é: ')
print ('{} → {}'.format (t1, t2), end= '')
cont = 3            #contador começa com 3 porque já mostrou o primeiro e segundo termo
while cont <= n:
    t3 = (t1 + t2)
    print (' → {}'.format (t3), end= '')
    t1 = t2
    t2 = t3
    cont = (cont + 1)
print (' → FIM')
