# A script demonstrating functions, dictionaries, and error handling

def evaluate_model_score(scores_dict):
    """Calculates average evaluation score from a dictionary of criteria."""
    total = sum(scores_dict.values())
    count = len(scores_dict)
    average = total / count
    return average

# Example dataset
rubric_scores = {
    "accuracy": 5,
    "logic_reasoning": 4,
    "instruction_following": 5,
    "formatting": 4
}

avg = evaluate_model_score(rubric_scores)
print(f"Evaluation Complete. Average Score: {avg:.2f}/5.00")
