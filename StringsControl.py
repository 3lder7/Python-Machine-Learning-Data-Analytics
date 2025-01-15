#Manipulando elementos dentro das strings
#Também considera espaços em branco

frase = 'Estou gostando do curso'

print(frase[2:7])#da letra de indice 2 ao 7
print(frase[5:])#a partir do 5 ate o final
print(frase[:13])#do inicio ate o final
print(frase[2:13:2])#pulando de 2 em 2

print(frase.count('t'))#quantas letras T
print(frase.count(' '))#quantos espaços

print(len(frase))#tamanho da variável

print(frase.replace('curso', 'aprendizado'))#substitui