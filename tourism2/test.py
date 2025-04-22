from backend.llm_interface import generate_sql_query_with_gpt

while True:
    question = input("Pose ta question (ou 'exit') : ")
    if question.lower() == 'exit':
        break
    sql = generate_sql_query_with_gpt(question)
    print("\nSQL généré :\n", sql)
