#<====================  import all modules here ================>
from tkinter import* # import tkinter module 
from tkinter import ttk # import tkinter.ttk module
from PIL import ImageTk,Image  # import PIL module
import googletrans # import googletrans to get all languages
from deep_translator import GoogleTranslator # import GoogleTranslator function from deep_translator for translating language
# Note: you need to collect to internet before it can work

#<========= calling all the functions here ==============>
def Language_Trans():
	Display_root()
	get_lang()
	Display_title()
	Display_text1()
	Display_text2()
	Label_change()
	Display_button()
	root.mainloop()

#<=========== function to display window =================>
def Display_root():
	global root,arrow_logo
	root = Tk()
	root.geometry("835x468+335+172")
	root.title("Music App")
	root.resizable(width=NO,height=NO)
	root.config(bg="#F7F7F7")
	arrow_logo = ImageTk.PhotoImage(Image.open("arrow.png"))
#<============= function to define all the languages =============>
def get_lang():
	global lang,langk,langv
	lang = googletrans.LANGUAGES  # English langauges name and codes
	langv,langk = [],[]  # language code, English language name
	for key,val in lang.items():
		langk.append(key)
		langv.append(val.upper())

#<=============== change the label text to combobox selected value ============>				
def Label_change():
	global c1,c2
	c1 = combo1.get()
	c2 = combo2.get()
	labe1.configure(text=c1)
	labe2.configure(text=c2)
	root.after(1000,Label_change)

#<========= convert one language to another ===================>
def Convert_button():
		#<======= get Text wiget texts =========>
		txt1 = text1.get(1.0,END)
		#< get language code. if combobox selected value is equal to English language name ======>
		lang = " ".join(langk[num] for num in range(len(langk)) if c1 == langv[num])

		if (txt1):
			#<===== get English language name. if English language name equal to combobox selected value ====>			
			dest = " ".join(langk[num] for num in range(len(langv)) if (langv[num] == c2))
			#<========= source parameter means: language code, target parameter means:English language name ========>
			translated = GoogleTranslator(source= lang ,target=dest).translate(str(txt1))
			#<==== insert translated language into the second Text widget ================>
			text2.insert(END,translated)

#<=========== function to clear Text widget text when user clicked clear button ============>
def clear_button():
	text1.delete(1.0,END)
	text2.delete(1.0,END)
#<=========== Function to display project title =======>
def Display_title():
	title = Label(root,text="LANGUAGE TRANSLATOR",bd=5,bg="white",font=("Roboto",25,"bold"),relief=GROOVE)
	title.place(x=0,y=0,width=835)

#<============= function to display all second frame and others widget =========>
def Display_text1():
	global combo1,labe1,text1
	#<====== combobox widget =====>
	combo1 = ttk.Combobox(root,font=("Roboto",15,"bold"),values=langv)
	combo1.set("SELECT")
	combo1.place(x=55,y=60,width=200,height=30)
	#<======== label widget ===========>	
	labe1 = Label(root,text="ENGLISH",bd=5,bg="white",font=("Roboto",25,"bold"),relief=GROOVE)
	labe1.place(x=35,y=100,width=240)
	#<========== Frame widget to hold Text frame widget =============>
	text_frame1 = Frame(root,bg="white",bd=4,relief=GROOVE)
	text_frame1.place(x=5,y=160,width=300,height=200)
	#<========= Scrollbar widget to make text frame scrollable ==========>
	scrollbar1 = Scrollbar(text_frame1,orient=VERTICAL)
	scrollbar1.pack(side=RIGHT,fill="y")
	#<===== Text frame for user to type what to convert to another language =========>
	text1 = Text(text_frame1,bg="white",font=("Arial",15,"bold"),yscrollcommand=scrollbar1.set)
	text1.pack(side=LEFT)
	#<====== change position of text frame when user move scrollbar up and down ==========>
	scrollbar1.configure(command=text1.yview)	
	arrow = Label(root,image=arrow_logo)
	arrow.place(x=341,y=218)
#<============= function to display all second frame and others widget =========>
def Display_text2():
	global combo2,labe2,text2
	#<====== combobox widget =====>
	combo2 = ttk.Combobox(root,font=("Roboto",15,"bold"),values=langv)
	combo2.set("SELECT")
	combo2.place(x=585,y=60,width=200,height=30)
	#<======== label widget ===========>	
	labe2 = Label(root,text="ENGLISH",bd=5,bg="white",font=("Roboto",25,"bold"),relief=GROOVE)
	labe2.place(x=563,y=100,width=240)
	#<========== Frame widget to hold Text frame widget =============>
	text_frame2 = Frame(root,bg="white",bd=4,relief=GROOVE)
	text_frame2.place(x=530,y=160,width=300,height=200)
	#<========= Scrollbar widget to make text frame scrollable ==========>
	scrollbar2 = Scrollbar(text_frame2,orient=VERTICAL)
	scrollbar2.pack(side=RIGHT,fill="y")
	#<===== Text frame for user to type what to convert to another language =========>
	text2 = Text(text_frame2,bg="white",font=("Arial",17,"bold"),yscrollcommand=scrollbar2.set)
	text2.pack(side=LEFT)
	#<====== change position of text frame when user move scrollbar up and down ==========>
	scrollbar2.configure(command=text2.yview)
#<=========== function for all buttons widget ================>		
def Display_button():
	convt = Button(root,text="CONVERT",fg="white",bg='#B200ED',font=("Roboto",15,"bold"),command=Convert_button)
	convt.place(x=341,y=316,width=160)
	clear = Button(root,text="CLEAR",fg="white",bg='red',font=("Roboto",15,"bold"),command=clear_button)
	clear.place(x=330,y=410,width=190)

print(Language_Trans())