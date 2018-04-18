#!usr/bin/env python3
#useless-dl0.py

def teach():
	i=0
	my_list = []
	while True:
		print(my_list)
		term = str(input('enter content to memorize: '))
		term=term.lower().strip()
		my_list.append(term)
		if my_list[0] == term and my_list[i-1] == term:
			i+=1
			if i == 2:
				print('I\'m learning...slowly, I suspect, but surely.')
			if i >= 3:
				print(f'Success...I remember {term}')
				print(my_list)
				carry_on()
		else:
			print('Oops..best start over...\nOr give up...')
			i=0
			del my_list[:]
			carry_on()

def carry_on():
	while True:
		keep_learning = str(input('Keep learning? [y/n]'))
		if keep_learning.lower().strip() != 'y':
			print('thank you. good bye.')
			quit()
		else:
			teach()

if __name__=='__main__':
	teach()
else:
	print(f'no can do. {__name__} won\'t run.') 

