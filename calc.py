#120+22*x+25*y=1488 формула
pasxalko = int(input('Введите желаемое число хп \n'))


shmotki = {
	#50: ['Blood grenade'], 
	125: ['Fluffy hat', 'Spirit vessel'],
	150: ['Pavice'],
	175: ['Point booster', 'Force staff'],
	200: ['Falcon blade', 'Vanguard', 'Phylactery', 'Solar crest', 'Khanda'],
	250: ['Vitality booster', 'Aeon disk', 'Crimson guard'],
	300: ['Rod of atos'],
	275: ['Gleipnir'],
	425: ['Soul Booster'],
	450: ['Bloodstone'],
	500: ['Octarine core']
}


def find_sum(number, terms, current_sum=[], start_index=0):
	# Если текущая сумма равна исходному числу, выводим текущую комбинацию слагаемых
	if sum(current_sum) == number and len(current_sum) <= 6:
		sum_v_shmotkah = []
		for i in current_sum:
			sum_v_shmotkah.append(shmotki.get(i)[0])
		print(sum_v_shmotkah, '\n')
		return
    
    # Если текущая сумма превысила исходное число или достигла его, выходим из рекурсии
	if sum(current_sum) > number or start_index == len(terms):
		return
    
    # Перебираем слагаемые, начиная с start_index
	for i in range(start_index, len(terms)):
		# Добавляем слагаемое к текущей сумме
		current_sum.append(terms[i])
		# Рекурсивно вызываем функцию для поиска следующих слагаемых
		find_sum(number, terms, current_sum, i)
		# Убираем последнее добавленное слагаемое для перехода к следующей итерации
		current_sum.pop()


for i in range(311):
	HP_V_Sile = 120+(22*i)
	HP_V_Shmotkah = (pasxalko - HP_V_Sile)
	shmotok = HP_V_Shmotkah/25
	if HP_V_Shmotkah%25 == 0 and shmotok > 0 and HP_V_Shmotkah<3750:
		print('Варианты шмоток для получения этого хп при ', i, ' силы:')
		find_sum(HP_V_Shmotkah, list(shmotki.keys()))

input()