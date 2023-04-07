from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from pymongo import *

def f1():
	root.withdraw()
	aw.deiconify()
def f2():
	aw.withdraw()
	root.deiconify()
def f3():
	root.withdraw()
	vw.deiconify()
	vw_st_data.delete(1.0,END)
	con=None
	try:
		con=MongoClient("mongodb://localhost:27017")
		db=con["6Jan2023"]
		coll=db["student"]
		data=coll.find()
		info=""
		for d in data:
			info=info+"rno= "+str(d["_id"])+"name= "+str(d["name"])+"\n"
		vw_st_data.insert(INSERT,info)
	except Exception as e:
		showerror("issues",e)
	finally:
		if con is not None:
			con.close()
def f4():
	vw.withdraw()
	root.deiconify()
def f5():
	con=None
	try:
		con=MongoClient("mongodb://localhost:27017")
		db=con["6Jan2023"]
		coll=db["student"]
		rno=int(aw_ent_rno.get())
		name=aw_ent_name.get()
		count=coll.count_documents({"_id":rno})
		if count == 1:
			showinfo(rno,"alredy exists")
		else:
			info={"_id":rno,"name":name}
			coll.insert_one(info)
			showinfo("success","record created")
	except Exception as e:
		print("issues",e)
	finally:
		if con is not None:
			con.close()
		aw_ent_rno.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_rno.focus()

root=Tk()
root.title("S.M.S")
root.geometry("500x600+50+50")
f=("Simsun",30,"bold")

btn_add=Button(root,text="Add Student",font=f,width=15,command=f1)
btn_add.pack(pady=20)
btn_view=Button(root,text="View Student",font=f,width=15,command=f3)
btn_view.pack(pady=20)

aw=Toplevel(root)
aw.title("Add Student")
aw.geometry("500x600+50+50")
aw_lab_rno=Label(aw,text="enter rno",font=f)
aw_ent_rno=Entry(aw,font=f,bd=2)
aw_lab_name=Label(aw,text="Enter name",font=f)
aw_ent_name=Entry(aw,font=f,bd=2)
aw_btn_save=Button(aw,text="Save",font=f,command=f5)
aw_btn_back=Button(aw,text="Back",font=f,command=f2)
aw_lab_rno.pack(pady=10)
aw_ent_rno.pack(pady=10)
aw_lab_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_btn_save.pack(pady=10)
aw_btn_back.pack(pady=10)
aw.withdraw()

vw=Toplevel(root)
vw.title("View Student")
vw.geometry("500x600+50+50")
vw_st_data=ScrolledText(vw,width=22,height=10,font=f)
vw_btn_back=Button(vw,text="Back",font=f,command=f4)
vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)
vw.withdraw()

root.mainloop()