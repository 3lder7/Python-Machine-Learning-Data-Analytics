kmh= [40, 50, 56, 64, 73, 79, 85, 96, 100, 120] #lista de km por hora

#converter para milhas por hora: (dividir todos por 1,61)
mph = []
for i in kmh:
    mph.append(i/1.61)
print(mph)

#sem loop for:
mph2 = list(map(lambda x: x/1.6, kmh))
print(mph2)