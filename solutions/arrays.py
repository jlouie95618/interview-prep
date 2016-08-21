
# 6.5
def delete_duplicates(arr, version = 0):
    print("delete duplicates")
    # Solution's attempt:
    # Runtime: O(n)
    # Space: O(1)
    if version == 0:
        pass
    # First pass attempt:
    # Runtime: O(n^2)
    # Space: O(1)
    elif version == 1:
        curr_index = 0
        # Because python for loops are really for-each loops,
        #   we need to use a while loop to get the intended
        #   "alteration during iteration" approach that we want 
        while curr_index < (len(arr) - 1):
            if arr[curr_index] == None: 
                break
            next_index = curr_index + 1
            if arr[curr_index] == arr[next_index]:
                replace_index = curr_index
                while replace_index < (len(arr) - 1):
                    arr[replace_index] = arr[replace_index + 1]
                    # Set sentinel value for ending outer while loop
                    arr[replace_index + 1] = None
                    replace_index += 1
                curr_index -= 1
            curr_index += 1
        return arr 

# 6.6
def buy_stocks_once(arr):
    pass


