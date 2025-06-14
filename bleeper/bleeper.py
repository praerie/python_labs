# Write an automated censor program that reads in the text from a file
# and creates a new file where all of the four-letter words have been replaced by "****". 
# You can ignore punctuation, and you may assume that no words in the file
# are split across multiple lines.

def censor_four_letter_words(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()  # Read lines while preserving line breaks

    censored_lines = []

    for line in lines:
        censored_words = []

        for word in line.split():
            # Extract any leading punctuation
            leading_punct = ""
            while word and not word[0].isalnum():  # isalnum: True if alpha-numeric string, False otherwise
                leading_punct += word[0]
                word = word[1:]

            # Extract any trailing punctuation
            trailing_punct = ""
            while word and not word[-1].isalnum():
                trailing_punct = word[-1] + trailing_punct
                word = word[:-1]

            # Handle words in quotation marks and keep contractions intact
            has_quotes = word.startswith(("'", '"')) and word.endswith(("'", '"')) and len(word) > 2
            if has_quotes:
                word = word[1:-1]

            # Split hyphenated words and check each part
            parts = word.split('-')
            censored_parts = []

            for part in parts:
                # Remove contractions (don't > dont) before checking length of word 
                clean_part = part.replace("'", "")

                # Censor only if the alphabetic part of the word is exactly four letters long
                if len(clean_part) == 4 and clean_part.isalpha():
                    censored_parts.append("****")
                else:
                    censored_parts.append(part)

            # Reassemble word with its original punctuation
            censored_word = "-".join(censored_parts)
            if has_quotes:
                censored_word = '"' + censored_word + '"'

            censored_words.append(leading_punct + censored_word + trailing_punct)

        # Reconstruct the line while maintaining its original structure
        censored_lines.append(" ".join(censored_words))

    # Preserve original line breaks in the output file
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        outfile.write("\n".join(censored_lines))


input_file = 'bleeper/test-input.txt'
output_file = 'bleeper/censored_output.txt'
censor_four_letter_words(input_file, output_file)
print(f'Censored file saved as {output_file}')