import streamlit as st
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import UnstructuredURLLoader
from langchain.llms import VertexAI
from langchain.memory import ConversationBufferMemory
from gnews import GNews
from langchain.prompts import PromptTemplate


# Initialize GNews object
google_news = GNews()
google_news.period = '1d'  # News from last 1 days
google_news.max_results = 5 # Number of responses across a keyword
google_news.country = 'USA' # News from a specific country 
google_news.language = 'en'  # News in English
google_news.exclude_websites = ['yahoo.com', 'cnn.com', 'msn.con', 'reuters.com'] # Exclude news from specific website i.e Yahoo.com and CNN.com
#google_news.start_date = (2024, 5, 10) # Search from 1st Jan 2023\n",
#google_news.end_date = (2024, 5, 20) # Search until 1st April 2023\n",

# Initialize LLM model
llm = VertexAI(temperature=0.1,
               model='text-bison-32k',
               top_k=40,
               top_p=0.8,
               max_output_token=2048)



llm2 = VertexAI(temperature=0.8,
               model='text-bison-32k',
               top_k=40,
               top_p=0.8,
               max_output_token=2048)

def generate_summary(news_articles):
    # Prompt template for summarization
    prompt_template = """Generate summary for the following text, using the following steps:
                         
                         1. If the text cannot be found or error, return: "Content empty"
                         2. Use only materials from the text supplied
                         3. Create summary in English
                         4. Don't stop half way of sentence
                         5. Generate the summary concisely
                         6. Generate the summaries with maximum 300 words only
                         
                        {text}
                        
                        SUMMARY:"""
    prompt = PromptTemplate.from_template(prompt_template)

    # Generate summary for each news item
    for i, article in enumerate(news_articles[:5]):
        # Extract news content
        loader = UnstructuredURLLoader(urls=[article['url']])
        data = loader.load()
        
        # Summarize using langchain for easy processing
        chain = load_summarize_chain(llm,
                                    chain_type="stuff",
                                    prompt=prompt,
                                    )
        summary = chain.run(data)  # Pass only positional arguments
        
        if article['title'] != "[Removed]" and summary.strip() != "Content empty":
            # Post-process the summary to ensure it ends with a complete sentence
            if not summary.endswith(('.', '!', '?')):
                summary += '.'  # Append a period if the summary doesn't end with punctuation
            
            
        st.success(f"Title: {article['title']}\n\nLink: {article['url']}\n\nSummary: {summary}")
           

def generate_dissummary(news_articles):
    # Prompt template for summarization
    prompt_template = """Generate a biased summary from the perspectives of the involved parties using the following steps:
                     1. Always show both perspectives with their personality
                     2. If the text cannot be found or an error occurs, return: "Content empty"
                     3. Create summaries in English
                     4. Summarize using each person's personality with a critical viewpoint
                     5. Don't forget to include both party's perspective
                     6. Always finish the sentences
                     7. If the text cannot be found or error, return: "Content empty"

                    
                    
                     First Party's Perspective:
                     {text}
                     
                     Second Party's Perspective:
                     {text}
                     
                     SUMMARY:"""

    prompt = PromptTemplate.from_template(prompt_template)

    # Generate summary for each news item
    for i, article in enumerate(news_articles[:5]):
        # Extract news content
        loader = UnstructuredURLLoader(urls=[article['url']])
        data = loader.load()

        # Summarize using langchain for easy processing
        chain = load_summarize_chain(llm2,
                                    chain_type="stuff",
                                    prompt=prompt
                                   )
        summary = chain.run(data)  # Pass only positional arguments

        if article['title'] != "[Removed]" and summary.strip() != "Content empty":
            # Post-process the summary to ensure it ends with a complete sentence
            if not summary.endswith(('.', '!', '?')):
                summary += '.'  # Append a period if the summary doesn't end with punctuation
                
           
        st.success(f"Title: {article['title']}\n\nLink: {article['url']}\n\nSummary: {summary}")


# Streamlit app
st.set_page_config(page_title="Short News App", layout='centered', initial_sidebar_state='expanded')
st.title('Welcome to Short News App!')

# Define the columns layout
row1 = st.columns([4, 4, 4])

# Column for the expander and its contents

my_expander = st.expander(label='Expand me for searching news!')
with my_expander:
    row = st.columns(2)
    with row[0]:
        search = st.text_input('Search your favorite topic:')
    with row[1]:
        submitted = st.button("Submit")
        dissubmit = st.button("Compare")
        topic = st.button("Topic")
       

# Display news summaries

if submitted:
    try:
            # Get news by keyword
        news_by_keyword = google_news.get_news(search)
        generate_summary(news_by_keyword)
    except Exception as e:
        st.error(f"An error occurred: {e}")

if dissubmit:
    try: 
            # Get news by keyword
        news_by_keyword = google_news.get_news(search)
        generate_dissummary(news_by_keyword)
    except Exception as e:
        st.error(f"An error occurred: {e}")

if topic:
    try:
            # Get news by keyword
        news_by_topic = google_news.get_news_by_topic(search)

        generate_summary(news_by_topic)
    except Exception as e:
        st.error(f"An error occurred: {e}")

