from tkinter import *
import pandas as pd
from sqlalchemy import create_engine

root=Tk()
root.title("Data Storer")
root.geometry("500x500+100+200")
def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)

    engine = create_engine('sqlite:///data.db', echo=False)
    
    data = {inputValue}

    df = pd.DataFrame(data=data).T
    # SQL
    #df.to_sql('data.db', con=engine, index_label='ID')
    # CSV
    #df2 = pd.read_sql('data.db', con=engine, index_col='ID')

    df.to_csv('data.csv')
    #print(df2)


textBox=Text(root, height=5.5, width=100)
textBox.pack()
buttonCommit=Button(root, height=1, width=15, text="Send and Store it!", 
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

root.mainloop()



