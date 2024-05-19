



# <p align="center">genieBot 💡</p>

An AI chatbot with Gemini API to assist in your daily usage of linux 😉

# Installation


## Automated setup

Setuping the app on your machine

  #### pre steps
  
  1. download the repo
  
  ```bash
  git https://github.com/Mohamedwaelfaro/genieBot
  ```
  
#### Get your own API key
 3. You will be asked for the api key. to get the key go to : 
  	 1. [Get API key | Google AI Studio](https://aistudio.google.com/app/apikey)
     2. click on `Create API KEY` button
  	 3. generate a new project if needed or select a previous google cloud project.
  	 4. Copy the api key Showen on the popup dialog
  	 
  	Also check the steps on the detailed images below
  <br/><br/><br/><br/>

## How to use
all you need is to call `genie` and your wishes will be granted ✨

#### examples:

1.
```bash
geny how to create a new directory?
```
###### output
```bash
mkdir directory_name
```
2.
```bash
geny how to list files in a directory?
```
###### output
```txt
ls
```

3.
```bash
geny how to copy files and directories?
```
###### output
```txt
cp [options] source destination
```
4.
```bash
geny What is 5 + 5?
```
###### output
```txt
I'm sorry, i only answer bash commands
```

# <p align="center">Genie 🧞 and the project. </p>

## Manual setup

step by step how to create and the code explanations

1. First of all this is the python main logic code

```py
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
    user_input = input("Ask me:")

    # Exit loop if user enters 'exit'
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    

    # Construct the prompt to ask for definition and example
    prompt = f"""
    You are a helpful and informative AI assistant, 
    i want a simple answer and 2 example usage , if it is not about terimnal commands in ubuntu 			 	terimnal say I’m sorry, I only answer bash specific questions,
    Please provide a for the following Linux command,
     adding emojis related to the command without writing word emojis: 
    
    {user_input}
    """

    # Generate response from the model
    animate()  # Start the animation
    response = model.generate_content(prompt)

    # Print the generated text
    print(response.text)
    print("------------------------------------------------------------")
```

<br/>
<br/>

The logic behind keeping genie only in the topic of bash commands is by passing a pre prompt that engineers the output for a specific case

```py
text="Help with any question I ask about Linux bash commands only in very summarized answer with a short example usage and don't add any markdown styling make sure all the output you give is pair text. other wise if my question is off topic please only answer politely by refusing to answer this question. So my questions is : "+" ".join(sys.argv[1:])
```
<br /><br /><br />
2. Now about how to convert the normal python code into a ready to install application for any Debian based Linux disruptions
by copying the above code don't forget to set your own API key [in this step](#get-your-own-api-key)
and set it in a file named `genie.py`
get the path of the file
```bash
pwd ./genie.py
```
copy the output and add `/genie.py` at the end of it
```bash
pwd genie

/home/<usrName>
```
thus the path is : 
`/home/<usrName>/genie.py`
copy it and keep it for the next step.

do the following 
```bash
nano ~/.bashrc
```

this will open a file for you in which go to `last line` in the file and add the following : 
```bash
alias genie='python3 /home/<usrName>/genie.py'
```

Now you are behind one step from the glow!
update the new settings for the system to read by doing : 
```bash
source ~/.bashrc
```
<br />
Now you can use genie just as like as you would use the installed geny from the mesba7

<h1 align="center">that's it 👀</h1>

