# News Summarization with perspective by Vertex AI

This repository contains a python code that demonstrates how to fetch the latest news articles and summarize them using Large Language Models (LLM) from Vertex AI. By the using of LLM, it can summarize news from the articles with meaningful and concise information.

## Overview

A detailed tutorial on using APIs to retrieve news stories from reputable sources and using LLM to create summaries may be found in the code `app.py`.

This project uses various types of technology and tool to create a structured online news summarization system. Below are keys components in the project:

- LangChain Agents: Making use of LangChain Agents' features to help components communicate and coordinate more effectively.
- Vertex AI: We use vertex ai to import large language model called text-bison which can maximize the utility on generating summaries.
- Prompt-Engineering: Maximizing the input prompts and raising the standard of the summaries that are produced by using prompt engineering techniques.
- Google News API: Using API from google news to obtain various articles and topics for summarizing.
- Python: Implementing the entire system using the Python programming language, enabling flexibility, ease of use, and a vast ecosystem of libraries and tools.
- Streamlit: Streamlit allow us to create a great user-friendly interface with powerful meaning.

## Prerequisites

To run the application, you need the following dependencies:

- Python 3.10
- Jupyter Notebook
- GNews
- Streamlit
- Langchain

## Getting Started

1. Clone this repository to your local machine.
   ```
   git clone https://github.com/dgNathiRocha/AI2-group14-NewsSummary.git
   ```
3. Launch any code environment and open the `app.py` python code.
4. Run below command on the terminal
 ```
   streamlit run app.py
   ```

## Improvement need

Right now the model still cannot summarize all the contents from the news articles due to permission access and input tokens limitation.


## Acknowledgments

We would like to thank the contributors and developers of the libraries and tools used in this project. Also thanks to [google news project by KillerStrike17 Shubham Agnihotri](https://github.com/mchoirul/genai-code/blob/main/notebook/googlenews_summarize_vertex_langchain-git.ipynb?source=post_page-----a0a3b513cdb5--------------------------------)for providing useful information and techniques on creating news summarizer.