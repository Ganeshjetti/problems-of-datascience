string1 = 'hello'
string2 = 'helle'        
def string_distance(string1, string2):
    if len(string1) < len(string2):
        return string_distance(string2, string1)

    # Initialize the distance to the length of the shorter string
    distance = len(string2)

    # Iterate over each character in the longer string
    for i in range(len(string1)):
        # Find the minimum number of edits needed to match the current substring
        # of string1 with a substring of string2
        min_edits = i
        for j in range(min(i, len(string2)) + 1):
            # Calculate the number of edits needed to match the current
            # substrings of string1 and string2
            edits = 0
            if string1[i - j] != string2[j]:
                edits += 1
            if j > 0:
                edits += min_edits
            min_edits = min(min_edits, edits)

        # Update the distance if a smaller number of edits was found
        distance = min(distance, min_edits)

    return distance
print(string_distance)