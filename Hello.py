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
    st.write('These following recommendation engines are POCs that leverages different form of technology build by SA Frank and the Cortext Team. Due to the nature of the underlying logic of the citation-based recommendation, the current evaluation method could not accurately measure the perofmanece of this new recommendation.
    Therefore, to get a better understanding the the performance of the citation based recommendation, we decided to take a human evaluation approach')
    st.divider()
    st.subheader ('Rating Scale')
    
    st.write("Please rate these on a scale of 0-2,
    0 as the result is not relevant to the target record,
    1 as the result is covering a single concept from the target record or an average recommendation, 
    2 as the result is good recommendation or covering two or all main concepts of the target record.")
    
    st.divider()
    st.subheader ('Recommendation Engines')
    st.write(Citation Based Recommendation
    





    st.sidebar.success("Select an article above.")

    
   
   
    


if __name__ == "__main__":
    run()
