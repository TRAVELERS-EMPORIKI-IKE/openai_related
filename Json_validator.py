import json

# Define the validation function
def validate_jsonl_object(json_obj):
    if "prompt" not in json_obj or "completion" not in json_obj:
        return False
    return True

# Open the JSONL file for reading
with open("your_file.jsonl", "r") as f:
    for line in f:
        json_obj = json.loads(line.strip())
        
        # Validate the JSON object
        if not validate_jsonl_object(json_obj):
            print(f"Validation failed for object: {json_obj}")

# If the script finishes without printing anything, validation passed for all objects
