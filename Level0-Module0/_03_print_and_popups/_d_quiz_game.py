from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    int = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question
    Q = simpledialog.askstring('', 'What is 2876 + 4328 ?')
    #      // 3.  Use an if statement to check if their answer is correct
    if Q.lower() == '7104':
        int += 1
    q = simpledialog.askstring('', 'What color is the sun?')
    if q.lower() == 'yellow':
        int += 1
    A = simpledialog.askstring('', 'What is the summer azimuth of the sunset?')
    if A.lower() == '300.15':
        int += 1
    a = simpledialog.askstring('', 'what is the largest human organ?')
    if a.lower() == 'skin':
        int += 1
    messagebox.showinfo('', 'Your score is'+ str(int) +'congrats')
    #      // 4.  if the user's answer was correct, add one to their score 

    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
