def sum(anyFunc):
    def innerfunc(a,b):
        sum = a + b
        return sum
    return innerfunc




@sum
def add(a,b):
    return a + b
print(add(2,3))