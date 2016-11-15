def pay(days):
	num_days = len(days)
	if num_days == 0:
		return 0
	elif num_days < 4:
		return num_days*2
	elif num_days >= 23:
		return 25
	else:
		sum_group_day = 0
		#7days
		days, temp = pay2(days, 7)
		sum_group_day += temp
		#6days
		days, temp = pay2(days, 6)
		sum_group_day += temp
		#5days
		days, temp = pay2(days, 5)
		sum_group_day += temp
		#4days
		days, temp = pay2(days, 4)
		sum_group_day += temp


		price = len(days)*2 + sum_group_day*7
		return price

def pay2(days, max_day):
	num_days = len(days)
	group_days = []
	new_days = days
	start_day_index = 0
	x = 0
	while x < num_days:
		if x+max_day > num_days:
			return new_days, len(group_days)
		sum_day = days[x+max_day-1] - days[x]
		if sum_day <= 6 and sum_day >= max_day-1:
			ok_days = days[x:x+max_day]
			new_days = [d for d in new_days if (d not in ok_days)]
			group_days.append(ok_days)
			x = x+max_day
		else:
			x += 1
		
	return new_days, len(group_days)
	
def pay1(days):
	num_days = len(days)
	group_days = []
	count = 0
	start_day_index = 0
	x = 0
	while x < num_days:
		if x+7 <= num_days:
			sum_day = days[x+6] - days[x]
			if sum_day <= 6:
				ok_days = days[x:x+7]
				days = [d for d in days if (d not in ok_days)]
				count += 1
				group_days.append(ok_days)

		elif x+6 <= num_days:
			sum_day = days[x+5] - days[x]
			if sum_day <= 6:
				ok_days = days[x:x+6]
				days = [d for d in days if (d not in ok_days)]
				count += 1
				group_days.append(ok_days)

		elif x+5 <= num_days:
			sum_day = days[x+4] - days[x]
			if sum_day <= 6:
				ok_days = days[x:x+5]
				days = [d for d in days if (d not in ok_days)]
				count += 1
				group_days.append(ok_days)

		elif x+4 <= num_days:
			sum_day = days[x+3] - days[x]
			if sum_day <= 6:
				ok_days = days[x:x+4]
				days = [d for d in days if (d not in ok_days)]
				count += 1
				group_days.append(ok_days)

		else:
			x += 1

		num_days = len(days)
		print("num_days: %d - array: %s" % (num_days, group_days))
		
	return count*7 + len(days)*2



