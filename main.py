# import tkinter as tk
# import mysql.connector


# cnx = mysql.connector.connect(
#     host='localhost', user='root', password='f1309D1309')

# cursor = cnx.cursor()
# cursor.execute('use UserInfo')
# cursor.execute('show tables')
# for x in cursor:
#     print(x)
# root = tk.Tk()
# root.geometry('500x300')

# tk.Label(master=root, text='Name').pack()
# name_entry = tk.Entry(master=root)
# name_entry.pack()

# tk.Label(master=root, text='Surname').pack()
# surname_entry = tk.Entry(master=root)
# surname_entry.pack()

# tk.Label(master=root, text='Card Number').pack()
# card_number_entry = tk.Entry(master=root)
# card_number_entry.pack()


# def save_to_db():
#     name = name_entry.get()
#     surname = surname_entry.get()
#     cardnumber = card_number_entry.get()

#     query = 'INSERT INTO information (name, surname, card_number) VALUES (%S, %S, %S)'
#     cursor.execute(query, (name, surname, cardnumber))
#     cnx.commit()


# tk.Button(master=root, text='Submit', command=save_to_db).pack()

# root.mainloop()


# cnx.close()


# import tkinter as tk
# import mysql.connector


# def save_to_db():
#     name = name_entry.get()
#     surname = surname_entry.get()
#     cardnumber = card_number_entry.get()

#     try:
#         # Initialize database connection
#         conn = mysql.connector.connect(
#             host='localhost',  # Replace with your MySQL server address
#             user='root',  # Replace with your MySQL username
#             password='f1309D1309',  # Replace with your MySQL password
#             database='mysql'  # Replace with your database name
#         )
#         cursor = conn.cursor()
#         print(conn)
#         print(cursor)

#         # Insert data into the database
#         query = '''
# use UserInfo


# '''

#         cursor.execute(query)
#         conn.commit()
#         query = 'INSERT INTO information (name, surname, card_number) VALUES (%s, %s, %s)'
#         cursor.execute(query, (name, surname, cardnumber))
#         conn.commit()

#         print("Data saved successfully!")
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#     finally:
#         cursor.close()
#         conn.close()


# # Create the Tkinter window
# root = tk.Tk()
# root.geometry('500x300')
# root.title("Database Entry Form")

# # Create input fields
# tk.Label(root, text="Name").pack()
# name_entry = tk.Entry(root)
# name_entry.pack()

# tk.Label(root, text="Surname").pack()
# surname_entry = tk.Entry(root)
# surname_entry.pack()

# tk.Label(root, text="Card Number").pack()
# card_number_entry = tk.Entry(root)
# card_number_entry.pack()

# # Create a button to save data
# tk.Button(root, text="Save to Database", command=save_to_db).pack()

# # Start the Tkinter event loop
# root.mainloop()


# from tkinter import Tk, Button, Label, filedialog
# from PIL import Image, ImageTk
# import mysql.connector

# root = Tk()
# root.geometry('600x300')
# root.title('Save Image')


# def save_image():
#     file_path = filedialog.askopenfilename(
#         filetypes=[('Image Files', '*,png *.jpg *.jpeg')])

#     try:
#         cnx = mysql.connector.connect(
#             host='localhost', user='root', password='f1309D1309', database='mysql')
#         cursor = cnx.cursor()
#         image = Image.open(file_path)
#         query = 'USE UserInfo'
#         cursor.execute(query)
#         cnx.commit()
#         print("Data saved successfully!")
#         img_byte_array = bytearray(image.tobytes())
#         cursor.execute('INSERT INTO info (image) VALUES (?)',
#                        (img_byte_array, ))
#         cnx.commit()
#         print('Image Saved......')
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#     finally:
#         cursor.close()
#         cnx.close()


# label = Label(master=root, text='Image Save Into db')
# label.pack()


# save = Button(master=root, text='Save', command=save_image)
# save.pack()


# root.mainloop()


# import mysql.connector
# import base64
# from PIL import Image
# import tkinter as tk
# from tkinter import filedialog
# import io


# root = tk.Tk()
# root.title('Saving image')


# def upload_image():
#     file_path = filedialog.askopenfilename(
#         filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if file_path:
#         with open(file_path, 'rb') as f:
#             image_data = f.read()

#         encode_data = base64.b64encode(image_data)

#         mydb = mysql.connector.connect(
#             host='localhost', user='root', password='f1309D1309', database='student')
#         cursor = mydb.cursor()
#         query = 'INSERT INTO profilst(name, image) VALUES (%s, %s)'
#         data = ("sample_image.png", encode_data)
#         cursor.execute(query, data)
#         mydb.commit()
#         mydb.close()

#         # Display a success message
#         tk.messagebox.showinfo("Success", "Image uploaded successfully!")


# # Create a button to upload the image
# button = tk.Button(root, text="Upload Image", command=upload_image)
# button.pack(pady=20)

# # Run the tkinter event loop
# root.mainloop()
