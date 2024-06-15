def process_data(data):
    output=""
    for item in data:
        question = item[0][0].strip()
        answer = item[0][1].strip()
        output+=f"Q: {question}\n"
        output+=f"A: {answer}\n\n"
    return output

def create_prompt(document, question):
    PROMPT = f"""
Task:Based on the QA styled context provided, answer insurance-related questions accurately and provide some short explanation.
Instructions:
Read the document carefully.
Consider key points, concepts, and details within the document.
Generate questions that seek information or clarification about the document's content.
Ensure that the questions are grammatically correct and understandable.
Give the answer directly, do not repeat the question or add any unrelated text
If the question is not related to the context or there is no answer in the context, return None and do not answer any thing else
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
