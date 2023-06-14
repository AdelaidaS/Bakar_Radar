import streamlit
import requests
import validators
import pandas as pd
from PIL import Image
import streamlit as st
import numpy as np
import hashlib
import os

os.chdir(os.path.dirname(__file__))

st.title('Proyecto Bakar Radar')


image = Image.open('./pages/soledad.jpg')
st.image(image, use_column_width=True)


# Convert Pass into hash format
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

# Check password matches during login
def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

# DB Management
import sqlite3 
conn = sqlite3.connect('user_data.db')
c = conn.cursor()
# DB Functions for create table
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,email TEX, password TEXT)')

# Insert the data into table
def add_userdata(username,email,password):
	c.execute('INSERT INTO userstable(username,email,password) VALUES (?,?,?)',(username,email,password))
	conn.commit()

# Password and email fetch
def login_user(email,password):
	c.execute('SELECT * FROM userstable WHERE email =? AND password = ?',(email,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

'''Muchas personas mayores, independientemente de su situación de convivencia, experimentan sentimientos de soledad no deseada en algún momento de su vida.'''
'''Ante el aumento de personas mayores en riesgo de soledad, el proyecto Bakar Radar propone una interesante unión entre la Estadística, Inteligencia Artificial y la Administración Pública.'''
'''Vamos a mostrar cómo el empleo de :red[algoritmos de aprendizaje automático] puede servir para mejorar la calidad de vida de las personas mayores, para optimizar los recursos de las Administraciones y reducir el impacto de la soledad no deseada en la población.'''  

# Main function
def main():
	#"""Login page"""
	st.subheader("Acceso a la App Soledad")
	menu = ["Acceder","Regístrate"]
	choice = st.selectbox("Registro o Acceso a la App_Soledad", menu,)
	st.markdown(
     "<h10 style='text-align: left; color: #ffffff;'> If you do not have an account, create an accouunt by select SignUp option from above dropdown box.</h10>",
     unsafe_allow_html=True
     )
	if choice == "":
		st.subheader("Acceder")
	elif choice == 'Acceder':
		st.write('-------')
		#st.subheader('Accede a la App')

		email = st.text_input("Usuario",placeholder='email')
		
		password = st.text_input("Password",type='password')
  
		if st.checkbox("Acceder"):
			# if password == '12345':
			# Hash password creation and store in a table
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(email,check_hashes(password,hashed_pswd))
			if result:

				st.success("Introduce aqui tus calves de acceso {}".format(email))

				
				if st.success:
					st.subheader("Usuario")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Usuario","Email","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")
	elif choice == "Regístrate":
		st.write('-----')
		st.subheader("Crea una nueva cuenta")
		new_user = st.text_input("Usuario",placeholder='name')
		new_user_email = st.text_input('Email',placeholder='email')
		new_password = st.text_input("Password",type='password')

		if st.button("Regístrate"):
			if new_user == '':     # if user name empty then show the warnings
				st.warning('Nombre de usuario erroneo')
			elif new_user_email == '':   # if email empty then show the warnings
				st.warning('email no reconocido')
			elif new_password == '':   # if password empty then show the warnings
				st.warning('Contraseña incorrecta')
			else:
				create_usertable()
				add_userdata(new_user,new_user_email,make_hashes(new_password))
				st.success("You have successfully created a valid Account")
				st.info("Go up and Login to you account")


if __name__ == '__main__':
	main()