def merge_questions_answers(question_file, answer_file, output_file):
    
    with open(question_file, 'r') as qf:
        questions = {line.split('. ')[0]: line.strip() for line in qf if line.strip()}
    
    with open(answer_file, 'r') as af:
        answers = {line.split('. ')[0]: line.split('. ')[1].strip() for line in af if line.strip()}
    
    with open(output_file, 'w') as of:
        for key in sorted(questions.keys()):
            question = questions.get(key, "")
            answer = answers.get(key, "Answer not found")
            of.write(f"{question}\n{answer}\n\n")

question_file ="QuesAns/questions.txt"
answer_file = "QuesAns/answers.txt"
output_file = "QuesAns/output.txt"

merge_questions_answers(question_file, answer_file, output_file)