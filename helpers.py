'''
This module will contain useful functions classes
for use in the connect 4 game

'''

# Returns whether there are n consecutive non-zero tokens
# Returns token id (int) if found, else returns 0
def checkConsecutive(aList, n):
    if len(aList) < n:
        return 0
    # Set 1st element as prev
    count = 1
    prev = aList[0]  
    for i in range(1, len(aList)):
        curr = aList[i]
        if curr == 0:
            count = 0
        elif prev != curr:
            count = 1
        else:
            count += 1
        # Check Count
        if count >= n:
            return prev
        # Set new prev
        prev = curr
    return 0
