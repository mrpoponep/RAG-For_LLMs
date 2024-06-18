<h1 align="center">Retrieval Augmented Generation (RAG) for LLMs</h3>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#architecture ">Architecture </a></li>
    <li><a href="#feature">Features</a></li>
    <li><a href="#deployed-application">Deployed Application</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
Welcome to the Insurance Question Answering System! This project leverages a Retrieval-Augmented Generation (RAG) model to provide accurate and comprehensive answers to insurance-related questions. The system integrates a powerful language model with a retrieval mechanism to enhance the quality and relevance of responses.


![plot](/Misc/Prj_screenshot.png)


<!-- GETTING STARTED -->
## Getting Started

How to run this project locally

### Prerequisites

Install milvus standalone: Follow instruction [here](https://milvus.io/docs/install_standalone-docker.md) to install and setup an milvus database.

### Installation

1. Get a free Google Gemini API key [here](https://ai.google.dev/).
2. Clone the repo
   ```sh
   git clone https://github.com/mrpoponep/RAG-For_LLMs
   ```
3. Install packages using pip.
   ```sh
    pip install -r requirement.txt
    ```
4. Create a local_settings.py file with your API key in it.
    ```sh
    API_KEY='abcdxyz'
    ```

### Usage
1. Start your milvus database and connect to it.
2. Prepare your own dataset as jsonl file ([Example](/Misc/Example_data.jsonl)).
3. Run main.ipynb file to upload your embeded data onto the database.
4. Test your RAG and LLM by running Test.ipynb file.\

### Architecture 
The system consists of the following components:


![plot](/Misc/RAG_diagram.png)

### Features
1. Real data used for trainning: Data used for retrieval are 21,325 answers for 12,889 common question gathered from this website [insurance library](https://www.insurancelibrary.com/).
2. Accurate Question Answering: Provides detailed and accurate answers to a wide range of insurance-related questions.
3. Retrieval-Augmented Generation: Combines retrieval of relevant documents with generation of answers for improved accuracy.

### Deployed Application
You can access the deployed version of this project [here](https://rag-for-llm.streamlit.app/).

Visit the link to try out the Insurance Question Answering System and see it in action!