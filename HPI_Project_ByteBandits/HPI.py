import random
import matplotlib.pyplot as plt

# Function to recommend a color based on mood
def mood_to_color(mood):
    mood_color_map = {
        'happy': 'yellow',
        'sad': 'blue',
        'relaxed': 'green',
        'excited': 'orange',
        'angry': 'red',
        'confident': 'purple',
        'anxious': 'gray'
    }
    return mood_color_map.get(mood.lower(), 'white')


# Function to provide a motivational message based on mood
def mood_to_message(mood):
    motivational_messages = {
        'happy': "Keep shining, your positivity is contagious!",
        'sad': "It's okay to feel down; brighter days are coming.",
        'relaxed': "Stay in this peaceful flow, great things happen in calmness.",
        'excited': "Channel your energy into something amazing today!",
        'angry': "Take a moment to pause; you can handle this with grace.",
        'confident': "You're unstoppable! Keep conquering your goals.",
        'anxious': "Take a deep breath, you're stronger than you think."
    }
    return motivational_messages.get(mood.lower(), "Stay positive, you're doing great!")


# Function to display the color and motivational message graphically
def display_mood_recommendation(mood):
    color = mood_to_color(mood)
    message = mood_to_message(mood)

    # Create a plot with the color background
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_facecolor(color)
    ax.text(0.5, 0.5, message, fontsize=12, ha='center', va='center', wrap=True)
    # ax.axis('off')  # Turn off the axes

    # hide x-axis
    ax.get_xaxis().set_visible(False)
    # hide y-axis
    ax.get_yaxis().set_visible(False)

    plt.title(f"Your Mood Color: {color.capitalize()}", fontsize=14, pad=20)
    plt.show()


# Example usage
user_mood = input("How are you feeling today? (e.g., happy, sad, relaxed): ")
display_mood_recommendation(user_mood)