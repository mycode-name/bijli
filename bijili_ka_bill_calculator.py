reading = int(input('main meter reading : '))
totalcost = int(input('total cost : '))
beauty= input('beauty(past,present) : ').split(',')
beautyread = int(beauty[1]) - int(beauty[0])
chadi = input('chadi(past,present) : ').split(',')
chadiread = int(chadi[1]) - int(chadi[0])
dada = input('dada(past,present) : ').split(',')
dadaread = int(dada[1]) - int(dada[0])
sony = input('sony(past,present) : ').split(',')
sonyread = int(sony[1]) - int(sony[0])
motor = input('motor(past,present) : ').split(',')
motorread = int(motor[1]) - int(motor[0])
readsum = beautyread + chadiread + dadaread + sonyread + motorread
print(f'sum of all readings = {readsum}')
costpreading = (totalcost/readsum)
print(f'cost per reading = {costpreading}')
motorcost = motorread*costpreading
date = int(input('write down the date : '))


print(f'\nBefore {date}\ncost of motor = {motorcost}')
print(f'beauty\'s cost (room + motor) = {costpreading*beautyread} + {motorcost/4} = {costpreading*beautyread + motorcost/4}')
print(f'chadi\'s cost (room + motor) = {costpreading*chadiread} + {motorcost/4} = {costpreading*chadiread + motorcost/4}')
print(f'dada\'s cost (room + motor) = {costpreading*dadaread} + {motorcost/4} = {costpreading*dadaread + motorcost/4}')
print(f'sony\'s cost (room + motor) = {costpreading*sonyread} + {motorcost/4} = {costpreading*sonyread + motorcost/4}')

aftercost = int(input('\nAfter {date}\nTotal cost with fine : '))
totalfine = aftercost - totalcost
finepread = totalfine/(readsum - motorread)
print(f'beauty\'s cost (room+motor+fine) = {costpreading*beautyread} + {motorcost/4} + {finepread*beautyread} = {costpreading*beautyread + motorcost/4 + finepread*beautyread}')
print(f'chadi\'s cost (room+motor+fine) = {costpreading*chadiread} + {motorcost/4} + {finepread*chadiread} = {costpreading*chadiread + motorcost/4 + finepread*chadiread}')
print(f'dada\'s cost (room+motor+fine) = {costpreading*dadaread} + {motorcost/4} + {finepread*dadaread} = {costpreading*dadaread + motorcost/4 + finepread*dadaread}')
print(f'sony\'s cost (room+motor+fine) = {costpreading*sonyread} + {motorcost/4} + {finepread*sonyread}= {costpreading*sonyread + motorcost/4 + finepread*sonyread}')
