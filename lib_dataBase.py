from tkinter import *

import sqlite3


class Library:
    def __init__(self,table,window):
        self.table=table
        self.window=window
        
        self.window.title('Library books management system')
        self.window.geometry('1350x900+0+0')
        self.window.configure(background='powder blue')
        mainFrame=Frame(self.window)
        mainFrame.pack()
        topFrame=Frame(mainFrame,width=900,height=70,borderwidth=2,relief=SUNKEN,padx=20,bg='powder blue')
        topFrame.pack(side=TOP,fill=X)
        centerFrame=Frame(mainFrame,width=900,height=800,relief=RIDGE)
        centerFrame.pack(side=TOP)
        leftFrame=Frame(centerFrame,width=300,height=700,borderwidth=2,relief=SUNKEN)
        leftFrame.pack(side=LEFT)
        rightFrame=Frame(centerFrame,width=600,height=700,borderwidth=2,relief=SUNKEN,bg='powder blue')
        rightFrame.pack(side=RIGHT)
        self.scroll_bar=Scrollbar(rightFrame)
        self.scroll_bar.pack(fill=Y,side=RIGHT)


        self.btn_add=Button(topFrame,text='Add Book',padx=14,font=10,command=self.add,bd=5,bg='white smoke')
        self.btn_add.pack(side=LEFT)
        self.btn_show=Button(topFrame,text='Show Books',padx=14,bg='powderblue',font=10,command=self.show,bd=5)
        self.btn_show.pack(side=LEFT)
        self.btn_update=Button(topFrame,text='Update Books',padx=14,font=10,command=self.update,bd=5,bg='white smoke')
        self.btn_update.pack(side=LEFT)
        self.btn_delete=Button(topFrame,text='Delete Book',padx=14,bg='powderblue',font=10,command=self.delete,bd=5)
        self.btn_delete.pack(side=LEFT)
        self.btn_search=Button(topFrame,text='Search Books',padx=14,font=10,command=self.search,bd=5,bg='white smoke')
        self.btn_search.pack(side=LEFT)
        self.btn_order=Button(topFrame,text='Sort Books',padx=14,bg='powderblue',font=10,command=self.order,bd=5)
        self.btn_order.pack(side=LEFT)
        self.btn_balance=Button(topFrame,text='Books balance',padx=14,font=14,command=self.balance,bd=5,bg='white smoke')
        self.btn_balance.pack(side=LEFT)
        self.btn_help=Button(topFrame,text='Help',padx=14,font=14,command=self.help,bg='powderblue',bd=5)
        self.btn_help.pack(side=LEFT)
        self.btn_about=Button(topFrame,text='About Program',padx=14,font=10,command=self.about,bd=5,bg='white smoke')
        self.btn_about.pack(side=LEFT)
        self.btn_exit=Button(topFrame,text='Program Exit',padx=14,font=10,command=self.close,bg='powderblue',bd=5)
        self.btn_exit.pack(side=LEFT)
        fields_bar=LabelFrame(leftFrame,width=300,height=75,text='Fields',font='arial 16 bold',bg='yellow2',bd=10)
        fields_bar.pack(fill=BOTH)
        
        self.lbl_id=Label(fields_bar,text='Book_ID: ',font='arial 14 bold',bg='powderblue')
        self.lbl_id.grid(row=0,column=0,padx=20,pady=10)
        self.ent_id=Entry(fields_bar,bd=10,font=50)
        self.ent_id.grid(row=0,column=1,padx=20,pady=10)
        
        self.lbl_title=Label(fields_bar,text='Book_Title: ',font='arial 14 bold',bg='powderblue')
        self.lbl_title.grid(row=1,column=0,padx=20,pady=10)
        self.ent_title=Entry(fields_bar,bd=10,font=50)
        self.ent_title.grid(row=1,column=1,padx=20,pady=10)
        
        self.lbl_author=Label(fields_bar,text='Book_Author: ',font='arial 14 bold',bg='powderblue')
        self.lbl_author.grid(row=2,column=0,padx=20,pady=10)
        self.ent_author=Entry(fields_bar,bd=10,font=50)
        self.ent_author.grid(row=2,column=1,padx=20,pady=10)
        
        self.lbl_genre=Label(fields_bar,text='Book_Genre: ',font='arial 14 bold',bg='powderblue')
        self.lbl_genre.grid(row=3,column=0,padx=20,pady=10)
        self.ent_genre=Entry(fields_bar,bd=10,font=50)
        self.ent_genre.grid(row=3,column=1,padx=20,pady=10)
        
        
        self.lbl_pageNum=Label(fields_bar,text='Book_PageNum: ',font='arial 14 bold',bg='powderblue')
        self.lbl_pageNum.grid(row=4,column=0,padx=20,pady=10)
        self.ent_pageNum=Entry(fields_bar,bd=10,font=50)
        self.ent_pageNum.grid(row=4,column=1,padx=20,pady=10)
        
        
        self.lbl_language=Label(fields_bar,text='Book_Language: ',font='arial 14 bold',bg='powderblue')
        self.lbl_language.grid(row=5,column=0,padx=20,pady=10)
        self.ent_language=Entry(fields_bar,bd=10,font=50)
        self.ent_language.grid(row=5,column=1,padx=20,pady=10)
        
        
        self.lbl_year=Label(fields_bar,text='Book_Year: ',font='arial 14 bold',bg='powderblue')
        self.lbl_year.grid(row=6,column=0,padx=20,pady=10)
        self.ent_year=Entry(fields_bar,bd=10,font=50)
        self.ent_year.grid(row=6,column=1,padx=20,pady=10)
        
        self.lt=Listbox(rightFrame,height=700,width=800,fg='blue',font='arial 13 bold',bd=10,yscrollcommand=self.scroll_bar.set)
        self.lt.pack(padx=20,pady=20,side=LEFT,fill=BOTH)
        self.scroll_bar.config(command=self.lt.yview)
        self.btn_clr_ent=Button(leftFrame,text='Clear_Fields',font='arial 14 bold',bg='yellow2',command=self.clr_ent,bd=10)
        self.btn_clr_ent.pack(side=LEFT)        
        self.btn_clr=Button(leftFrame,text='Clear_Box',font='arial 14 bold',bg='powder blue',command=self.clr_box,bd=10)
        self.btn_clr.pack(side=LEFT)

       
        

        

      

        
        
    def connect(self):
        db=sqlite3.connect('library.db')
        cr=db.cursor()
        cr.execute(f'create table if not exists {self.table}(ID int,title varchar(30),author varchar(30),genre varchar(30),pageNum int,language varchar(30),year int)')
        
        
    def show(self):
        db=sqlite3.connect('library.db')
        cr=db.cursor() 
        cr.execute(f'select * from {self.table}')
        rows=cr.fetchall()
        if len(rows)==0:
            self.lt.insert(0,'Table is empty!')
        else:
            index=0
            lst=['Book_ID','Book_Title','Book_Author','Book_Genre','Book_PageNum','Book_Language','Book_Year']
            for i in rows:
                counter=0
                for j in i:
                    
                 self.lt.insert(index,f'{lst[counter]}:{j}') 
                 counter+=1 
                 index+=1  
                index=0 
                self.lt.insert(index,'--------------------------------------------------')    

    def add(self):
        db=sqlite3.connect('library.db')
        cr=db.cursor()
        cr.execute(f'select * from {self.table}')
        rows=cr.fetchall()
        if self.ent_id.get()=='' or self.ent_title.get()=='' or self.ent_author.get()=='' or self.ent_genre.get()=='' or self.ent_pageNum.get()=='' or self.ent_language.get()=='' or self.ent_year.get()=='':
            self.lt.insert(0,'Fill up all of the fields bar!')
        else:
                
         for i in rows:
            
            if self.ent_id.get().lower() ==  f'{i[0]}':
                self.lt.insert(0,'This ID has been entered before!')
                break

         else:
            cr.execute(f'insert into {self.table} values(?,?,?,?,?,?,?)',(self.ent_id.get().lower(),self.ent_title.get().lower(),self.ent_author.get().lower(),self.ent_genre.get().lower(),self.ent_pageNum.get().lower(),self.ent_language.get().lower(),self.ent_year.get().lower()))
            db.commit()   
            self.lt.insert(0,'Fields have been added')           
 
    def clr_box(self):
        self.lt.delete(0,END)            
    def clr_ent(self):
        self.ent_id.delete(0,END)
        self.ent_title.delete(0,END)
        self.ent_author.delete(0,END)
        self.ent_genre.delete(0,END)
        self.ent_pageNum.delete(0,END)
        self.ent_language.delete(0,END)
        self.ent_year.delete(0,END)
    def update(self):
        db=sqlite3.connect('library.db')
        cr=db.cursor() 
        cr.execute(f'select * from {self.table}')
        rows=cr.fetchall()


        if len(rows)==0:
            self.lt.insert(0,'Table is empty')
        elif self.ent_id.get()=='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            self.lt.insert(0,'Fill up ID bar and the field that you want to update its value!')                      
        elif self.ent_id.get()!='' and self.ent_title.get()!='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            for i in rows:
                if self.ent_id.get().lower()==f'{i[0]}':
                    cr.execute(f'update {self.table} set title="{self.ent_title.get().lower()}" where ID="{self.ent_id.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,f'"{self.ent_title.get().lower()}" has been updated in book title with ID "{self.ent_id.get().lower()}"') 
                    break
            else:
                self.lt.insert(0,f'ID "{self.ent_id.get().lower()}" not found!')
                
        elif self.ent_id.get()!='' and self.ent_title.get()=='' and self.ent_author.get()!='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            for i in rows:
                if self.ent_id.get().lower()==f'{i[0]}':
                    cr.execute(f'update {self.table} set author="{self.ent_author.get().lower()}" where ID="{self.ent_id.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,f'"{self.ent_author.get().lower()}" has been updated in book author with ID "{self.ent_id.get().lower()}"') 
                    break
            else:
                self.lt.insert(0,f'ID "{self.ent_id.get().lower()}" not found!')            
        elif self.ent_id.get()!='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()!='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            for i in rows:
                if self.ent_id.get().lower()==f'{i[0]}':
                    cr.execute(f'update {self.table} set genre="{self.ent_genre.get().lower()}" where ID="{self.ent_id.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,f'"{self.ent_genre.get().lower()}" has been updated in book genre with ID "{self.ent_id.get().lower()}"') 
                    break
            else:
                self.lt.insert(0,f'ID "{self.ent_id.get().lower()}" not found!')            
        elif self.ent_id.get()!='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()!='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            for i in rows:
                if self.ent_id.get().lower()==f'{i[0]}':
                    cr.execute(f'update {self.table} set pageNum="{self.ent_pageNum.get().lower()}" where ID="{self.ent_id.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,f'"{self.ent_pageNum.get().lower()}" has been updated in book pageNum with ID "{self.ent_id.get().lower()}"') 
                    break
            else:
                self.lt.insert(0,f'ID "{self.ent_id.get().lower()}" not found!')        
        elif self.ent_id.get()!='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()!='' and self.ent_year.get()=='':
            for i in rows:
                if self.ent_id.get().lower()==f'{i[0]}':
                    cr.execute(f'update {self.table} set language="{self.ent_language.get().lower()}" where ID="{self.ent_id.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,f'"{self.ent_language.get().lower()}" has been updated in book language with ID "{self.ent_id.get().lower()}"') 
                    break
            else:
                self.lt.insert(0,f'ID "{self.ent_id.get().lower()}" not found!')        
        elif self.ent_id.get()!='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()!='':
            for i in rows:
                if self.ent_id.get().lower()==f'{i[0]}':
                    cr.execute(f'update {self.table} set year="{self.ent_year.get().lower()}" where ID="{self.ent_id.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,f'"{self.ent_year.get().lower()}" has been updated in book year with ID "{self.ent_id.get().lower()}"') 
                    break
            else:
                self.lt.insert(0,f'ID "{self.ent_id.get().lower()}" not found!')        
        else:
            self.lt.insert(0,'Just Fill up ID bar and the field that you want to update its value!')
                                    
    def search(self):

        
        db=sqlite3.connect('library.db')
        cr=db.cursor() 
        cr.execute(f'select * from {self.table}')
        rows=cr.fetchall()
        if len(rows)==0:
            self.lt.insert(0,'Table is empty')        
        elif self.ent_id.get()=='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            self.lt.insert(0,'Fill up at least one field!')

        else:
            ok=0

            for i in rows:
                if self.ent_id.get().lower()==f'{i[0]}' or self.ent_title.get().lower()==f'{i[1]}' or self.ent_author.get().lower()==f'{i[2]}' or self.ent_genre.get().lower()==f'{i[3]}' or self.ent_pageNum.get().lower()==f'{i[4]}' or self.ent_language.get().lower()==f'{i[5]}' or self.ent_year.get().lower()==f'{i[6]}':
                    ok+=1
                    cr.execute(f'select * from {self.table} where ID="{self.ent_id.get().lower()}" or title="{self.ent_title.get().lower()}" or author="{self.ent_author.get().lower()}" or genre="{self.ent_genre.get().lower()}" or pageNum="{self.ent_pageNum.get().lower()}" or language="{self.ent_language.get().lower()}" or year="{self.ent_year.get().lower()}" ')
                

            if ok==0:
                self.lt.insert(0,'There is no book that matches with this description!')        
            else:
                index=0
                rows=cr.fetchall()
                lst=['Book_ID','Book_Title','Book_Author','Book_Genre','Book_PageNum','Book_Language','Book_Year']
                for i in rows:
                    counter=0
                    for j in i:
                    
                      self.lt.insert(index,f'{lst[counter]}:{j}') 
                      counter+=1 
                      index+=1  
                    index=0 
                    self.lt.insert(index,'--------------------------------------------------')  

    def delete(self):
        db=sqlite3.connect('library.db')
        cr=db.cursor() 
        cr.execute(f'select * from {self.table}')
        rows=cr.fetchall()
        if len(rows)==0:
            self.lt.insert(1,'Table is empty!')         
        elif self.ent_id.get()=='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            self.lt.insert(1,'Fill up one Field bar!')
   
        elif  self.ent_id.get()!='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            ok=0
            for i in rows:
                if self.ent_id.get().lower()==f'{i[0]}':
                    ok+=1
                    cr.execute(f'delete from {self.table}  where ID="{self.ent_id.get().lower()}" ')
                    db.commit()
                

            if ok==0:
                self.lt.insert(0,'There is no book that matches with this description!')        
            else:
                self.lt.insert(0,'Book has been deleted')
        elif   self.ent_title.get()!='' and self.ent_id.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            ok=0
            for i in rows:
                if  self.ent_title.get().lower()==f'{i[1]}':
                    ok+=1
                    cr.execute(f'delete from {self.table} where title="{self.ent_title.get().lower()}"')
                    db.commit()
                

            if ok==0:
                self.lt.insert(0,'There is no book that matches with this description!')        
            else:
                self.lt.insert(0,'Book has been deleted')
        elif self.ent_author.get()!=''and self.ent_title.get()=='' and self.ent_id.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            ok=0
            for i in rows:
                if self.ent_author.get().lower()==f'{i[2]}':
                    ok+=1
                    cr.execute(f'delete from {self.table} where author="{self.ent_author.get().lower()}"')
                    db.commit()
                

            if ok==0:
                self.lt.insert(0,'There is no book that matches with this description!')        
            else:
                self.lt.insert(0,'Book has been deleted')
        elif self.ent_author.get()==''and self.ent_title.get()=='' and self.ent_id.get()=='' and self.ent_genre.get()!='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            ok=0
            for i in rows:
                if self.ent_genre.get().lower()==f'{i[3]}':
                    ok+=1
                    cr.execute(f'delete from {self.table} where genre="{self.ent_genre.get().lower()}"')
                    db.commit()
                

            if ok==0:
                self.lt.insert(0,'There is no book that matches with this description!')        
            else:
                self.lt.insert(0,'Book has been deleted')
        elif self.ent_author.get()==''and self.ent_title.get()=='' and self.ent_id.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()!='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            ok=0
            for i in rows:
                if self.ent_pageNum.get().lower()==f'{i[4]}':
                    ok+=1
                    cr.execute(f'delete from {self.table} where pageNum="{self.ent_pageNum.get().lower()}"')
                    db.commit()
                

            if ok==0:
                self.lt.insert(0,'There is no book that matches with this description!')        
            else:
                self.lt.insert(0,'Book has been deleted')
        elif self.ent_author.get()==''and self.ent_title.get()=='' and self.ent_id.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()!='' and self.ent_year.get()=='':
            ok=0
            for i in rows:
                if self.ent_language.get().lower()==f'{i[5]}':
                    ok+=1
                    cr.execute(f'delete from {self.table} where language="{self.ent_language.get().lower()}"')
                    db.commit()
                

            if ok==0:
                self.lt.insert(0,'There is no book that matches with this description!')        
            else:
                self.lt.insert(0,'Book has been deleted')
        elif self.ent_author.get()==''and self.ent_title.get()=='' and self.ent_id.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()!='':
            ok=0
            for i in rows:
                if self.ent_year.get().lower()==f'{i[6]}':
                    ok+=1
                    cr.execute(f'delete from {self.table} where year="{self.ent_year.get().lower()}"')
                    db.commit()
                

            if ok==0:
                self.lt.insert(0,'There is no book that matches with this description!')        
            else:
                self.lt.insert(0,'Book has been deleted')
        else:
            self.lt.insert(1,'Fill up just one field bar!')   


                
                        
            
    def balance(self):
        db=sqlite3.connect('library.db')
        cr=db.cursor()
        cr.execute(f'select * from {self.table}')
        books=cr.fetchall()
        self.lt.insert(0,f'Total number of all books:{len(books)}')
        if self.ent_id.get()=='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            pass
        elif self.ent_id.get()!='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            cr.execute(f'select * from {self.table} where ID="{self.ent_id.get().lower()}"')
            book=cr.fetchall()
            self.lt.insert(0,f'Total number of books with ID "{self.ent_id.get().lower()}":{len(book)}')
            
        elif self.ent_id.get()=='' and self.ent_title.get()!='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            cr.execute(f'select * from {self.table} where title="{self.ent_title.get().lower()}"')
            book=cr.fetchall()
            self.lt.insert(1,f'Total number of books with title "{self.ent_title.get().lower()}":{len(book)}')            
        elif self.ent_id.get()=='' and self.ent_title.get()=='' and self.ent_author.get()!='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            cr.execute(f'select * from {self.table} where author="{self.ent_author.get().lower()}"')
            book=cr.fetchall()
            self.lt.insert(1,f'Total number of books with author "{self.ent_author.get().lower()}":{len(book)}')            
        elif self.ent_id.get()=='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()!='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            cr.execute(f'select * from {self.table} where genre="{self.ent_genre.get().lower()}"')
            book=cr.fetchall()
            self.lt.insert(1,f'Total number of books with genre "{self.ent_genre.get().lower()}":{len(book)}')            
        elif self.ent_id.get()=='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()!='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            cr.execute(f'select * from {self.table} where pageNum="{self.ent_pageNum.get().lower()}"')
            book=cr.fetchall()
            self.lt.insert(1,f'Total number of books with pageNum "{self.ent_pageNum.get().lower()}":{len(book)}')            
        elif self.ent_id.get()=='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()!='' and self.ent_year.get()=='':
            cr.execute(f'select * from {self.table} where language="{self.ent_language.get().lower()}"')
            book=cr.fetchall()
            self.lt.insert(1,f'Total number of books with language "{self.ent_language.get().lower()}":{len(book)}')            
        elif self.ent_id.get()=='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()!='': 
            cr.execute(f'select * from {self.table} where year="{self.ent_year.get().lower()}"')
            book=cr.fetchall()
            self.lt.insert(1,f'Total number of books with year "{self.ent_year.get().lower()}":{len(book)}')               
        else:
            self.lt.insert(1,'Fill up only one field or none fields!')
                            
                
    def help(self):
        self.lt.insert(0,'# For adding books fill up the field bars then press Add Book.')
        self.lt.insert(1,'# Press Show Books for showing all of the fields.')
        self.lt.insert(2,'# To update books values fill up ID bar with existed value ')
        self.lt.insert(3,' and field that you want to change its value with new value and then press Update Books.')
        self.lt.insert(4,'# To delete books just fill up one bar then press Delete Book and program will delete the book.')       
        self.lt.insert(5,'# To search books fill up any fields then press Search Books and program finds the book with given value.')       
        self.lt.insert(6,'# To sort books fill up just one of the fields with "a" for ascending order and "d" for descending order ')       
        self.lt.insert(7,' Then press Sort Books to sort the books.')       
        self.lt.insert(8,'# Press About Program to show some informations about program. ')
        self.lt.insert(9,'# Press Program Exit to close the program.')
        self.lt.insert(10,'# Press Clear_Box to clear the answer box.')
        self.lt.insert(11,'# Press Books balance to show the number of all books')
        self.lt.insert(12,' and you can fill up one field to show the number of books with that field.')
        self.lt.insert(13,'# Press Clear_Fields to clear the fields bar.')
        self.lt.insert(14,'------------------------------------------------------------------')
    def order(self):
        db=sqlite3.connect('library.db')
        cr=db.cursor() 
        cr.execute(f'select * from {self.table}')
        rows=cr.fetchall()
        if len(rows)==0:
            self.lt.insert(0,'Table is empty')        
        elif self.ent_id.get()=='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            self.lt.insert(0,'Fill up one field with "a" for ascending order or "d" for descending order!')

        elif  self.ent_id.get().lower()=='a' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':   
            cr.execute(f'select * from {self.table} order by ID DESC')
            rows=cr.fetchall()
            index=0
            lst=['Book_ID','Book_Title','Book_Author','Book_Genre','Book_PageNum','Book_Language','Book_Year']
            for i in rows:
                counter=0
                for j in i:
                    
                    self.lt.insert(index,f'{lst[counter]}:{j}') 
                    counter+=1 
                    index+=1  
                index=0 
                self.lt.insert(index,'--------------------------------------------------')              
              
        elif  self.ent_id.get().lower()=='d' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':  
            cr.execute(f'select * from {self.table} order by ID ASC')
            rows=cr.fetchall()
            index=0
            lst=['Book_ID','Book_Title','Book_Author','Book_Genre','Book_PageNum','Book_Language','Book_Year']
            for i in rows:
                counter=0
                for j in i:
                    
                    self.lt.insert(index,f'{lst[counter]}:{j}') 
                    counter+=1 
                    index+=1  
                index=0 
                self.lt.insert(index,'--------------------------------------------------')                 
        elif  self.ent_id.get().lower()=='' and self.ent_title.get().lower()=='a' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':  
            cr.execute(f'select * from {self.table} order by title DESC')
            rows=cr.fetchall()
            index=0
            lst=['Book_ID','Book_Title','Book_Author','Book_Genre','Book_PageNum','Book_Language','Book_Year']
            for i in rows:
                counter=0
                for j in i:
                    
                    self.lt.insert(index,f'{lst[counter]}:{j}') 
                    counter+=1 
                    index+=1  
                index=0 
                self.lt.insert(index,'--------------------------------------------------')                 
        elif  self.ent_id.get().lower()=='' and self.ent_title.get().lower()=='d' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':  
            cr.execute(f'select * from {self.table} order by title ASC')
            rows=cr.fetchall()
            index=0
            lst=['Book_ID','Book_Title','Book_Author','Book_Genre','Book_PageNum','Book_Language','Book_Year']
            for i in rows:
                counter=0
                for j in i:
                    
                    self.lt.insert(index,f'{lst[counter]}:{j}') 
                    counter+=1 
                    index+=1  
                index=0 
                self.lt.insert(index,'--------------------------------------------------')                 
        elif  self.ent_id.get().lower()=='' and self.ent_title.get()=='' and self.ent_author.get().lower()=='a' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':   
            cr.execute(f'select * from {self.table} order by author DESC')
            rows=cr.fetchall()
            index=0
            lst=['Book_ID','Book_Title','Book_Author','Book_Genre','Book_PageNum','Book_Language','Book_Year']
            for i in rows:
                counter=0
                for j in i:
                    
                    self.lt.insert(index,f'{lst[counter]}:{j}') 
                    counter+=1 
                    index+=1  
                index=0 
                self.lt.insert(index,'--------------------------------------------------')                
        elif  self.ent_id.get().lower()=='' and self.ent_title.get()=='' and self.ent_author.get().lower()=='d' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':  
            cr.execute(f'select * from {self.table} order by author ASC')
            rows=cr.fetchall()
            index=0
            lst=['Book_ID','Book_Title','Book_Author','Book_Genre','Book_PageNum','Book_Language','Book_Year']
            for i in rows:
                counter=0
                for j in i:
                    
                    self.lt.insert(index,f'{lst[counter]}:{j}') 
                    counter+=1 
                    index+=1  
                index=0 
                self.lt.insert(index,'--------------------------------------------------')                 
        elif  self.ent_id.get().lower()=='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get().lower()=='a' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='':
            cr.execute(f'select * from {self.table} order by genre DESC')
            rows=cr.fetchall()
            index=0
            lst=['Book_ID','Book_Title','Book_Author','Book_Genre','Book_PageNum','Book_Language','Book_Year']
            for i in rows:
                counter=0
                for j in i:
                    
                    self.lt.insert(index,f'{lst[counter]}:{j}') 
                    counter+=1 
                    index+=1  
                index=0 
                self.lt.insert(index,'--------------------------------------------------')                   
        elif  self.ent_id.get().lower()=='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get().lower()=='d' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get()=='': 
            cr.execute(f'select * from {self.table} order by genre ASC')
            rows=cr.fetchall()
            index=0
            lst=['Book_ID','Book_Title','Book_Author','Book_Genre','Book_PageNum','Book_Language','Book_Year']
            for i in rows:
                counter=0
                for j in i:
                    
                    self.lt.insert(index,f'{lst[counter]}:{j}') 
                    counter+=1 
                    index+=1  
                index=0 
                self.lt.insert(index,'--------------------------------------------------')                  
        elif  self.ent_id.get().lower()=='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get().lower()=='a' and self.ent_language.get()=='' and self.ent_year.get()=='':  
            cr.execute(f'select * from {self.table} order by pageNum DESC')
            rows=cr.fetchall()
            index=0
            lst=['Book_ID','Book_Title','Book_Author','Book_Genre','Book_PageNum','Book_Language','Book_Year']
            for i in rows:
                counter=0
                for j in i:
                    
                    self.lt.insert(index,f'{lst[counter]}:{j}') 
                    counter+=1 
                    index+=1  
                index=0 
                self.lt.insert(index,'--------------------------------------------------')                 
        elif  self.ent_id.get().lower()=='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get().lower()=='d' and self.ent_language.get()=='' and self.ent_year.get()=='':
            cr.execute(f'select * from {self.table} order by pageNum ASC')
            rows=cr.fetchall()
            index=0
            lst=['Book_ID','Book_Title','Book_Author','Book_Genre','Book_PageNum','Book_Language','Book_Year']
            for i in rows:
                counter=0
                for j in i:
                    
                    self.lt.insert(index,f'{lst[counter]}:{j}') 
                    counter+=1 
                    index+=1  
                index=0 
                self.lt.insert(index,'--------------------------------------------------')                   
        elif  self.ent_id.get().lower()=='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get().lower()=='a' and self.ent_year.get()=='':  
            cr.execute(f'select * from {self.table} order by language DESC')
            rows=cr.fetchall()
            index=0
            lst=['Book_ID','Book_Title','Book_Author','Book_Genre','Book_PageNum','Book_Language','Book_Year']
            for i in rows:
                counter=0
                for j in i:
                    
                    self.lt.insert(index,f'{lst[counter]}:{j}') 
                    counter+=1 
                    index+=1  
                index=0 
                self.lt.insert(index,'--------------------------------------------------')                 
        elif  self.ent_id.get().lower()=='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get().lower()=='d' and self.ent_year.get()=='': 
            cr.execute(f'select * from {self.table} order by language ASC')
            rows=cr.fetchall()
            index=0
            lst=['Book_ID','Book_Title','Book_Author','Book_Genre','Book_PageNum','Book_Language','Book_Year']
            for i in rows:
                counter=0
                for j in i:
                    
                    self.lt.insert(index,f'{lst[counter]}:{j}') 
                    counter+=1 
                    index+=1  
                index=0 
                self.lt.insert(index,'--------------------------------------------------')                  
        elif  self.ent_id.get().lower()=='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get().lower()=='a': 
            cr.execute(f'select * from {self.table} order by year DESC')
            rows=cr.fetchall()
            index=0
            lst=['Book_ID','Book_Title','Book_Author','Book_Genre','Book_PageNum','Book_Language','Book_Year']
            for i in rows:
                counter=0
                for j in i:
                    
                    self.lt.insert(index,f'{lst[counter]}:{j}') 
                    counter+=1 
                    index+=1  
                index=0 
                self.lt.insert(index,'--------------------------------------------------')                  
        elif  self.ent_id.get().lower()=='' and self.ent_title.get()=='' and self.ent_author.get()=='' and self.ent_genre.get()=='' and self.ent_pageNum.get()=='' and self.ent_language.get()=='' and self.ent_year.get().lower()=='d': 
            cr.execute(f'select * from {self.table} order by year ASC')
            rows=cr.fetchall()
            index=0
            lst=['Book_ID','Book_Title','Book_Author','Book_Genre','Book_PageNum','Book_Language','Book_Year']
            for i in rows:
                counter=0
                for j in i:
                    
                    self.lt.insert(index,f'{lst[counter]}:{j}') 
                    counter+=1 
                    index+=1  
                index=0 
                self.lt.insert(index,'--------------------------------------------------')               
        else:
            self.lt.insert(0,'Fill up just one field with "a" or "d"!')       
    def about(self):
        self.lt.insert(0,'Master:Dr.ALI SALEHI')
        self.lt.insert(1,'Programmer:AMIRHOSSEIN JAZDAREYI')
        self.lt.insert(2,'Subject:MFT 1402 programming with python class final project')
        self.lt.insert(3,'Project name:Library management system for books')
        self.lt.insert(4,'GUI:Tkinter ')
        self.lt.insert(5,'Programming language:Python3')
        self.lt.insert(6,'DataBase:Sqlite3')
        self.lt.insert(7,'Design pattern:Object-Oriented(OOP)')
        self.lt.insert(8,'--------------------------------------------------------------------')
        
    def close(self):
        self.window.destroy()
if __name__=='__main__':
    window=Tk()
    book=Library('Books',window)
    book.connect()
    book.lt.insert(0,'Library database is connected')
    

    
    window.mainloop()
        
            