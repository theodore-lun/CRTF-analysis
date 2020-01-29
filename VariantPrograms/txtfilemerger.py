
keepgoing = input('press y to keep entering files')
total_data = ""
while keepgoing == 'y':
	filename = input('enter a filename')
	with open(filename, 'r') as file:
		data = file.read()
		total_data += "\n\n"
		total_data += data

	keepgoing = input('press y to keep entering files')

with open('mergedSequenceFiles.txt', 'x') as mergedfiles:
	mergedfiles.write(total_data)
