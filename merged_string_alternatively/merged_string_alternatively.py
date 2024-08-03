#!/usr/bin/python3

def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """

    merged_string = ""
    word1Length = len(word1)
    word2Length = len(word2)
    

    shorter = findTheShorterString(word1= word1, word2=word2)
    longer = findTheLongerString(word1=word1, word2=word2)

    if word1Length == word2Length:
        for i in range(0, word1Length):
            merged_string = merged_string + word1[i]
            merged_string = merged_string + word2[i]
        
        return merged_string

    for x in range(0, len(shorter)):
        merged_string = merged_string + word1[x]
        merged_string = merged_string + word2[x]
    
    current_position = int(len(merged_string)/2)

    merged_string = merged_string + longer[current_position:]

    return merged_string

        
def findTheShorterString(word1, word2) -> str:
    if len(word1) > len(word2):
        return word2
    
    return word1

def findTheLongerString(word1, word2) -> str:
    if len(word1) > len(word2):
        return word1
    
    return word2





print( mergeAlternately(word1="ab", word2="pqrs") )