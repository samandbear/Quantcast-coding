import sys
import datetime
import collections

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

def check_args_size():
	if len(sys.argv) != 4:
		raise Exception("Not enough input")
	# make sure the input file is in valid .csv format
	if not sys.argv[1].endswith(".csv"):
		raise Exception("Wrong input format")

	if sys.argv[2] != "-d":
		raise Exception("parameter")

	validate(sys.argv[3])

	return sys.argv[1], sys.argv[3]


if __name__ == '__main__':
	csv, time = check_args_size()
	with open(csv) as file:
		rows = file.readlines()
		ans = []
		for row in rows:
			cookie, init_time = row.split(',')
			init_time = init_time[0:10]
			if init_time == sys.argv[3]:
				ans.append(cookie)
		mul = collections.Counter(ans)
		final = []
		maxval = 0

		for value, time in mul.items():
			if time > maxval:
				maxval = time

		for value, time in mul.items():
			if time == maxval:
				final.append(value)

		for cookie in final:
			print(cookie)

	



