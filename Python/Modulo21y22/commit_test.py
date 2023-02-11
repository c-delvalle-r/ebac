import time
print('This is a test')
print('Second Print')
a = 1
b = 2
print('Resultado=', a+b)

t = time.localtime()
current_time = time.strftime('%H:%M:%S', t)
print(current_time)
