import random


def problems_to_be_solved(seed_value, name, no_of_problems, sample):
    random.seed(seed_value)
    practice = range(1, no_of_problems + 1)

    problem_list = random.sample(practice, k=sample)
    to_be_solved_list = sorted(problem_list)
    print(f"{name} is going to solve this list: {to_be_solved_list}")

    print(f"Length of practice list: {len(problem_list)}")
    print(f"Length of sorted practice list: {len(to_be_solved_list)}")


#
# problems_to_be_solved(100, "Farhaan")
# problems_to_be_solved(29, "Azwad")
# problems_to_be_solved(57, "Shuvom")
# problems_to_be_solved(70, "Samuel")
problems_to_be_solved(20, "Showrin", 281, 50)
problems_to_be_solved(20, "Showrin", 80, 40)
