# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 11:15:59 2021

@author: Admin
"""





import streamlit as st
import os
import pandas as pd
import pickle
from xgboost import XGBClassifier
import random


st.set_page_config(layout="wide")




@st.cache
def get_data(filename):
    df = pd.read_csv(filename)
    
    return df



df = get_data('df_all_processedf4.csv')

#loaded_model = pickle.load(open(filename, 'rb'))



def main():
        """medicine review app"""
        
        st.title("Medicine Review & Its SideEffect Web App")
        #st.subheader("Created by ProjectBatch:P55 Team:6 Excelr Solutions:")
     
        menu = ["Single"]
        
        df = pd.read_csv('df_all_processedf4.csv')
        
        choice = st.sidebar.selectbox("Menu", menu)
        
        condition_list = df["condition"].unique().tolist()
        condition_name = st.sidebar.selectbox("Please Select Your Condition From List", condition_list)

       # output = st.text_input("Enter Your Illness Condition", condition_name) 
        with st.info("Please find the Drug Name List below wrt Illness Condition"):
                retrived_df = df[df["condition"].str.contains(condition_name, na=False)]
                                 
        st.dataframe(retrived_df[["drugName"]])
       
        
        if choice == "Single":
            st.subheader("Please Check Below For More Details wrt Drug")
            condition_list = df["condition"].unique().tolist()
            drug_list = retrived_df["drugName"].tolist()
            #condition_name = st.sidebar.selectbox("Condition List", condition_list)
            drug = st.selectbox("Please Select Drug From List", drug_list)
            drug_df = df[(df["condition"] == condition_name) & (df["drugName"] == drug)]
            rating = df['rating']
            
            # layout
            

            c1, c2 = st.beta_columns([5, 1])
            
            
            # Single slection layout
            with c1:
                
                
                try:
                    selected_conditionname = drug_df[
                         (drug_df["drugName"] == drug)
                   ]
       
                    st.write(selected_conditionname)
                   
                   
                except:
                       st.info("Please Check below")
            
            
                    
            with c2:
                
                
                rating_list = range(10)
                rat_choice = random.choice(rating_list)
                random_condition_name = random.choice(condition_list)
                rand_drug_df = df[df["condition"] == random_condition_name]
                
                try:
                    randomly_selected_conditionname = rand_drug_df[
                        (rand_drug_df["rating"] == rat_choice)
                    ]
                    mytext = randomly_selected_conditionname
                except:
                    mytext = rand_drug_df[
                        (rand_drug_df["rating"] == 1)
                    ]
                    
            
                
                 
         
            
            

if __name__ == '__main__':
        main()