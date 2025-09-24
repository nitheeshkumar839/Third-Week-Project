"""
import random

# Dictionary mapping moods/events to outfit suggestions
outfit_data = {
    "happy": [
        ("Yellow", "a bright yellow t-shirt with denim jeans"),
        ("Green", "a fresh green dress or casual shirt"),
    ],
    "calm": [
        ("Blue", "a soft blue hoodie with joggers"),
        ("White", "a white kurta or casual shirt"),
    ],
    "confident": [
        ("Red", "a bold red shirt with black jeans"),
        ("Black", "a sleek black suit or blazer"),
    ],
    "energetic": [
        ("Yellow", "a yellow sports tee with shorts"),
        ("Red", "a red top with blue jeans"),
    ],
    "stressed": [
        ("Blue", "a calming blue sweater with trousers"),
        ("White", "a white t-shirt with comfy track pants"),
    ],
    "interview": [
        ("Black", "a black blazer with white shirt and trousers"),
        ("Blue", "a navy blue formal shirt with black pants"),
    ],
    "date": [
        ("Red", "a red dress or red shirt with black jeans"),
        ("White", "a white outfit with elegant accessories"),
    ],
    "party": [
        ("Black", "a black sequin dress or a black leather jacket"),
        ("Yellow", "a vibrant yellow shirt with stylish jeans"),
    ],
    "casual outing": [
        ("Green", "a green casual shirt with chinos"),
        ("Blue", "a blue t-shirt with denim shorts"),
    ]
}


def get_outfit(user_input):
    user_input = user_input.lower()
    if user_input in outfit_data:
        color, suggestion = random.choice(outfit_data[user_input])
        return f"Based on your {user_input}, try wearing {suggestion} ({color} is perfect for this!)."
    else:
        return "Sorry, I don't have outfit ideas for that. Try moods like happy, calm, confident, energetic, stressed or events like interview, date, party, casual outing."


# Main Program
print("Welcome to the Color Psychology Outfit Recommender!")
print("You can enter your mood (happy, calm, confident, energetic, stressed) or event (interview, date, party, casual outing).")

user_input = input("Enter your mood or event: ")
recommendation = get_outfit(user_input)
print("\n" + recommendation)
"""


import random

# Dictionary mapping moods/events to outfit suggestions
outfit_data = {
    "happy": [
        ("Yellow", "a bright yellow t-shirt with denim jeans"),
        ("Green", "a fresh green dress or casual shirt"),
    ],
    "calm": [
        ("Blue", "a soft blue hoodie with joggers"),
        ("White", "a white kurta or casual shirt"),
    ],
    "confident": [
        ("Red", "a bold red shirt with black jeans"),
        ("Black", "a sleek black suit or blazer"),
    ],
    "energetic": [
        ("Yellow", "a yellow sports tee with shorts"),
        ("Red", "a red top with blue jeans"),
    ],
    "stressed": [
        ("Blue", "a calming blue sweater with trousers"),
        ("White", "a white t-shirt with comfy track pants"),
    ],
    "interview": [
        ("Black", "a black blazer with white shirt and trousers"),
        ("Blue", "a navy blue formal shirt with black pants"),
    ],
    "date": [
        ("Red", "a red dress or red shirt with black jeans"),
        ("White", "a white outfit with elegant accessories"),
    ],
    "party": [
        ("Black", "a black sequin dress or a black leather jacket"),
        ("Yellow", "a vibrant yellow shirt with stylish jeans"),
    ],
    "casual outing": [
        ("Green", "a green casual shirt with chinos"),
        ("Blue", "a blue t-shirt with denim shorts"),
    ]
}


def get_outfit(user_input):
    user_input = user_input.lower()
    if user_input in outfit_data:
        color, suggestion = random.choice(outfit_data[user_input])
        return f"Based on your {user_input}, try wearing {suggestion} ({color} is perfect for this!)."
    else:
        return "Sorry, I don't have outfit ideas for that."


# Main Program with loop
print("🎨 Welcome to the Color Psychology Outfit Recommender! 🎽👗")
print("Available moods/events: happy, calm, confident, energetic, stressed, interview, date, party, casual outing")

while True:
    user_input = input("\n👉 Enter your mood/event (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("👋 Thanks for using the Outfit Recommender. Stay stylish!")
        break

    recommendation = get_outfit(user_input)
    print(recommendation)
