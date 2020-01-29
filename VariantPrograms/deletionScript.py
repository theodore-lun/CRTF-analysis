with open("ENST00000648260.1.txt", 'r+') as file:
    sequence = file.read().replace('\n', '')

    variant = sequence[0:(117480082 - 117480011 )] + 'C' + sequence[(117480104 - 117480011 + 2):(117627910-117480011)]

variantName = input ('What is variant ID?')

with open(variantName + '.txt', 'x') as variantFile:
    variantFile.write(variant)
