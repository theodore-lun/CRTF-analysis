with open("ENST00000648260.1.txt", 'r+') as file:
    sequence = file.read().replace('\n', '')
    variantLocation = int(input('Variant location?'))
    replacement = input('What is replaced?')
    
    #for point mutations, deletions
    variant = sequence[0:(variantLocation - 117480011 + 1)] + replacement + sequence[(variantLocation - 117480011 + 2):(117627910-117480011)]

    #for insertions
    insertion = input('What is inserted')
    variant = sequence[0:(variantLocation - 117480011 + 1)] + replacement + sequence[(variantLocation - 117480011 + 1):(117627910-117480011)]

#copies variant data into new file 
variantName = input ('What is variant ID?')
with open(variantName + '.txt', 'x') as variantFile:
    variantFile.write(variant)
