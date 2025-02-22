# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    final_perm = []
    # Base case is when sequence is a single char
    if (len(sequence) == 1):
        return [sequence]
    else:
        first_alpha = sequence[0]
        for p in get_permutations(sequence[1:]):
            for i in range(len(p) + 1):
                final_perm.append(p[:i] + first_alpha + p[i:])
    return final_perm
            
            

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    input1 = 'abc'
    print('Input One:', input1)
    print('Expected Output One:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output One:', get_permutations(input1))
    
    input2 = 'xyz'
    print('Input Two:', input2)
    print('Expected Output Two:', ['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx'])
    print('Actual Output Two:', get_permutations(input2))
    
    input3 = 'rs'
    print('Input Three:', input2)
    print('Expected Output Three:', ['rs', 'sr'])
    print('Actual Output Three:', get_permutations(input3))
    