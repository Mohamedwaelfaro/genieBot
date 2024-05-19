import google.generativeai as genai
import os
import textwrap
import time
import sys

# Set the Google API Key (replace with your actual key)
your_api_key = "AIzaSyDyL27pH9PRKQxjJk9txGzkUn5qBVGZGJw"
os.environ['GOOGLE_API_KEY'] = your_api_key

# Configure Google Generative AI
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


# def to_markdown(text):
#     """Converts plain text to Markdown format with bullets.

#     Args:
#         text: The plain text string to convert.

#     Returns:
#         A string containing the Markdown formatted text.
#     """
#     text = text.replace('•', '  *')  # Use two spaces for better formatting
#     # Indent each line
#     return textwrap.indent(text, '> ', predicate=lambda _: True)


# Load the generative model (replace 'gemini-1.5-pro-latest' if desired)
model = genai.GenerativeModel('gemini-1.0-pro')

# Animation function


def animate():
    animation = "|/-\\"
    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write("\rGenie: " + animation[i % len(animation)])
        sys.stdout.flush()
    sys.stdout.write("\rGenie: ")


# Interactive chat loop
while True:
    # Get user input
    user_input = input(" ")

    # Exit loop if user enters 'exit'
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    # Check if the input is a mathematical operation
    if any(op in user_input for op in ['+', '-', '*', '/', '^', '%']):
        print("I’m sorry, I only answer Linux command specific questions.")
        continue

    # Construct the prompt to ask for definition and example
    prompt = f"""
    You are a helpful and informative AI assistant, 
    i want a simple answer and 2 example usage , if it is not about terimnal commands in ubuntu terimnal say I’m sorry, I only answer bash specific questions, 
    Please provide a definition for the following Linux command,add emojy to make it more fun:relate to the command:: 
    
    {user_input}
    """

    # Generate response from the model
    animate()  # Start the animation
    response = model.generate_content(prompt)

    # Print the generated text
    print(response.text)
    