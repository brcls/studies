import forca
import adivinhacao

print("*********************************")
print("*******Escolha seu jogo!*********")
print("*********************************")

print("(1) Forca (2) Advinhacao")

jogo = int(input("Qual jogo: "))

if jogo == 1:
    print("Jogando jogo da forca")
    forca.jogar()
elif jogo == 2:
    print("Jogando jogo de advinhacao")
    adivinhacao.jogar()