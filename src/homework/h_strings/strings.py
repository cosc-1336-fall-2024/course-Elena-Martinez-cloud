#
def get_hamming_distance(dna1, dna2):
    count = 0
    for i in range (len(dna1)):
        if dna1[i] != dna2[i]:
            count += 1
    return count


def get_dna_complement(dna):
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    reverse_complement = ""
    for base in dna[::-1]:
        reverse_complement += complement[base]
    return reverse_complement


