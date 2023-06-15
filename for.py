
palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativa = 0

while True:
    letra_digitada = input('Digite uma letra:')
    numero_tentativa += 1

    if len(letra_digitada) > 1:
        print('digite apenas uma letra:')
        continue

    if letra_digitada in palavra_secreta:
       letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
      if letra_secreta  in letras_acertadas:
         palavra_formada += letra_secreta
      else:
        palavra_formada += '*'

    print('A palavra formada:', palavra_formada)
    
    if palavra_formada == palavra_secreta:
       print('Você ganhou!!')
       print('A palavra era', palavra_formada)
       print('Tentativas:', numero_tentativa)
       letras_acertadas = ''
       numero_tentativa = 0 
    
