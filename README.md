# Building a Medical Chatbot Powered by Large Language Model

## Quickstart

### Create an environment

```bash
python -m venv <venv>
```

### Activate the virtual environment.

For Windows
```bash
<venv>\Scripts\activate.bat
```

For MacOS and Linux
```bash
source <venv>/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the flask application
For Windows
```bash
export FLASK_APP=app/run.py
export FLASK_ENV=development
flask run
```

For MacOS and Linux
```bash
set FLASK_APP=app/run.py
set FLASK_ENV=development
flask run
```
---
# Building a Medical Chatbot Powered by Large Language Model
## **Abstract**
The Medical Chatbot leverages state-of-the-art AI technologies, including LLaMA3, Retrieval-Augmented Generation (RAG), and LangChain, to provide accurate and empathetic responses to a wide range of health-related queries. Built with a Flask-based backend and a vectorized retrieval system using FAISS, the chatbot integrates real-time information retrieval with large-scale language understanding to serve as an educational tool for patients, caregivers, and healthcare professionals. Evaluation focuses on accuracy, relevance, and latency metrics.

---
## **Table of Contents**

1. **Introduction**
    - 2.1 Background
    - 2.2 Objectives
    - 2.3 Scope
2. **Literature Review**
    - 3.1 Existing Healthcare Chatbots
    - 3.2 Limitations of Current Approaches
    - 3.3 Impact of LLaMA on Healthcare Chatbots
3. **Methodology**
    - 4.1 Data Collection and Preparation
    - 4.2 Model Fine-Tuning
    - 4.3 RAG Pipeline Integration
    - 4.4 Backend Development
    - 4.5 Software Dependencies
4. **Implementation**
    - 5.1 Architecture Overview
    - 5.2 Technologies Used
5. **Results and Analysis**
    - 6.1 Accuracy & Relevance Metric
    - 6.2 Latency Metric
6. **Discussion**
    - 7.1 Significance
    - 7.2 Limitations
7. **Conclusion**
    - 8.1 Future Scope
8. **References**

---

## **Introduction**

### **2.1 Background**
Managing chronic diseases requires consistent education, symptom monitoring, and lifestyle adjustments. Healthcare systems often face challenges in offering instant, personalized guidance on health concerns. Patients and caregivers rely heavily on online resources, which may lack reliability or comprehensiveness. AI-powered medical chatbots are emerging as transformative tools for providing reliable health-related information and support.

### **2.2 Objectives**
- Develop a scalable chatbot capable of handling diverse health-related queries.
- Integrate retrieval and LLMs for real-time, accurate responses.
- Evaluate system performance on key metrics, ensuring reliability.

### **2.3 Scope**
The chatbot serves as:
- An interactive assistant for patients and caregivers.
- A quick reference for healthcare professionals.
- A scalable solution with potential extensions for additional medical domains.

---

## **Literature Review**

### **3.1 Existing Healthcare Chatbots**
Healthcare chatbots provide real-time assistance but face limitations such as:
- Lack of contextual understanding.
- Dependence on static datasets.
- Narrow scope focused on specific domains.

### **3.2 Limitations of Current Approaches**
- Limited dynamic retrieval.
- Generalized language models not fine-tuned for healthcare.
- Poor user interaction quality.

### **3.3 Impact of LLaMA on Healthcare Chatbots**
- Fine-tuning for domain-specific expertise.
- Empathy in responses for a better user experience.
- Scalability and efficiency in real-world applications.

---

## **Methodology**

### **4.1 Data Collection and Preparation**
- **Data Source**: Medical text data from the "Gale Encyclopedia of Medicine."
- **Text Splitting**: Recursive splitting into manageable chunks with contextual overlap.
- **Embedding**: Semantic vectorization using `sentence-transformers/all-MiniLM-L6-v2`.
- **Retrieval System**: FAISS for efficient semantic search.

### **4.2 Model Fine-Tuning**
Fine-tuning was simulated using advanced prompt engineering to enhance domain-specific accuracy without modifying hosted model parameters.

### **4.3 RAG Pipeline Integration**
- Combines retrieval (FAISS) and generation (LLaMA3) to generate accurate, contextually relevant responses.
- Reduces hallucinations and enhances response reliability.

### **4.4 Backend Development**
- **Framework**: Flask for scalable API management.
- **Integration**: RAG pipeline for dynamic retrieval and generation.
- **Memory Management**: Multi-turn chat history using conversation buffer memory.

### **4.5 Software Dependencies**
- **Backend**: Flask, SQLAlchemy, Flask-JWT-Extended.
- **Retrieval**: FAISS, Sentence-Transformers.
- **LLM**: ChatGroq API for LLaMA3.

---

## **Implementation**

### **5.1 Architecture Overview**
- **User Interface**: Frontend for user interaction.
- **Backend**: Flask API managing retrieval and generation.
- **Retrieval**: FAISS vector store for semantic search.
- **LLM**: LLaMA3 via ChatGroq API for response generation.
- **Memory**: Conversation buffer for context retention.

### **5.2 Technologies Used**
- **Retrieval**: FAISS and Sentence-Transformers.
- **Backend**: Flask, Flask-SQLAlchemy, Flask-JWT-Extended.
- **LLM**: ChatGroq API for LLaMA3 integration.

---

## **Results and Analysis**

### **6.1 Accuracy & Relevance Metric**
- **Score**: 68.33%
- **Evaluation Framework**:
  - Scoring based on factual accuracy, relevance, and completeness.
  - Dataset of 20 queries with reference answers and chatbot responses.

### **6.2 Latency Metric**
- **Average Latency**: 2.33 seconds.
- **Key Insights**:
  - Minimal latency for simple queries.
  - Higher latency for detailed responses.

---

## **Discussion**

### **7.1 Significance**
- Enhanced accessibility for medical information.
- Scalable architecture for diverse medical domains.
- Empowers users with reliable and accurate health knowledge.

### **7.2 Limitations**
- Latency variations for complex queries.
- Accuracy challenges for ambiguous topics.
- Limited to English queries, requiring multilingual support.

---

## **Conclusion**

### **8.1 Future Scope**
- **Multilingual Support**: Extend accessibility for non-English users.
- **Domain-Specific Fine-Tuning**: Improve understanding of complex medical terms.
- **IoT Integration**: Real-time health monitoring with wearable devices.
- **Latency Optimization**: Faster response times with model and retrieval enhancements.

---

## **References**
1. [LangChain Documentation](https://langchain.readthedocs.io)
2. [FAISS Documentation](https://faiss.ai)
3. [Hugging Face Transformers](https://huggingface.co/docs/transformers)