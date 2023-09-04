# Complete the solution so that it returns the number of times the search_text is found within the full_text. Overlap is not permitted : "aaa" contains 1 instance of "aa", not 2.

# Usage example:

# full_text = "aa_bb_cc_dd_bb_e", search_text = "bb"
#     ---> should return 2 since "bb" shows up twice


# full_text = "aaabbbcccc", search_text = "bbb"
#     ---> should return 1

def solution(full_text, search_text):
    count = 0
    search_len = len(search_text)
    if search_text == '':
        count = len(full_text) + 1
    else:
        for i, text in enumerate(full_text):
            if search_text == full_text[i: i + search_len]:
                count += 1
    return count


print(solution("fjkdslfjalksdjlf", ""))
