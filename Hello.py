# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Compare Citation Based Recommendation and AI based",
        page_icon="👋",
    
    )
    st.header("Citation VS AI keyword",divider='rainbow')
    st.write("""These following recommendation engines are POCs that leverages different form of technology build by SA Frank and the Cortext Team. Due to the nature of the underlying logic of the citation-based recommendation, the current evaluation method could not accurately measure the perofmanece of this new recommendation.
        Therefore, to get a better understanding the the performance of the citation based recommendation, we decided to take a human evaluation approach""")
    st.divider()
    st.subheader (':blue[Rating Scale]')
    
    st.write("""Please rate these on a scale of 0-2:""")
    st.write(""":red[[0]] as the result is a bad recommendation that is not relevant to the target record""")
    st.write(""":blue[[1]] as the result is an average recommendation that covers at least a single concept from the target record""")
    st.write(""" :green[[2]] as the result is a good recommendation that covers two or all main concepts of the target record.""")
    
    st.write('Please rate the top 5 records from each engine')
    st.divider()
    st.subheader ('Recommendation Engines')
    col1, col2 = st.columns(2)

    with col1:
        st.header("Citation Based POC")
        st.write("""This is the citation based POC developed in [F76700](https://rally1.rallydev.com/#/?detail=/portfolioitem/feature/720287977253&fdp=true),which is a canidate for the recommendation engine 3.0.
                 This engine leverages the citing and refering relationship of the target record to find relevant record"""
                 )
    
    with col2:
        st.header("AI Key Word Based")
        st.write("These are AI keyword extraction based recommendation engine. Separatly, GPT 4 and GPT 3.5 turbo are used to extract key words from the record's title and abstract to build an advanced query to identify recommendations.")







    st.sidebar.success("Select an article above.")

    
   
   
    


if __name__ == "__main__":
    run()
