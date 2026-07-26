# Filtering and cleaning data using loops and list methods

raw_inputs = ["  valid prompt  ", "", "another good response", "   ", "error: model timed out"]
cleaned_prompts = []

for item in raw_inputs:
    trimmed = item.strip()
    # Filter out blank inputs or error logs
    if trimmed and not trimmed.startswith("error:"):
        cleaned_prompts.append(trimmed)

print("Cleaned Dataset:")
for idx, prompt in enumerate(cleaned_prompts, 1):
    print(f"{idx}. {prompt}")
