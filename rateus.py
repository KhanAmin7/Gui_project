import tkinter as tk
from tkinter import messagebox

class RateUsPage(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Rate Us")
        
        # Create a label and entry for feedback
        feedback_label = tk.Label(self, text="Please provide your feedback:")
        feedback_label.pack()
        self.feedback_entry = tk.Entry(self, width=50)
        self.feedback_entry.pack()
        
        # Create a label and rating scale for the rating
        rating_label = tk.Label(self, text="Please rate your experience:")
        rating_label.pack()
        self.rating_scale = tk.Scale(self, from_=1, to=5, orient=tk.HORIZONTAL)
        self.rating_scale.pack()
        
        # Create a submit button
        submit_button = tk.Button(self, text="Submit", command=self.submit_feedback)
        submit_button.pack()
        
    def submit_feedback(self):
        # Get the feedback and rating values
        feedback = self.feedback_entry.get()
        rating = self.rating_scale.get()
        
        # Print the rating to the console
        print(f"User rating: {rating}")
        print(f"User comment: {feedback}")
        
       
        
        # Show a message box to confirm that the feedback was submitted
        messagebox.showinfo("Thank You", "Thank you for your feedback!")
        self.destroy()

root = tk.Tk()

def open_rate_us_page():
    rate_us_page = RateUsPage(root)

rate_us_button = tk.Button(root, text="Rate Us", command=open_rate_us_page)
rate_us_button.pack()

root.mainloop()
