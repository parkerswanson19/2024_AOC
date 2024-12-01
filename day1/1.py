def find_total_distance(list1, list2):
    list1.sort()
    list2.sort()

    total_distance = 0

    for i, j in zip(list1, list2):
        total_distance += abs(int(i) - int(j))

    return total_distance

def find_similarity_score(list1, list2):
    list1_freq = {}

    for item in list1:
        if item in list1_freq:
            list1_freq[item] += 1
        else:
            list1_freq[item] = 1

    similarity_score = 0
    for item in list2:
        if item in list1_freq:
            similarity_score += list1_freq[item] * int(item)

    return similarity_score



def parse_input_file(input_file):
    l1 = []
    l2 = []
    for line in open(input_file,'r'):
        item1, item2 = line.split()
        l1.append(item1)
        l2.append(item2)

    return (l1, l2)

l1, l2 = parse_input_file("./input.txt")
print(find_total_distance(l1, l2))
print(find_similarity_score(l1, l2))


