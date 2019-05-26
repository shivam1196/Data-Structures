"""
A program to check whether two given strings are anagrams of one another or not.

An anagram is a word (or phrase) that is formed by rearranging the letters of another word (or phrase).

For example:

"rat" is an anagram of "art"
"alert" is an anagram of "alter"
"Slot machines" is an anagram of "Cash lost in me"
"""

"""
check_for_anagram


"""


def check_for_anagram(string_one, string_two):
    list_from_string_one = []
    list_from_string_two = []
    isAnagram = bool

    for i in range(len(string_one)):
        list_from_string_one.append(string_one[i])

    for i in range(len(string_two)):
        list_from_string_two.append(string_two[i])

    list_from_string_one.sort()
    list_from_string_two.sort()

    if len(list_from_string_one) != len(list_from_string_two):
        print("The words are not anagrams")
        return


    else:
        for i in range(len(list_from_string_one)):
            if list_from_string_one[i] != list_from_string_two[i]:

                isAnagram = False
            else:
                continue

    if (isAnagram):
        print ("The two words are anagrams")

    else:
        print("The two words are not anagrams")


def check_for_anagrams_optimised(string_one, string_two):
    hash_list_for_string_one = [0] * 26
    hash_list_for_string_two = [0] * 26

    string_one.lower()

    string_two.lower()

    if len(string_one) != len(string_two):
        print("Two words are not anagrams")
        return

    else:
        for i in range(len(string_one)):
            index_to_store = ord(string_one[i]) - ord('a')
            hash_list_for_string_one[index_to_store] = hash_list_for_string_one[index_to_store] + 1
            index_for_second_list = ord(string_two[i]) - ord('a')
            hash_list_for_string_two[index_for_second_list] = hash_list_for_string_two[index_for_second_list] + 1

    print (hash_list_for_string_one)
    print("Hash List")
    print (hash_list_for_string_two)


#check_for_anagrams_optimised("alter", "alert")

check_for_anagrams_optimised("Shivam", "Anirud")
