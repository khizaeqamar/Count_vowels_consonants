# Count Vowels & Consonants
def count_vow_conso(UserInput):
    # Define vowels
    vowels = "AEIOUaeiou"
    vowels_count = 0
    consonants_count = 0

    for eachchr in UserInput:
        if eachchr.isalpha():
            if eachchr in vowels:
                vowels_count += 1
            else:
                consonants_count += 1

    return vowels_count, consonants_count


# Function call
vowels, consonants = count_vow_conso("Khizar Qamar")
print(vowels, consonants)


