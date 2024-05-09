from itertools import permutations

def solve_cryptarithmetic(puzzle):
    letters = set("".join(puzzle))
    
    if len(letters) > 10:
        return "Too many letters for unique digit assignment."

    for perm in permutations(range(10), len(letters)):
        if all(perm[puzzle[i].index(puzzle[i][0])] != 0 for i in range(len(puzzle))):
            mapping = dict(zip(letters, perm))
            num1 = int("".join([str(mapping[c]) for c in puzzle[0]]))
            num2 = int("".join([str(mapping[c]) for c in puzzle[1]]))
            num3 = int("".join([str(mapping[c]) for c in puzzle[2]]))

            if num1 + num2 == num3:
                return mapping

    return "No solution found."


def main():
    print("Example : \nFirst word + Second word = Third word")
    a = input("Enter the first word: ")
    b = input("Enter the second word: ")
    c = input("Enter the third word: ")
    puzzle = [a, b, c]
    solution = solve_cryptarithmetic(puzzle)
    print(solution)

if __name__ == "__main__":
    main()
