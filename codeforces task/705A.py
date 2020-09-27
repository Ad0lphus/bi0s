n = int(input())
feelings = ['I hate', 'I love']
print(' that '.join([feelings[i % 2] for i in range(n)]) + ' it')
