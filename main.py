import numpy as np
import streamlit as st 
import random



#Generation de couple mission personne 


random.seed(40)
Ppl = ["","Lucas","Anto","Juliette","Val","Sixtine","CP","Amelie","Romain"]


Ppl2 = ["Lucas","Anto","Juliette","Val","Sixtine","CP","Amelie","Romain"]
random.shuffle(Ppl2)
Passe = ["","Cactus","moi","pasantoleplusbo","hakunamatata","vivelaluge","bouledeneige","racletteofromage","fondueofromage"]

msn =  open("ski_missions.txt","r",encoding="utf-8")  
Missions= []
for x in msn:
	Missions.append(x)

#st.write(Missions)


n = random.randint(100, 110)
tokill = ["Lucas","Anto","Juliette","Val","Sixtine","CP","Amelie","Romain"]
for i in range(len(tokill)):
	tokill[i]= Ppl2[(i+n)%8]

#st.write(Ppl2)
#st.write(tokill)
#st.write(Passe)


#Interface 


miss = random.sample(Missions,len(Ppl2))



st.title("Le jeu du killer pew pew :gun:")





st.sidebar.title("Choisis ton nom dans la liste :ski:")

ppl_log =st.sidebar.selectbox('Tu es :',Ppl)

index= Ppl.index(ppl_log)
index2 = Ppl2.index(ppl_log)

if ppl_log!="":
	st.write("Bienvenue "+ str(ppl_log) + ", entre ton mot de passe :closed_lock_with_key:")

	st.write("")

	user_input = st.text_input("le mot de passe :", " ")

	if user_input!="":
		
		if user_input== Passe[index]:
			st.write("Correct")

			st.title("Tu dois tuer : "+tokill[index2])
			st.title("Ta mission : "+miss[index2])






		else : 
			st.write("N'essaye pas de tricher, ce n'est pas bon !")

