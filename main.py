# using hugging face model to summarize text on tkinter
from transformers import pipeline
import tkinter

def makeSmall():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    ARTICLE = inputtext.get("1.0",'end-1c')
    converted = summarizer(ARTICLE,max_length=142, min_length=100, do_sample=True)
    outputtext.insert('1.0',converted[0]['summary_text'])
root = tkinter.Tk()
root.geometry("1000x1000")
root.title("Text Summarization")
inputtext = tkinter.Text(root, height=20,width=100)
outputtext = tkinter.Text(root,height=20,width=100)
button = tkinter.Button(root, text="Summarize", bg="#bf1d1d", fg="white", font=("Arial", 12), bd=0, padx=10, pady=10, activebackground="#1da1bf",command=lambda:makeSmall())
inputtext.pack()
button.pack(padx=20,pady=20)
outputtext.pack()
root.mainloop()
'''
Here is an Example
"Never Gonna Give You Up" is a classic 1980s pop song with a catchy melody and upbeat tempo. It was written and produced by Stock Aitken Waterman, a British songwriting and production team who were responsible for many hits during that era.
The song's music video features Rick Astley performing the song and dancing in a variety of locations, including a studio and a city street. Astley's distinctive baritone voice, combined with the song's memorable hook and upbeat rhythm, helped to make it a huge success both in the UK and internationally.
In the years since its release, "Never Gonna Give You Up" has become a cultural touchstone, thanks in large part to the internet phenomenon of rickrolling. This involves sending a link to someone with the promise of leading them to one thing, but instead redirecting them to the music video for the song. The practice of rickrolling gained popularity in the mid-2000s and has been used as a playful prank, a form of internet trolling, and even a political statement. Despite being associated with the prank, the song itself remains a beloved classic of 80s pop music.
'''



