# using the facebook/bart-large-cnn trained model to summarize text
from transformers import pipeline
from tkinter import *
def makeSmall():
    ARTICLE = inputtext.get("1.0", 'end-1c')
    firstwords =ARTICLE.split(" ")
    lengthoffirstwords = len(firstwords)
    getfirst.config(text="Length of words is %d"%lengthoffirstwords)
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    converted = summarizer(ARTICLE,max_length=142, min_length=100, do_sample=True)
    outputtext.configure(text=converted[0]['summary_text'],font="Arial",aspect=500)
    last = converted[0]['summary_text'].split(" ")
    lengthoflast = len(last)
    lastwords.config(text="Length of summarized text is %d"%lengthoflast)
root = Tk()
root.geometry("1000x1000")
root.title("Text Summarization")
getfirst = Label(root)
lastwords = Label(root)
inputtext = Text(root, height=20,width=100)
outputtext = Message(root,cursor='hand2')
button = Button(root, text="Summarize", bg="#bf1d1d", fg="white", font=("Arial", 20), bd=0, padx=10, pady=10, activebackground="#1da1bf",command=makeSmall)
getfirst.pack()
inputtext.pack()
button.pack(padx=20,pady=20)
outputtext.pack()
lastwords.pack()
root.mainloop()