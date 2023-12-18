minor = True
Average = False
bigger = False

lista = [1,2,3]

print(type(len(lista)))
print(type(sum(lista)))
def menor():
    minor = True
    m = min(lista)
    return f"o menor número é: {m}"

dicionario = {minor:menor(), 
              bigger:'o menor número é: ', 
              Average:'média'}

for key, value in dicionario.items():
    if key:
        print(value)