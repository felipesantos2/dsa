# Stack => LIFO Last In First Out

# ['Felipe', 'pinheiro', 'dos', 'Santos']
#
#  Stack, Pilha
#
# O último a entrar é o primeiro a sair
#
# Exatamente igual a uma pilha de pratos. O último prato ensaboado,
# o prato ensaboado mais recentemente é o primeiro a ser enxaguado com água


stack = ["Felipe"]


def push(stack: list, data) -> list:
    stack.append(data)
    return stack


def pop(stack: list) -> list:
    stack.pop()
    return stack


def last(stack)-> int | float | str | list | dict:
    last = len(stack) - 1
    return stack[last]


push(stack, "Pinheiro")
push(stack, "dos")

print(push(stack, "Santos"))
print(pop(stack))

print(last(stack))
