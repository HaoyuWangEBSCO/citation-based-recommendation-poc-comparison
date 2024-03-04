

import streamlit as st
from streamlit.logger import get_logger
import pandas as pd


st.set_page_config(
        page_title="Compare Citation Based Recommendation and AI based",
        layout="wide"

    )
st.header("Citation VS AI keyword",divider='rainbow')




compare=pd.read_csv(r"citation_based_comparison_deduped.csv")
compare['rating']=0

oaid=compare['oa_id'].drop_duplicates().tolist() 
oa_id_sample='W4281697563'
st.write(':blue[W4281697563]')

ogtitle=compare[compare['oa_id']==oa_id_sample]['original'].drop_duplicates()
oGab=compare[compare['oa_id']==oa_id_sample]['OGab'].drop_duplicates()

st.subheader('Original Article')

st.write(':blue[Title]')
st.write(ogtitle.item())
st.write(':blue[Abstract]')
st.write(oGab.item())

st.divider()
st.subheader('Recommended Article')
sampledata=compare[compare['oa_id']==oa_id_sample]

st.header(":green[Citation Based]")
edited_df_citation_based = st.data_editor(
    sampledata[sampledata['Engine']=='Citation Based'][['ranking','Re_record_title','Re_record_ab','queries/concepts','rating']].reset_index(drop=True,inplace=False),
    column_config={
        "ranking": "Ranking",
        'Re_record_title':"Title",
        'Re_record_ab':"Abstract",
        'queries/concepts':'Concept',
        'rating': st.column_config.NumberColumn(
            "Your rating",
            help="How much do you like this command (1-3)?",
            min_value=0,
            max_value=2,
            step=1)},
    disabled=["command", "is_widget"],
hide_index=True,)

st.divider()
st.header(":green[Gpt 3.5]")
edited_df_35= st.data_editor(
    sampledata[sampledata['Engine']=='gpt 3.5 turbo abstract keywords'][['ranking','Re_record_title','Re_record_ab','queries/concepts','rating']].reset_index(drop=True,inplace=False),
    column_config={
        "ranking": "Ranking",
        'Re_record_title':"Title",
        'Re_record_ab':"Abstract",
        'queries/concepts':'Concept',
        'rating': st.column_config.NumberColumn(
            "Your rating",
            help="How much do you like this command (0-2)?",
            min_value=0,
            max_value=2,
            step=1)},
    disabled=["command", "is_widget"],
hide_index=True,)

st.divider()

st.header(":green[GPT 4]")
edited_df_4= st.data_editor(
    sampledata[sampledata['Engine']=='gpt 4 abstract keywords'][['ranking','Re_record_title','Re_record_ab','queries/concepts','rating']].reset_index(drop=True,inplace=False),
    column_config={
        "ranking": "Ranking",
        'Re_record_title':"Title",
        'Re_record_ab':"Abstract",
        'queries/concepts':'Concept',
        'rating': st.column_config.NumberColumn(
            "Your rating",
            help="How much do you like this command (0-2)?",
            min_value=0,
            max_value=2,
            step=1,)},
    disabled=["command", "is_widget"],
    hide_index=True,)



saved=st.button('Save')

if saved: 
    edited_df_citation_based['Engine']='Citation Based'

    edited_df_35['Engine']='gpt 3.5 turbo abstract keywords'
    edited_df_4['Engine']='gpt 4 abstract keywords'

    allrated=pd.concat([edited_df_citation_based,edited_df_35,edited_df_4])

    allrated['oa_id']=oa_id_sample
    allrated['OG_title']=ogtitle.item()

    allrated['OG_ab']=oGab.item()
    filename=r"C:\Users\hwang\Desktop\related content API testing\Citation based\rated\{}.csv".format(oa_id_sample)
    allrated.to_csv(filename)
    st.write('The Rating is Saved')
    saved=False 