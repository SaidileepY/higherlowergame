import random
from art import logo,vs
from game_data import data
account_b=random.choice(data)
print(logo)
count=0
game_should_continue=True
while game_should_continue:
    def format_data(account):
        account_name=account["name"]
        account_desc=account["description"]
        account_country=account["country"]
        return f"{account_name},a {account_desc}, from {account_country}"

    def check_answer(user_guess,a_followers,b_followers):
        if a_followers>b_followers:
            return user_guess=="a"
        else:
            return user_guess=="b"

    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)

    print(f"Compare A:{format_data(account_a)}.")
    print(vs)
    print(f"Against B:{format_data(account_b)}.")
    guess=input("Who has more followers? Type 'A' or 'B':").lower()
    print("\n"*20)
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    is_correct=check_answer(guess,a_follower_count,b_follower_count)
    if is_correct:
        count+=1
        print(f"You're right. Your current score is {count}")
    else:
        print(f"Sorry, that's wrong. Your final score is {count}")
        game_should_continue=False


