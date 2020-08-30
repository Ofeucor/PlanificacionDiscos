#!/usr/bin/python3

import sys, os
from pythonlangutil.overload import Overload

commands = "Mete mierda"
pl = ['FCFS','S-CAM','C-CAM','S-LOOK','C-LOOK','SSTF']

def main(argv):
	if len(argv) == 1:
		print(commands)
	elif len(argv) >= 3:
		#try:
			if argv[1][0] == '-':
				argv[1] = argv[1][1::]
			numbers = correct_list(argv[2])
			if not(argv[1] in pl) or numbers == False:
				print(commands, "FOMRAT")
			else:
				if argv[1] == 'FCFS':
					FCFS(numbers)
				if argv[1] == 'S-CAM':
					try:
						if len(argv) == 4:
							SCAM(numbers, True, int(argv[3]))
						else:
							if argv[3] == '+':
								SCAM(numbers, True, int(argv[4]))
							elif argv[3] == '-':
								SCAM(numbers, False, int(argv[4]))
					except: 
						print(commands, "ERRRo")
				if argv[1] == 'C-CAM':
					try:
						if len(argv) == 4:
							CCAM(numbers, True, int(argv[3]))
						else:
							if argv[3] == '+':
								CCAM(numbers, True, int(argv[4]))
							elif argv[3] == '-':
								CCAM(numbers, False, int(argv[4]))
					except: 
						print(commands, "ERRRo")
				if argv[1] == 'S-LOOK':
					try:
						if len(argv) == 4:
							SLOOK(numbers, True, int(argv[3]))
						else:
							if argv[3] == '+':
								SLOOK(numbers, True, int(argv[4]))
							elif argv[3] == '-':
								SLOOK(numbers, False, int(argv[4]))
					except: 
						print(commands, "ERRRo")
				if argv[1] == 'C-LOOK':
					try:
						if len(argv) == 4:
							CLOOK(numbers, True, int(argv[3]))
						else:
							if argv[3] == '+':
								CLOOK(numbers, True, int(argv[4]))
							elif argv[3] == '-':
								CLOOK(numbers, False, int(argv[4]))
					except: 
						print(commands, "ERRRo")
				if argv[1] == 'SSTF':
					sstf(numbers)

		#except:
		#	print(commands, "ERRRo")
	else:
		print(commands,"inic")


def FCFS(numbers):
	print("FCFS\n")
	new_list = numbers[:]
	new_list.sort()
	distance =	recorrer(new_list, numbers, int(numbers[0]))
	print("la distancia es de : ", distance)


def SCAM(numbers, mov, tam):
	print("S-CAM\n")
	new_list = numbers[:]
	new_list.sort()
	distance = 0
	if mov:
		lit = new_list[:new_list.index(numbers[0])]
		big = new_list[new_list.index(numbers[0]):]
		lit = lit[::-1]
		new_list.append(tam)
		big.append(tam)
		distance += recorrer(new_list, big, int(numbers[0]))
		if lit:
			distance += recorrer(new_list, lit, tam)
	else: 
		lit = new_list[:new_list.index(numbers[0])+1]
		big = new_list[new_list.index(numbers[0])+1:]
		lit = lit[::-1]
		new_list.insert(0,0)
		lit.append(0) 
		distance += recorrer(new_list, lit, int(numbers[0]))
		if big:
			distance += recorrer(new_list, big, 0)
	print("la distancia es de : ", distance)


def CCAM(numbers, mov, tam):
	print("C-CAM\n")
	new_list = numbers[:]
	new_list.sort()
	distance = 0
	if mov:
		lit = new_list[:new_list.index(numbers[0])]
		big = new_list[new_list.index(numbers[0]):]
		if lit:
			big.append(tam) 
			new_list.append(tam)
			new_list.insert(0,0)
			lit.insert(0,0) 
			distance +=  recorrer(new_list, big, int(numbers[0])) + tam + recorrer(new_list, lit, 0)
		else:
			distance += recorrer(new_list, big, int(numbers[0]))
	else: 
		lit = new_list[:new_list.index(numbers[0])+1]
		big = new_list[new_list.index(numbers[0])+1:]
		lit = lit [::-1]
		big = big[::-1]
		if big:
			lit.append(0) 
			new_list.append(tam)
			new_list.insert(0,0)
			big.insert(0,tam)
			distance += recorrer(new_list, lit, int(numbers[0])) + tam + recorrer(new_list, big, tam)
		else:
			distance += recorrer(new_list, lit, int(numbers[0]))

	print("la distancia es de : ", distance)


def SLOOK(numbers, mov, tam):
	print("S-LOOK\n")
	new_list = numbers[:]
	new_list.sort()
	distance = 0
	if mov:
		lit = new_list[:new_list.index(numbers[0])]
		big = new_list[new_list.index(numbers[0]):]
		lit = lit [::-1]
		if lit:
			distance +=  recorrer(new_list, big, int(numbers[0])) + recorrer(new_list, lit, int(big[-1]))
		else:
			distance += recorrer(new_list, big, int(numbers[0]))
	else: 
		lit = new_list[:new_list.index(numbers[0])+1]
		big = new_list[new_list.index(numbers[0])+1:]
		lit = lit [::-1]
		if lit:
			distance +=  recorrer(new_list, lit, int(numbers[0])) + recorrer(new_list, big, int(lit[-1]))
		else:
			distance += recorrer(new_list, lit, int(numbers[0]))

	print("la distancia es de : ", distance)

def CLOOK(numbers, mov, tam):
	print("C-LOOK\n")
	new_list = numbers[:]
	new_list.sort()
	distance = 0
	if mov:
		lit = new_list[:new_list.index(numbers[0])]
		big = new_list[new_list.index(numbers[0]):]
		if lit:
			distance +=  recorrer(new_list, big, int(numbers[0])) + (int(big[-1]) - int(lit[0])) + recorrer(new_list, lit, int(lit[0]))
		else:
			distance += recorrer(new_list, big, int(numbers[0]))
	else: 
		lit = new_list[:new_list.index(numbers[0])+1]
		big = new_list[new_list.index(numbers[0])+1:]
		big = big [::-1]
		lit = lit [::-1]
		if lit:
			distance +=  recorrer(new_list, lit, int(numbers[0])) + (int(big[0]) - int(lit[-1])) + recorrer(new_list, big, int(big[0]))
		else:
			distance += recorrer(new_list, lit, int(numbers[0]))

	print("la distancia es de : ", distance)

def sstf(numbers):
	print("C-LOOK\n")
	distance = 0
	origen = numbers[0]
	new_list = numbers[:]
	new_list.sort()
	numbers.sort()
	while numbers:
		p0 = numbers.index(origen)
		for i in range(0, new_list.index(origen)):
				print("\t", end = '')
		print(origen)
		origen = nearlest(p0, numbers)
		if origen != None:
			distance += abs(int(origen) - int(numbers[p0]))
		numbers.remove(numbers[p0])
	print("la distancia es de : ", distance)




def recorrer(sortedlist, list, origen):
	distance = 0
	while len(list) != 0:
			for i in range(0, sortedlist.index(list[0])):
				print("\t", end = '')
			print(list[0])
			distance += abs(origen - int(list[0]))
			origen = int(list[0])
			list = list[1:]
	return distance

def nearlest(p0, numbers):
	if len(numbers) == 1:
		return None
	elif len(numbers) == 2:
		if p0 == 0:
			return numbers[1]
		else:
			return numbers[0]
	else:
		if (abs((int(numbers[p0]) - int(numbers[p0+1]))) <= abs((int(numbers[p0]) - int(numbers[p0-1])))):
			return numbers[p0+1]
		else:
			return numbers[p0-1]

def correct_list(lista):
	if (lista[0] == '[' and lista[-1] == ']'):
		lista = lista[1:-1:]
		lista = lista.split(',')
		for i in lista:
			if not(i.isnumeric()):
				return False
		return lista
	else:
		return False

if __name__ == "__main__":
	main(sys.argv)
	sys.exit(0)