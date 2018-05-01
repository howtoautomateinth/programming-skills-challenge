n = 8
l = ['1','2','3','4','5','6','7','8','9','10']
for idx in range(n):
	print((n-idx) * ' ' + ''.join(l[:idx]) + ''.join(l[idx::-1]), end='')
	print()
for idx in range(n,-1,-1):
	print((n-idx) * ' ' + ''.join(l[:idx]) + ''.join(l[idx::-1]))