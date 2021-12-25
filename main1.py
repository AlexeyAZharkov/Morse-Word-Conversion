morze_dic = {'A': '·−', 'B': '−···', 'C': '−·−·', 'D': '−··', 'E': '·', 'F': '··−·',
              'G': '−−·', 'H': '····', 'I': '··', 'J': '·−−−', 'K': '−·−', 'L': '·−··',
              'M': '−−', 'N': '−·', 'O': '−−−', 'P': '·−−·', 'Q': '−−·−', 'R': '·−·',
              'S': '···', 'T': '−', 'U': '··−',
              'V': '···−', 'W': '·−−', 'X': '−··−', 'Y': '−·−−', 'Z': '−−··'}

new_word = input("Enter the words: ").upper()
morze_word = ''
for letter in new_word:
    if letter == ' ':
        morze_word += '   '
    else:
        morze_word += morze_dic[letter] + ' '
print(morze_word)


