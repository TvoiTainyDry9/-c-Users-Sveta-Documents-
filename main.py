
def nod(a, b):
    if a == b:
	return a
    if b > a:
	a, b = b, a
    c = a % b
    if c == 0:
        return b
    else:
	return nod(b, c)


def nok(a, b):
    return a * b // nod(a, b)
    


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(nod(a, b))
    print(nok(a, b))
