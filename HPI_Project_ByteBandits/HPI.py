# Mood Art Generator
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0

import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def get_mood_palette(mood):
    """
    Returns a color palette, shape type, and motivational message for a given mood.

    Args:
        mood (str): The user's mood.
    
    Returns:
        tuple: (list of colors, shape type, motivational message)
    """
    palettes = {
        'happy': (['#FFFF00', '#FFD700', '#FFA500'], 'circle', "Keep shining, your positivity is contagious!"),
        'sad': (['#0000FF', '#1E90FF', '#87CEEB'], 'rectangle', "It's okay to feel down; brighter days are coming."),
        'relaxed': (['#00FF00', '#32CD32', '#98FB98'], 'circle', "Stay in this peaceful flow, great things happen in calmness."),
        'excited': (['#FFA500', '#FF4500', '#FFD700'], 'triangle', "Channel your energy into something amazing today!"),
        'angry': (['#FF0000', '#8B0000', '#FF6347'], 'rectangle', "Take a moment to pause; you can handle this with grace."),
        'confident': (['#800080', '#4B0082', '#9932CC'], 'triangle', "You're unstoppable! Keep conquering your goals."),
        'anxious': (['#808080', '#A9A9A9', '#696969'], 'rectangle', "Take a deep breath, you're stronger than you think.")
    }
    # Return None if the mood is not recognized
    return palettes.get(mood.lower(), None)

def draw_mood_art(mood):
    """
    Generates and displays a piece of mood-based generative art with a motivational message.

    Args:
        mood (str): The user's mood.

    Returns:
        None
    """
    # Get the mood palette
    mood_data = get_mood_palette(mood)
    if mood_data is None:
        # Notify the user if the mood is not recognized
        print(f"Sorry, I don't recognize the mood '{mood}'. Please try again with a valid mood.")
        print("Valid moods are: happy, sad, relaxed, excited, angry, confident, anxious.")
        return  # Stop the function if the mood is not recognized

    # Extract colors, shape type, and motivational message
    colors, shape_type, message = mood_data

    # Create a blank canvas
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')  # Hide axes for a clean look

    # Draw random shapes
    for _ in range(30):  # Generate 30 shapes
        x, y = random.uniform(0, 1), random.uniform(0, 1)  # Random position
        color = random.choice(colors)  # Random color from the palette

        if shape_type == 'circle':
            radius = random.uniform(0.02, 0.1)  # Random size
            circle = patches.Circle((x, y), radius, color=color, alpha=0.7)
            ax.add_patch(circle)

        elif shape_type == 'rectangle':
            width, height = random.uniform(0.02, 0.1), random.uniform(0.02, 0.1)
            rectangle = patches.Rectangle((x, y), width, height, color=color, alpha=0.7)
            ax.add_patch(rectangle)

        elif shape_type == 'triangle':
            size = random.uniform(0.02, 0.1)
            triangle = patches.Polygon([
                (x, y), 
                (x + size, y), 
                (x + size / 2, y + size * 0.866)
            ], closed=True, color=color, alpha=0.7)
            ax.add_patch(triangle)

    # Add the motivational message at the center of the canvas
    ax.text(0.5, 0.5, message, fontsize=14, color="black", ha='center', va='center', wrap=True, bbox=dict(facecolor='white', alpha=0.8))

    # Display the mood art
    plt.title(f"Mood Art: {mood.capitalize()}", fontsize=16, pad=20)
    plt.show()

# Example usage
user_mood = input("Enter your mood (happy, sad, relaxed, excited, angry, confident, anxious): ")
draw_mood_art(user_mood)
