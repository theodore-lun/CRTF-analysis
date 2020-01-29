with open("ENST00000648260.1.txt", 'r+') as file:
    sequence = file.read().replace('\n', '')

    variant = sequence[0:(117480082 - 117480011 )] + 'C' + sequence[(117480104 - 117480011 + 2):(117627910-117480011)]

variantName = input ('What is variant ID?')

with open(variantName + '.txt', 'x') as variantFile:
    variantFile.write(variant)

#range=chr7:117480011-117627910
#>hg38_knownGene_ENST00000648260.1 range=chr7:117480011-117627910 5'pad=0 3'pad=0 strand=+ repeatMasking=none
#ENST00000648260.1
#genomicedittest.txt