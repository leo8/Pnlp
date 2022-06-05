import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests
import json
from sklearn.preprocessing import MultiLabelBinarizer
from sentence_transformers import util, SentenceTransformer


model = pickle.load(open('model/model', 'rb'))
mlb = pickle.load(open('model/mlb_embeddings', 'rb'))
words_embeddings = pickle.load(open('model/words_embeddings', 'rb'))
all_tags = pickle.load(open('model/all_tags', 'rb'))


def get_random_request():

    response = requests.get("https://api.stackexchange.com/2.2/questions?site=stackoverflow&filter=withbody")
    raw_data = json.loads(response.text)
    data = raw_data['items'][0]
    
    return data


to_replace_substrings = ['<p>', '</p>',
                         '<a>', '</a>',
                         '<pre>', '</pre>',
                         '<code>', '</code>',
                         '<blockquote>', '</blockquote>',
                         '<em>', '</em>',
                         '<strong>', '</strong>',
                         '<br>', '</br>',
                         '<li>', '</li>',
                         '<ol>', '</ol>',
                         '\n'
                        ]


def tag_droper(text):
    for sub in to_replace_substrings:
        text = text.replace(sub, '')
    return text

def run():
    data_load_state = st.text('Loading data...')
    data = get_random_request()
    data_load_state.text('Loading data...done!')

    link = data['link']
    tags = data['tags']
    title = data['title']
    body = tag_droper(data['body'])
    text = title + ' ' + body


    st.text(f'Title : {title}')
    st.text(f'Link of the question : {link}')
    st.text(f'Original tags: {tags}')


    model_predict_state = st.text('Making predictions...')
    embeddings = model.encode(text)
    cosine_scores = util.cos_sim(embeddings, words_embeddings)
    predictions = [all_tags[int(e)] for e in cosine_scores.sort(descending=True)[1][0][0:3]]
    model_predict_state.text('Making predictions...done!')

    st.text(f'Suggested tags: {predictions}')


st.title('Question tagger')
if st.button('Run Predictions on random question'):
    run()

