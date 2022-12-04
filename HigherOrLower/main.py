import art
import game_data
import random

game_over = False
dict_size = len(game_data.data)
used_list = []
score = 0
message = ""


def draw_unique():
    while dict_size != len(used_list):
        choice = random.randint(0, dict_size - 1)
        if choice not in used_list:
            used_list.append(choice)
            return choice


def compare(persin1, person2, answer):
    if answer == "b" and person2['follower_count'] > person1['follower_count']:
        return True
    elif answer == "a" and person2['follower_count'] < person1['follower_count']:
        return True
    else:
        return False


person1 = game_data.data[draw_unique()]

while not game_over:
    print(art.logo)

    if message != "":
        print(message)
    print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}.")

    print(art.vs)

    person2 = game_data.data[draw_unique()]
    if person2 != None:
        print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}.")
    else:
        message = f"Sorry, end of questions. Final score: {score}"
        game_over = True

    answer = input("Who has more followers? Type 'A' or 'B'; ").lower()
    result = compare(person1, person2, answer)
    if result:
        score += 1
        person1 = person2
        message = f"You're right! Current score: {score}"
    else:
        message = f"Sorry, that's wrong. Final score: {score}"
        game_over = True
print(message)