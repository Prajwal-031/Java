import random

def get_random_quote():
    quotes = [
        "The best way to predict the future is to invent it. - Alan Kay",
        "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "If you can dream it, you can achieve it. - Zig Ziglar",
        "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt"
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    print("Here is your inspirational quote for the day:")
    print(get_random_quote())