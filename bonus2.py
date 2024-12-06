def my_sort(my_list: [int]) -> [int]:
    result = my_list.copy() # Copie de la liste pour ne pas modifier l'originale
    n = len(result)
    
    for i in range(n):
        for j in range(n - 1):
            # Echange les éléments si le précédent est plus grand
            if result[j] > result[j + 1]:
                # Si le précédent est plus grand, on les échange de place
                result[j], result[j + 1] = result[j + 1], result[j]
    
    return result

# Tests
if '__main__' == __name__:
    test_list = [2, 6, 1, 9, 3]
    sorted_list = my_sort(test_list)
    print(f"Original list: {test_list}")
    print(f"Sorted list: {sorted_list}")
    

# source et documentation: https://www.geeksforgeeks.org/bubble-sort/