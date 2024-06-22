def process_data(data):
    output=""
    for item in data:
        question = item[0][0].strip()
        answer = item[0][1].strip()
        answer = answer.replace('-LRB- ', '(')
        answer = answer.replace(' -RRB-', ')')
        answer = answer.replace('``', " '' ")
        output+=f"Q: {question}\n\n"
        output+=f"A: {answer}\n\n"
    return output

def create_prompt(document, question):
    PROMPT = f"""
Task: Your are a Insurance assistance, your job is based on a conversation of a costumer and a insurance expert, 
answer insurance-related questions accurately and provide detailed  explanation.
Instructions:

Read the context carefully.

Generate questions that seek information or clarification about the document's content.

Ensure that the questions are grammatically correct and understandable.

If the user talk to you casually, you can rely back

If the question is blank, tell the user to type the question in.

If the question is not related to the context or there is no answer in the context, tell the users the question is not related to insurance or there is no answer in your database

Context:

{document}

Question:

{question}

"""
    return PROMPT

if __name__ == '__main__':
    data='''Question: How Soon Do You Need To Get Different Auto Insurance After You Move To Another State?
Answer: The most common time to get new insurance is 30 days . There may be some flexibility however before you can register your auto in the new state you will need to establish your new insurance policy . Also going to long could get you fine should you happen to encounter an officer who is not in a generous mood .'''

    print(create_prompt(data))
