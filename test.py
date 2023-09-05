# Define the input and output file names
input_file_name = "file_to_read.txt"
output_file_name = "result.txt"

# Read the input file
with open(input_file_name, "r") as input_file:
    text = input_file.read()

# Split the text into words and initialize counters
words = text.split()
terrible_count = 0

# Process each word
for i, word in enumerate(words):
    if word.lower() == "terrible":
        terrible_count += 1
        if terrible_count % 2 == 0:  # Even occurrence
            words[i] = "pathetic"
        else:  # Odd occurrence
            words[i] = "marvellous"

# Join the modified words back into a text
modified_text = " ".join(words)

# Write the modified text to the output file
with open(output_file_name, "w") as output_file:
    output_file.write(modified_text)

# Display the total count of "terrible"
print("Total occurrences of 'terrible':", terrible_count)
