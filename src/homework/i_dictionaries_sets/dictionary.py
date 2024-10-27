#
def test_config():
    return True

def get_p_distance (list1, list2):
    #get_p_distance with list parameter list1 and list2
    mismatches = 0
    for i in range (len(list1)):
        if list1[i] != list2[i]:
            mismatches += 1
    return mismatches / len(list1)

def get_p_distance_matrix(dna_list):
    # get_p_distance_matrix with list parameter list1 (
    # see general matric function above for function code)
    # Use the get_p_distance function to get the distance between two lists, 
# save the result to p_distance_matrix[i][j].

    n = len(dna_list)
    p_distance_matrix = [[0.0 for _ in range(n)]for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                p_distance_matrix[i][j] = get_p_distance(dna_list[i], dna_list[j])
    return p_distance_matrix

dna_list = [
    ['T','T','T','C','C','A','T','T','T','A'],
    ['G','A','T','T','C','A','T','T','T','C'],
    ['T','T','T','C','C','A','T','T','T','T'],
    ['G','T','T','C','C','A','T','T','T','A']
]

distance_matrix = get_p_distance_matrix(dna_list)