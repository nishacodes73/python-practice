import tkinter as tk
root=tk.Tk()
root.title("Student Registration Form")
root.geometry("500x400")

# Name
name_label=tk.Label(root,text="Name")
name_label.grid(row=0,column=0)
Enter_name=tk.Entry(root)
Enter_name.grid(row=0,column=1)

#age
age_label=tk.Label(root,text="Age")
age_label.grid(row=1,column=0)
Enter_age=tk.Entry(root)
Enter_age.grid(row=1,column=1)

# Course
course_label=tk.Label(root,text="Course")
course_label.grid(row=2,column=0)
Enter_course=tk.Entry(root)
Enter_course.grid(row=2,column=1)

# collect information
def collection():
 name=Enter_name.get()
 age=Enter_age.get()
 course=Enter_course.get()
 print("Student name:",name)
 print("Student age:",age)
 print("Student course:",course)

submit_button=tk.Button(root,text="Submit",command=collection)
submit_button.grid(row=3,column=1)

root.mainloop()




