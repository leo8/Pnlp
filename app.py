import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import MultiLabelBinarizer
from sentence_transformers import util, SentenceTransformer

model = pickle.load(open(model/model, 'rb'))
mlb = pickle.load(open(model/mlb_embeddings, 'rb'))
word_embeddings = pickle.load(open(model/word_embeddings, 'rb'))

st.title('Question tagger')



def tag_droper(text):
    for sub in to_replace_substrings:
        text = text.replace(sub, '')
    return text
    
raw_data['Body'] = raw_data['Body'].apply(tag_droper)
raw_data['FullPost'] = raw_data['Title'] + ' ' + raw_data['Body']