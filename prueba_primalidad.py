def es_primo(numero):
    contador = 0
    for num in range(numero):
        if numero % (num+1) != 0:
            continue
        else:
            contador += 1
    if contador == 2:
        print('El número es primo')
    else:
        print('el número no es primo')


def run():
    entrada = int(input('Por favor, ingrese un número: '))
    es_primo(entrada)


if __name__ == '__main__':
    run()
