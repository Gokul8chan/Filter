from itertools import permutations

def solve_cryptarithmetic(puzzle):
    # Split the puzzle into words and find unique letters
    words = puzzle.split()
    unique_letters = set("".join(words))
    
    # Generate all possible permutations of digits from 0 to 9
    digit_permutations = permutations("0123456789", len(unique_letters))
    
    for perm in digit_permutations:
        # Create a mapping of letters to digits
        letter_to_digit = dict(zip(unique_letters, perm))
        
        # Replace letters with corresponding digits in each word
        digit_words = ["".join([letter_to_digit[letter] for letter in word]) for word in words]
        
        # Check if the puzzle is valid
        if all(int(digit_words[i]) == int(digit_words[i+1]) for i in range(len(digit_words) - 1)):
            return letter_to_digit
    
    return None

# Accept user input for the cryptarithmetic puzzle
if __name__ == "__main__":
    print("Enter the cryptarithmetic puzzle in the format 'WORD1 + WORD2 = WORD3':")
    puzzle = input()
    
    solution = solve_cryptarithmetic(puzzle)
    
    if solution:
        print("Solution found:")
        for letter, digit in solution.items():
            print(f"{letter} = {digit}")
            
    else:
        print("No solution found.")
