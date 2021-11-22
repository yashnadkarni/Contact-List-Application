#---------------My Individual DB Design Project-------------------
#--------------Creator: Yash Nadkarni-----------------------------
#---------------Net-ID: ydn200000---------------------------------
from datetime import date
from os import stat
from re import L
from tkinter import font
from numpy import number, single
import pymysql.cursors
import pymysql
from tkinter import *
from tkcalendar import *
#import _tkinter

root= Tk()
root.geometry("950x750")#("750x350")
root.title("Contact Application")
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             db='yashdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor=connection.cursor()

#print(result)

def Search():
    result=[]
    query="select distinct c.contact_id from contact c join address a on c.contact_id=a.contact_id join Phone p on c.contact_id=p.contact_id join Date d on c.contact_id=d.contact_id where CONCAT(c.first_name,c.middle_name,c.last_name,a.address_type,a.address,a.city,a.state,a.zip,p.Phone_type,p.Area_code,p.Number,d.Date_type,d.Date) LIKE '%"+search_entry.get()+"%';"
    cursor.execute(query)
    result=cursor.fetchall()
    #print(result)
    contacts_list.delete(0,END)
    for i in range(len(result)):
        query1="select * from contact where contact_id="+str(result[i]['contact_id'])+";"
        cursor.execute(query1)
        rows=cursor.fetchall()
        for row in rows:
            temp=" "+row['first_name']+" "+row['middle_name']+" "+row['last_name']#str(row['contact_id'])
            contacts_list.insert(END,temp)
    


i=0
j=0
k=0
update_contact_count=0
delete_contact_count=0
contacts_added=0
user_address=[]
user_phone=[]
user_date=[]

addr_rows=[]
phone_rows=[]
date_rows=[]

asthetic_gap_2=Label(root,text=" ").grid(row=0,column=0)
details = Label(root,text="Contact Details", font="Verdana 20 bold").grid(row=0,column=1)

def display_all_contacts():
    contacts_list.delete(0,END)
    query1="select * from contact;"
    cursor.execute(query1)
    rows=cursor.fetchall()
    for row in rows:
        temp=" "+row['first_name']+" "+row['middle_name']+" "+row['last_name']#str(row['contact_id'])
        contacts_list.insert(END,temp)
    new_address_clear_function()
    new_phone_clear_function()
    new_dates_clear_function()

def get_rows(event):
    global addr_rows,phone_rows,date_rows
    global curr_contact_id
    new_address_clear_function()
    new_phone_clear_function()
    new_dates_clear_function()
    #del addr_rows[0:]
    add_user_details=contacts_list.get(contacts_list.curselection()[0]).split(" ")
    fname.delete(0,END)
    mname.delete(0,END)
    lname.delete(0,END)
    fname.insert(END,add_user_details[1])
    mname.insert(END,add_user_details[2])
    lname.insert(END,add_user_details[3:])#(DONE FOR O' HERN GUY)
    f_name_recover_id=contacts_list.get(contacts_list.curselection()[0]).split(" ")[1]
    m_name_recover_id=contacts_list.get(contacts_list.curselection()[0]).split(" ")[2]
    l_name_recover_id=contacts_list.get(contacts_list.curselection()[0]).split(" ")[3]
    cursor.execute("select contact_id from contact where first_name='"+f_name_recover_id+"' and middle_name='"+m_name_recover_id+"' and last_name='"+l_name_recover_id+"';")
    curr_contact_id=cursor.fetchone()['contact_id']
    address_list.delete(0,END)
    phone_list.delete(0,END)
    date_list.delete(0,END)
    cursor.execute("select address_type,address,city,state,zip from address where Contact_id="+str(curr_contact_id)+";")
    addr_rows=cursor.fetchall()
    for row in addr_rows:
        temp=" "+row['address_type']+" "+row['address']+" "+row['city']+" "+row['state']+" "+row['zip']#str(row['contact_id'])
        address_list.insert(END,temp)
    address_list.insert(END," ")
    address_list.insert(END,"#Want to add more? Click 'Add New Address' -> Enter Details -> click 'Add This Address'")
    #For phone
    cursor.execute("select Phone_type,Area_code,Number from Phone where Contact_id="+str(curr_contact_id)+";")
    phone_rows=cursor.fetchall()
    for row in phone_rows:
        temp=" "+row['Phone_type']+" "+row['Area_code']+"-"+row['Number']
        phone_list.insert(END,temp)
    #For Date
    cursor.execute("select Date_type,Date from Date where Contact_id="+str(curr_contact_id)+";")
    date_rows=cursor.fetchall()
    #print(date_rows)
    if date_rows==():
        date_list.insert(END,"No Dates present")
    for row in date_rows:
        temp=" "+row['Date_type']+" "+row['Date']
        date_list.insert(END,temp)
    #print(date_list)

display_contacts= Button(root, text="Display All Contacts",command=lambda:display_all_contacts())
display_contacts.grid(row=1,column=1)

contacts_list=Listbox(root,height=20,width=40,selectmode=single)
contacts_list.grid(row=2,column=1,rowspan=9,columnspan=2)
contacts_list.bind('<<ListboxSelect>>',get_rows)

fname_lb=Label(root, text = "First Name").grid(row=12,column=1)
mname_lb= Label(root ,text = "Middle Name").grid(row = 13,column = 1)
lname_lb = Label(root ,text = "Last Name").grid(row = 14,column = 1)

fname=Entry(root)
fname.grid(row=12,column=2)
mname = Entry(root)
mname.grid(row = 13,column = 2)
lname = Entry(root)
lname.grid(row = 14,column = 2)


#asthetic_gap_3=Label(root,text="  ").grid(row=1,column=4)
main_addr_label= Label(root,text="Addresses",font="Verdana 20 bold")
main_addr_label.grid(row=2,column=5,rowspan=4)
def fill_address_data(event):
    global addr_rows
    cur_addr=addr_rows[address_list.curselection()[0]]
    addr_type1.delete(0,END)
    addr1.delete(0,END)
    city1.delete(0,END)
    state1.delete(0,END)
    addr_zip1.delete(0,END)
    addr_type1.insert(END,cur_addr['address_type'])
    addr1.insert(END,cur_addr['address'])
    city1.insert(END,cur_addr['city'])
    state1.insert(END,cur_addr['state'])
    addr_zip1.insert(END,cur_addr['zip'][:-2:])

address_list=Listbox(root,height=5,width=40)
address_list.grid(row=2,column=6,rowspan=4,columnspan=4)
address_list.bind('<<ListboxSelect>>',fill_address_data)


addr_type_lb1=Label(root, text = "Address type").grid(row=6,column=5)
addr_lb1= Label(root ,text = "Address").grid(row = 7,column = 5)
city_lb1 = Label(root ,text = "City").grid(row = 8,column = 5)
state_lb1 = Label(root ,text = "State").grid(row = 9,column = 5)
zip_lb1 = Label(root ,text = "Zip").grid(row = 10,column = 5)
addr_type1=Entry(root)
addr_type1.grid(row=6,column=6)
addr1 = Entry(root)
addr1.grid(row = 7,column = 6)
city1 = Entry(root)
city1.grid(row = 8,column = 6)
state1 = Entry(root)
state1.grid(row = 9,column = 6)
addr_zip1 = Entry(root)
addr_zip1.grid(row = 10,column = 6)

def new_address_clear_function():
    addr_type1.delete(0,END)
    addr1.delete(0,END)
    city1.delete(0,END)
    state1.delete(0,END)
    addr_zip1.delete(0,END)

def add_new_addr_during_modify():
    global curr_contact_id
    cursor.execute("insert into address(Contact_id,address_type,address,city,state,zip) values ("+str(curr_contact_id)+",'"+addr_type1.get()+"','"+addr1.get()+"','"+city1.get()+"','"+state1.get()+"','"+addr_zip1.get()+".0');")
    connection.commit()
    new_address_clear_function()

add_more_address=Button(root,text="Add New Address",command=lambda:new_address_clear_function())
add_more_address.grid(row=6,column=7)

addr_reset_btn= Button(root,text='Add This Address',command=lambda:add_new_addr_during_modify())
addr_reset_btn.grid(row=10,column=7)

#Phone number details

def fill_phone_data(event):
    global phone_rows
    cur_phone=phone_rows[phone_list.curselection()[0]]
    phone_type.delete(0,END)
    phone.delete(0,END)
    phone_type.insert(END,cur_phone['Phone_type'])
    phone.insert(END,cur_phone['Area_code']+"-"+cur_phone['Number'])

main_phone_label= Label(root,text="Phone/s",font="Verdana 20 bold")
main_phone_label.grid(row=11,column=5,rowspan=4)

phone_list=Listbox(root,height=4,width=40)
phone_list.grid(row=11,column=6,rowspan=4,columnspan=4)
phone_list.bind('<<ListboxSelect>>',fill_phone_data)

phone_type_lb= Label(root ,text = "Phone Type").grid(row = 15,column = 5)
phone_lb = Label(root ,text = "Phone Number").grid(row = 16,column = 5)

phone_type=Entry(root)
phone_type.grid(row=15,column=6,pady=10)
phone = Entry(root)
phone.grid(row = 16,column = 6,pady=10)

def new_phone_clear_function():
    phone_type.delete(0,END)
    phone.delete(0,END)

def add_new_phone_during_modify():
    global curr_contact_id
    cursor.execute("insert into Phone(Contact_id,Phone_type,Area_code,Number) values ("+str(curr_contact_id)+",'"+phone_type.get()+"','"+phone.get()[0:3]+"','"+phone.get()[4:]+"');")
    connection.commit()
    new_phone_clear_function()

add_new_number=Button(root,text="Add New Number",command=lambda:new_phone_clear_function())
add_new_number.grid(row=15,column=7)

add_phone_btn= Button(root,text='Add This Number',command=lambda:add_new_phone_during_modify())
add_phone_btn.grid(row=16,column=7)

#Date details

def fill_date_data(event):
    global date_rows
    cur_date=date_rows[date_list.curselection()[0]]
    print(cur_date)
    date_type.delete(0,END)
    date1.delete(0,END)
    date_type.insert(END,cur_date['Date_type'])
    date1.insert(END,cur_date['Date'])

main_date_label= Label(root,text="Date/s",font="Verdana 20 bold")
main_date_label.grid(row=17,column=5,rowspan=4)

date_list=Listbox(root,height=4,width=40)
date_list.grid(row=17,column=6,rowspan=4,columnspan=4)
date_list.bind('<<ListboxSelect>>',fill_date_data)

date_type_lb= Label(root ,text = "Date Type").grid(row = 21,column = 5)
phone_lb = Label(root ,text = "Date").grid(row = 22,column = 5)

date_type=Entry(root)
date_type.grid(row=21,column=6,pady=10)
date1 = Entry(root)
date1.grid(row = 22,column = 6,pady=10)

def new_dates_clear_function():
    date_type.delete(0,END)
    date1.delete(0,END)

def add_new_date_during_modify():
    global curr_contact_id
    cursor.execute("insert into Date(Contact_id,Date_type,Date) values ("+str(curr_contact_id)+",'"+date_type.get()+"','"+date1.get()+"');")
    connection.commit()
    new_dates_clear_function()

add_more_dates=Button(root,text="Add New Date",command=lambda:new_dates_clear_function())
add_more_dates.grid(row=21,column=7)

date_add_btn= Button(root,text='Add This Date',command=lambda:add_new_date_during_modify())
date_add_btn.grid(row=22,column=7)


#Search Box
search_entry= Entry(root)
search_entry.grid(row = 0,column = 5)
search_btn=Button(root,text="Search", command=lambda:Search())
search_btn.grid(row=0,column=6)


def insert_data_window():
     
    # Toplevel object which will
    # be treated as a new window
    insert_window = Toplevel(root)
    # sets the title of the Toplevel widget
    insert_window.title("Add Details")
    # sets the geometry of toplevel
    insert_window.geometry("680x380")
    # A Label widget to show in toplevel
    global contacts_added
    contacts_added=0
    #User Details----------------------------------------------------------------------------------
    details = Label(insert_window,text="User Details", font="Verdana 20 bold").grid(row=0,column=0)
    f_name_lb= Label(insert_window ,text = "First Name").grid(row = 1,column = 0)
    m_name_lb= Label(insert_window ,text = "Middle Name").grid(row = 2,column = 0)
    l_name_lb= Label(insert_window ,text = "Last Name").grid(row = 3,column = 0)
    f_name= Entry(insert_window)
    f_name.grid(row = 1,column = 1)
    m_name = Entry(insert_window)
    m_name.grid(row = 2,column = 1)
    l_name = Entry(insert_window)
    l_name.grid(row = 3,column = 1)

    asthetic_gap=Label(insert_window,text=" ").grid(row=0,column=2)

    #Adddress Details----------------------------------------------------------------------------------
    address_title = Label(insert_window,text="Add Address", font="Verdana 20 bold").grid(row=4,column=0)

    def clear_addresses():
        global user_address,address_count
        global i
        i+=1
        temp_addr_type="'"+addr_type.get()+"'"
        temp_addr="'"+addr.get()+"'"
        temp_city="'"+city.get()+"'"
        temp_state="'"+state.get()+"'"
        temp_zip="'"+addr_zip.get() + ".0"+"'"
        if temp_addr_type=="":temp_addr_type="''"
        if temp_addr=="":temp_addr="''"
        if temp_city=="":temp_city="''"
        if temp_state=="":temp_state="''"
        if temp_zip=="":temp_zip="''"
        temp1="insert into address(Contact_id,address_type,address,city,state,zip) values(,"+temp_addr_type+","+temp_addr+","+temp_city+","+temp_state+","+temp_zip+");"
        user_address.append(temp1)
        address_count = Label(insert_window,text=str(i)+" address(es) added", font="Verdana 15 ")
        address_count.grid(row=4,column=1)
        addr_type.delete(0,END)
        addr.delete(0,END)
        city.delete(0,END)
        state.delete(0,END)
        addr_zip.delete(0,END)
    
    addr_type_lb=Label(insert_window, text = "Address type").grid(row=6,column=0)
    addr_lb= Label(insert_window ,text = "Address").grid(row = 7,column = 0)
    city_lb = Label(insert_window ,text = "City").grid(row = 8,column = 0)
    state_lb = Label(insert_window ,text = "State").grid(row = 9,column = 0)
    zip_lb = Label(insert_window ,text = "Zip").grid(row = 10,column = 0)
    addr_type=Entry(insert_window)
    addr_type.grid(row=6,column=1)
    addr = Entry(insert_window)
    addr.grid(row = 7,column = 1)
    city = Entry(insert_window)
    city.grid(row = 8,column = 1)
    state = Entry(insert_window)
    state.grid(row = 9,column = 1)
    addr_zip = Entry(insert_window)
    addr_zip.grid(row = 10,column = 1)
    addr_submit=Button(insert_window,text="Add Address", command=lambda:clear_addresses())
    addr_submit.grid(row=11,column=0)

    #Phone Details----------------------------------------------------------------------------------
    phone_title = Label(insert_window,text="Add Phone", font="Verdana 20 bold").grid(row=0,column=4)

    def clear_phone():
        global user_phone,phone_count
        global j
        j+=1
        temp_phone_type="'"+phone_type.get()+"'"
        temp_phone="'"+phone.get()+"'"
        if temp_phone_type=="":temp_phone_type="''"
        if temp_phone=="":temp_phone="''"
        temp2="insert into Phone(Contact_id,Phone_type,Area_code,Number) values(,"+temp_phone_type+","+temp_phone[0:4]+"','"+temp_phone[5:]+");"
        user_phone.append(temp2)
        phone_count = Label(insert_window,text=str(j)+" phone(s) added", font="Verdana 15 ")
        phone_count.grid(row=0,column=5)
        phone_type.delete(0,END)
        phone.delete(0,END)

    phone_type_lb=Label(insert_window, text = "Phone type").grid(row=1,column=4)
    phone_lb = Label(insert_window ,text = "Phone").grid(row = 2,column = 4)
    phone_type=Entry(insert_window)
    phone_type.grid(row=1,column=5)
    phone = Entry(insert_window)
    phone.grid(row = 2,column = 5)
    phone.insert(0,"xxx-xxx-xxxx")

    phone_submit=Button(insert_window,text="Add Number", command=lambda:clear_phone())
    phone_submit.grid(row=3,column=4)

    #Date Details----------------------------------------------------------------------------------

    Date_title = Label(insert_window,text="Add Date", font="Verdana 20 bold").grid(row=4,column=4)

    def clear_date():
        global user_date,date_count
        global k
        k+=1
        temp_date_type="'"+date_type.get()+"'"
        temp_date="'"+str(date1.get_date())+"'"
        if temp_date_type=="":temp_date_type="''"
        if temp_date=="":temp_date="''"
        temp3="insert into Date(Contact_id,Date_type,Date) values(,"+temp_date_type+","+temp_date+");"
        user_date.append(temp3)
        date_count = Label(insert_window,text=str(k)+" date(s) added", font="Verdana 15 ")
        date_count.grid(row=4,column=5)
        date_type.delete(0,END)

    date_type_lb=Label(insert_window, text = "Date type").grid(row=6,column=4)
    date_lb = Label(insert_window ,text = "Date").grid(row = 7,column = 4)
    date_type=Entry(insert_window)
    date_type.grid(row=6,column=5)
    date1=DateEntry(insert_window, locale='en_US', date_pattern='yyyy-mm-dd')
    date1.grid(row=7,column=5)
    date_submit=Button(insert_window,text="Add date", command=lambda:clear_date())
    date_submit.grid(row=8,column=4)

    #All values insert function
    def insert_values_in_db():
        global date_count,address_count,phone_count,i,j,k
        # address_count.destroy()
        # phone_count.destroy()
        # date_count.destroy()
        #print("***************************************")
        global contacts_added,i,j,k,number_of_entries
        global user_address,user_date,user_phone
        #Code to insert all values in db
        contact_query="insert into contact(first_name,middle_name,last_name) values('"+f_name.get()+"','"+m_name.get()+"','"+l_name.get()+"');"
        cursor.execute(contact_query)
        connection.commit()
        cursor.execute("select contact_id from contact order by contact_id desc limit 1")
        c_id=cursor.fetchone()
        for each_addr in user_address:
            each_addr=each_addr[0:75]+str(c_id.get("contact_id"))+each_addr[75:]
            cursor.execute(each_addr)
            connection.commit()
        for each_phone in user_phone:
            each_phone=each_phone[0:65]+str(c_id.get("contact_id"))+each_phone[65:]   
            cursor.execute(each_phone) 
            connection.commit()
        for each_date in user_date:
            each_date=each_date[0:51]+str(c_id.get("contact_id"))+each_date[51:]   
            cursor.execute(each_date)
            connection.commit()
        #print("ALL VALUES INSERTED")
        #Search()
        contacts_added+=1
        number_of_entries= Label(insert_window,text=str(contacts_added)+" contact(s) added", font="Verdana 15 ").grid(row=21,column=4)
        print(f_name.get()+" "+m_name.get()+" "+l_name.get())
        print(user_address,user_date,user_phone)
        del user_address[0:]
        del user_phone[0:]
        del user_date[0:]
        f_name.delete(0,END)
        m_name.delete(0,END)
        l_name.delete(0,END)
        i=0
        j=0
        k=0
        #print("***************************************")

    submit_all=Button(insert_window,text="SUBMIT",padx=50,command=lambda:insert_values_in_db())
    submit_all.grid(row=21,column=5)
    exit_btn=Button(insert_window,text="Click to exit",command=lambda:insert_window.destroy())
    exit_btn.grid(row=22,column=0)
    


new_window=Button(root,text="Add New Contact",command=lambda:insert_data_window())
new_window.grid(row=15,column=1,rowspan=2)

def update_function():
    global update_contact_count
    print("in update table")
    upt_fname=fname.get()
    upt_mname=mname.get()
    upt_lname=lname.get()
    #print(upt_fname,upt_mname,upt_lname)
    upt_addr_type=addr_type1.get()
    upt_addr=addr1.get()
    upt_city=city1.get()
    upt_state=state1.get()
    upt_zip=addr_zip1.get()
    
    upt_phone_type=phone_type.get()
    upt_area_code = phone.get()[0:3]
    upt_phone=phone.get()[4:]

    upt_date_type=date_type.get()
    upt_date=date1.get()

    cursor.execute("update contact set first_name='"+upt_fname+"',middle_name='"+upt_mname+"',last_name='"+upt_lname+"' where contact_id="+str(curr_contact_id)+";")
    connection.commit()
    cursor.execute("update address set address_type='"+upt_addr_type+"',address='"+upt_addr+"',city='"+upt_city+"',state='"+upt_state+"',zip='"+upt_zip+"' where Contact_id="+str(curr_contact_id)+" and address_type='"+upt_addr_type+"';")
    connection.commit()
    cursor.execute("update Phone set Phone_type='"+upt_phone_type+"',Area_code='"+upt_area_code+"',Number='"+upt_phone+"' where contact_id="+str(curr_contact_id)+" and Phone_type='"+upt_phone_type+"';")
    connection.commit()
    cursor.execute("update Date set Date_type='"+upt_date_type+"',Date='"+upt_date+"' where contact_id="+str(curr_contact_id)+" and Date_type='"+upt_date_type+"';")
    connection.commit()
    update_contact_count+=1
    update_count=Label(root,text=str(update_contact_count)+" update/s done",font="Verdana 15").grid(row=17,column=2)


update_contact=Button(root,text="Update This Contact",command=lambda:update_function())
update_contact.grid(row=17,column=1,rowspan=2)

def delete_contact_function():
    global delete_contact_count,curr_contact_id
    cursor.execute("delete from address where Contact_id="+str(curr_contact_id)+";")
    connection.commit()
    cursor.execute("delete from Phone where Contact_id="+str(curr_contact_id)+";")
    connection.commit()
    cursor.execute("delete from Date where Contact_id="+str(curr_contact_id)+";")
    connection.commit()
    cursor.execute("delete from contact where contact_id="+str(curr_contact_id)+";")
    connection.commit()
    delete_contact_count+=1
    delete_contact=Label(root,text=str(delete_contact_count)+" delete/s done",font="Verdana 15").grid(row=19,column=2)
    

delete_contact_btn=Button(root,text="Delete This Contact",command=lambda:delete_contact_function())
delete_contact_btn.grid(row=19,column=1,rowspan=2)


root.mainloop()
#connection.commit()
connection.close()


'''
SEARCH QUERY 

select c.contact_id,c.first_name,c.middle_name,c.last_name,a.address_type,a.address,a.city,a.state,a.zip,p.Phone_type,p.Area_code,p.Number,d.Date_type,d.Date
 from contact c 
 join address a on c.contact_id=a.contact_id
 join Phone p on c.contact_id=p.contact_id
 join Date d on c.contact_id=d.contact_id
 where CONCAT(c.first_name,c.middle_name,c.last_name,a.address_type,a.address,a.city,a.state,a.zip,p.Phone_type,p.Area_code,p.Number,d.Date_type,d.Date) LIKE "%Brand%";'''

