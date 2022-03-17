import subprocess

bashCommand = "./most_active_cookie data.csv -d 2018-12-09"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)
print(error)

bashCommand = "./most_active_cookie data.csv -e 2018-12-09"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)
print(error)

bashCommand = "./most_active_cookie data.cp -d 2018-12-09"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)
print(error)