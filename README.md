# Contact-List-Application
A database host application with a GUI where users can search, view, add, update and delete contacts


QUICK START GUIDE

Welcome to my Contacts Application. This application is used to display, modify, insert and delete contacts. This is very similar to the contact applications we have on our mobile devices.

Requirements:
1.	Python3
2.	MySQL
3.	Tkinter & TkCalendar
4.	MacOS or Windows
5.	Recommended IDE: Microsoft Visual Studio

Recommended OS: MacOS
IDE: Visual Studio Code

Technical Dependencies:
▪ Python3
▪ pymysql
▪ MySQL
▪ Tkinter,TkCalender

Steps to install necessary software
• Install python3 on your PC or Mac(Version used in the project: 3.9.7 64 bit)
• This can be done by pip in command line or home-brew in Mac
• Command: pip install python3 (To check version: python3 -v)
• Install MySQL on your computer by package installer
• Visit tis site for further details: https://dev.mysql.com/doc/refman/5.7/en/macos-installation-pkg.html
• Install Tkinter and TkCalender
• Command line: pip install tk;  If it does not work, try brew install python-tk
• For calendar: pip install tkCalender
• Install pymysql
• For more details, visit : https://pypi.org/project/PyMySQL/

Open db-start.py and run it.

Installation:
	Fill the database with the data present from the Contacts.csv file
(For details, refer info-to-add-data-from-db-to-csv)
	Run the db-start.py

Once the application is loaded,
	Click on ‘Display All Contacts’. All Contact names should appear on a textbox below.
	Click on any name to access their details like address, phone number and dates.
	If you wish to get more details, click on the items inside to textbox so that they will be displayed on the corresponding text entries.
	Change any entry if you wish to do so and just click on update this contact.
	If you wish to add a field, for eg: address, phone, date to your existing contact, simply click on Add New address/phone/date, enter the values and click Add This Address, Phone, Date.
	If you want to delete a contact, just click on delete this contact. Click on display all contacts again to see the refreshed set of contacts.
	In order to insert a contact, click on add new contact. This will open a new page which will have a form to add a contact.
	While adding an address, once you fill the form, click on add address. A label will show you how many addresses you have added. Without this, the address won’t be added. The same is applicable to Add Phone and Add Date.
	After filling out everything, click on the submit button. If you wish to add more contacts, just repeat the same process. A text will show how many contacts you have added.

