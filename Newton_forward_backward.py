data = list()

with open('input_data.txt') as f:
    for line in f:
        data.append(list(map(float, line.strip().split())))

n = len(data)

def fact(x, nums = 1):
    factorial = 1
    temp = x - nums
    while x > temp:
        factorial *= x
        x = x - 1
    return factorial
 
def del_gen(num):
    
    cache = list()
    last_cache = [x[1] for x in data]
    
    for i in range(num):
        temp_cache = last_cache
        in_cache = list()
        
        for j in range(len(temp_cache) - 1):
            in_cache.append(temp_cache[j + 1] - temp_cache[j])
            
        last_cache = in_cache
        cache.append(in_cache)
        
    return cache

def newton(val, forward = True):
    if forward:
        a = data[0][0]
        for i in range(n):
            if val < data[i][0]:
                a = data[i - 1][0]
                index = i - 1
                break
        u = (val - a)/(data[1][0] - data[0][0])
        k = data[index][1]
        
        delta = del_gen(n - index - 1)
        for i in range(n - index - 1):
            k += fact(u, i + 1)/fact(i + 1, i) * delta[i][index]
        
        return k
        
    else:
        #backward
        a = data[0][0]
        for i in range(n):
            if val < data[i][0]:
                a = data[i][0]
                index = i
                break
        u = (val - a)/(data[1][0] - data[0][0])
        k = data[index][1]
        delta = del_gen(index)
        for i in range(index):
            k += fact(u + i, i + 1)/fact(i + 1, i) * delta[i][index - i - 1]
        
        return k
    
print('x     y')
for (i,j) in data:
    print(i, j)


num = float(input('What do you want to predict?'))

if num < data[len(data)//2][0]:
    print(newton(num))
else:
    print(newton(num, False))
  
