a1 = [10, 45, 2, 56, 12, 34, 90, 27]
a2 = [45, 1, 89, 77, 2, 90, 100]

def commonElementsInArrays(a1,a2):
    new_a1 = sorted(a1)
    new_a2 = sorted(a2)
    result = []
    for i in new_a1:
        if i in new_a2:
            result.append(i)            
    print(sorted(result))    


commonElementsInArrays(a1,a2)
