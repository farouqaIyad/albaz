import json
import unicodedata
import re
import string

def contains_english(text):
    return bool(re.search(r"[A-Za-z]", text))


def load_mapping(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        mapping = json.load(file)
    return mapping


table_of_words = load_mapping(
    r"C:\Users\farouq\Desktop\projects\freelance project\table_of_words.json"
)
table_of_two_chars = load_mapping(
    r"C:\Users\farouq\Desktop\projects\freelance project\two_chars.json"
)
tanween_final_codes = load_mapping(
    r"C:\Users\farouq\Desktop\projects\freelance project\tanween_final.json"
)

tanween_list = [1614, 1615, 1616, 1617, 1611, 1612, 1613]
shadda_uni_code = 1617


def split_words_with_last_indicator(text):
    normalized_text = unicodedata.normalize("NFC", text)

    words = normalized_text.split()

    if not words:
        return []

    result = [
        (word, "last" if i == len(words) - 1 else "other")
        for i, word in enumerate(words)
    ]

    return result


def in_tanween_list(output, word, char, i, mapping, b):

    char_uni_code = ord(char)
    if i + 1 < len(word) and ord(word[i + 1]) == shadda_uni_code:
        output.append(output[-1])
        b = False

    if char_uni_code == shadda_uni_code and b:
        output.append(output[-1])

    if char_uni_code != shadda_uni_code:
        if (
            i == len(word) - 1
            or (i == len(word) - 2 and ord(word[-1])) == shadda_uni_code
        ):
            output.append(tanween_final_codes.get(str(char_uni_code), char))

        else:
            output.append(mapping.get(str(char_uni_code), char))

    return output, b


def shamsi_and_qamari(word):
    if word.startswith("ال"):
        if ord(word[2]) == 1618:
            if word[3] in "ابغ حجك وخف عقيمه":
                word = "\u2090l" + word[3:]
            else:
                word = "\u2090" + word[3:]
        if word[2] in "ابغ حجك وخف عقيمه":
            word = "\u2090l" + word[2:]
        else:
            word = "\u2090" + word[2:]

    return word


def skipables(word):
    """Replace two-character sequences based on the table."""
    for key, replacement in table_of_two_chars.items():
        word = re.sub(re.escape(key), replacement, word)
    return word


def iterate_over_single_word(word, mapping, indicator):
    output = []
    b = True
    
    for i, char in enumerate(word):
        char_uni_code = ord(char)
        print(f"Character: {char}, Unicode: {char_uni_code}")

        if char_uni_code in tanween_list:
            output, b = in_tanween_list(output, word, char, i, mapping, b)
            continue

        mapped_value = mapping.get(char, char)

        if isinstance(mapped_value, dict):
            output.append(mapped_value.get(indicator, char))
            continue
        elif char_uni_code == 1618:
            continue
        else:
            if char == "ي" and ord(word[i - 1]) == 1616:
                output.append("e")
                continue
            elif  char == "و" and ord(word[i - 1]) == 1615:
                output.append("o")
                continue

        output.append(mapped_value)

    return output


def iterate_over_words(words, mapping):
    all_output = []

    for word, indicator in words:
        if word not in table_of_words:
            word = shamsi_and_qamari(word)
            word = skipables(word)
            output = iterate_over_single_word(word, mapping, indicator)
            str_output = "".join(output)
            str_output = str_output.replace("eee","eyy")
            str_output = string.capwords(str_output)
            output = str.split(str_output)
            all_output.append("".join(output) + " ")
        else:
            all_output.append(table_of_words.get(word, word))
            
    return all_output


def transcribe_arabic_to_english(text, mapping):
    # Split the input text by lines to preserve new lines
    lines = text.splitlines()
    transcribed_lines = []
    
    for line in lines:
        words = split_words_with_last_indicator(line)
        transcribed_line = iterate_over_words(words, mapping)
        
        for i in range(len(transcribed_line)-1):
            if transcribed_line[i].endswith("\u207f ") and transcribed_line[i+1].startswith("\u2090"):
                transcribed_line[i] = transcribed_line[i].replace("\u207f","\u207f\u1d49")
        transcribed_lines.append("".join(transcribed_line))
    
    # Join the transcribed lines with new line characters
    return "\n".join(transcribed_lines)

