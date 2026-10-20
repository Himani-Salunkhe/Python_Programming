
import tkinter as tk
from ollama import chat
import threading

# Conversation history
messages = [
    {
        "role": "system",
        "content": "You are a Python programming teacher"
    }
]

# Function to get AI response
def GetAnswer(question):

    try:
        response = chat(
            model="llama3.2:1b",
            messages=messages
        )

        answer = response.message.content

        messages.append({
            "role": "assistant",
            "content": answer
        })

        root.after(0, DisplayAnswer, answer)

    except Exception as error:
        messages.pop()
        root.after(0, DisplayAnswer, "Error: " + str(error))


# Function to display AI answer
def DisplayAnswer(answer):

    chatBox.insert(tk.END, "Marvellous AI: " + answer + "\n\n")
    chatBox.see(tk.END)

    entryQuestion.config(state="normal")
    buttonSend.config(state="normal")
    entryQuestion.focus()


# Function executed on button click
def SendMessage():

    question = entryQuestion.get().strip()

    if not question:
        return

    entryQuestion.delete(0, tk.END)

    chatBox.insert(tk.END, "You: " + question + "\n\n")
    chatBox.see(tk.END)

    messages.append({
        "role": "user",
        "content": question
    })

    entryQuestion.config(state="disabled")
    buttonSend.config(state="disabled")

    threading.Thread(
        target=GetAnswer,
        args=(question,),
        daemon=True
    ).start()


# Create main window
root = tk.Tk()

root.title("Marvellous Python Tutor")
root.geometry("600x500")

tk.Label(
    root,
    text="Marvellous Infosystems",
    font=("Arial", 20, "bold"),
    fg="blue"
).pack(pady=10)

# Application heading
tk.Label(
    root,
    text="Marvellous Python AI Tutor",
    font=("Arial", 14)
).pack()

# Chat display
chatBox = tk.Text(
    root,
    height=18,
    width=65,
    wrap="word"
)
chatBox.pack(pady=10)

# Input field
entryQuestion = tk.Entry(
    root,
    width=55,
    font=("Arial", 12)
)
entryQuestion.pack(pady=5)

# Send button
buttonSend = tk.Button(
    root,
    text="Send",
    font=("Arial", 12),
    command=SendMessage
)
buttonSend.pack(pady=10)

# Press Enter to send
entryQuestion.bind("<Return>", lambda event: SendMessage())

# Start GUI
root.mainloop()
