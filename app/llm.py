from app.prompt import prompt_template, question_categorize_prompt_template, conversation_prompt_template
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA, LLMChain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

DB_FAISS_PATH = 'vectorstore/db_faiss'
PROMPT=PromptTemplate(template=prompt_template, input_variables=["chat_history", "context", "question"])
CATEGORIZE_PROMPT=PromptTemplate(template=question_categorize_prompt_template, input_variables=["chat_history", "question"])
CONVERSATIONAL_PROMPT=PromptTemplate(template=conversation_prompt_template, input_variables=["chat_history", "question"])

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
llm = ChatGroq(
    groq_api_key='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',
    model_name='llama3-8b-8192'
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
qa_chain = ConversationalRetrievalChain.from_llm(llm=llm,
                                    chain_type='map_rerank',
                                    retriever=db.as_retriever(search_kwargs={'k': 3}), #k=3 specifies retrieving the top 3 results
                                    memory=memory,
                                    # combine_docs_chain_kwargs={'prompt': PROMPT},
                                    verbose=True
                                    )

# Chain for categorizing a user query into General Statement and Medical-Related question
cuq_chain = LLMChain(prompt=CATEGORIZE_PROMPT, llm=llm, verbose=True)

# Chain for answering based on the chat history only
conv_chain = LLMChain(prompt=CONVERSATIONAL_PROMPT, llm=llm, memory=memory, verbose=True)

def get_user_query_response(question, chat_history):
    cat = cuq_chain.run({'question': question, 'chat_history': chat_history})
    print(cat)
    if cat.strip() == 'medical':
        # print(qa_chain({'question': question, 'chat_history': chat_history}))
        return qa_chain({'question': question, 'chat_history': chat_history})['answer']
    elif cat.strip() == 'non-medical':
        # Skip answering non-medical questions
        return "I'm sorry, I can only assist with medical-related questions."
    else:
        # Handle unexpected output from categorization
        return "I'm not sure how to categorize your question. Please rephrase it or ask a medical-related query."
    # else:
    #     # print(conv_chain({'question': question, 'chat_history': chat_history}))
    #     return conv_chain({'question': question, 'chat_history': chat_history})['text']

# query = "What is type 2 diabetes?"
# response = qa_chain({'query': query})
# print(response)

# query = "What to do if I've CYSTIC FIBROSIS?"
# response = qa_chain({'query': query})
# print(response)