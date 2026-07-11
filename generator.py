def generate_question_paper(context):
    prompt = f"""
You are an expert question paper setter.

Based on the following study material, generate a professional question paper.

Study Material:
{context}

Question Paper Format:

Section A (5 MCQs)
Section B (5 Short Answer Questions)
Section C (3 Long Answer Questions)

Also provide the answer key for MCQs.
"""

    return prompt
