Standard = """
##Task
You are an expert in the English Language. Your task is to paraphrase a piece of text that I will provide you in
the Input section delimited between triple backticks. You should change up the words, the sentence structure, 
add or remove figurative language, and change anything necessary in order to paraphrase the text. However, it is 
extremely important you do not change the original meaning and significance of the text.

In regard to the style you should use when paraphrasing keep it simple and straight to the point don't expand or
shorten the text keep it the same length and make sure you dont use any complex vocabulary. Plus, use the same
style used in the input text and the same level of formality in the use of words.

Keep in mind that there are some words or sentences that shouldnt be changed because they are the name of something
being explained in the piece of text. For example, if a text is talking about how to identify spam comments the word
"spam comments" shouldnt be paraphrased because otherwise the reader wouldnt understand what we're talking about.
So make sure to read thoroughly the input text understand what its about to identify the key parts which should be 
paraphrased.

##Input
Text: ```{input}```

##Output
The output should only be the paraphrased new text and nothing else.
"""

Academic = """
##Task
You are an expert in the English Language. Your task is to paraphrase a piece of text to make it more academic
worthy. I'll provide you with the text in the Input section delimited between triple backticks. You should change 
up the words, the sentence structure, add or remove figurative language, and change anything necessary in order 
to make the text more academic. However, it is extremely important you do not change the original meaning and 
significance of the text.

In regard to the style you should use when paraphrasing, it should be turned into an academic piece of text which
has the following characteristics:
- Clearly and accurately convey information and meaning.
- Focus on the information rather than personal feelings or opinions.
- Use a formal tone and avoid slang.
- Use complex sentence structures and advanced vocabulary. Not too much though.
- Clearly define the relationship between ideas and arguments. So, improve the structure as necessary.

Keep in mind that there are some words or sentences that shouldnt be changed because they are the name of something
being explained in the piece of text. For example, if a text is talking about how to identify spam comments the word
"spam comments" shouldnt be paraphrased because otherwise the reader wouldnt understand what we're talking about.
So make sure to read thoroughly the input text understand what its about to identify the key parts which should be 
paraphrased.

##Input
Text: ```{input}```

##Output
The output should only be the paraphrased new text and nothing else.
"""

Kiddie = """
##Task
You are an expert in the English Language. Your task is to paraphrase a piece of text to make it more for kids.
I'll provide you with the text in the Input section delimited between triple backticks. You should change 
up the words, the sentence structure, add or remove figurative language, and change anything necessary in order 
to make the easier and more fun for kids to read. However, it is extremely important you do not change the 
original meaning and significance of the text.

In regard to the style you should use when paraphrasing, here are some characteristics of a kiddie text:
- Use basic, commonly understood words to ensure clarity for young readers.
- Keep sentences short, brief, and straightforward.
- Use the active voice to make the text more engaging.
- Focus on concrete rather than abstract ideas, as children grasp tangible concepts more readily.
- Include vivid descriptions that help children visualize the content.
- Maintain a cheerful and positive tone to make the reading experience enjoyable.
- Employ repetition of words and phrases.
- Incorporate questions or direct addresses to the reader to make the text interactive.
- Provide definitions within the text for any complex terms that are necessary to include.

Keep in mind that there are some words or sentences that shouldnt be changed because they are the name of something
being explained in the piece of text. For example, if a text is explaining what quantum physics is, you should write
this term and next to it simply explain it in kid language using maximum a sentence. So make sure to read 
thoroughly the input text understand what its about to identify the key parts which should be paraphrased.

##Input
Text: ```{input}```

##Output
The output should only be the paraphrased new text and nothing else.
"""

Formal = """
##Task
You are an expert in the English Language. Your task is to paraphrase a piece of text to make it more fromal
worthy. I'll provide you with the text in the Input section delimited between triple backticks. You should change 
up the words, the sentence structure, add or remove figurative language, and change anything necessary in order 
to make the text more formal. However, it is extremely important you do not change the original meaning and 
significance of the text.

In regard to the style you should use when paraphrasing, it should be turned into a formal piece of text which
has the following characteristics:
- Use specific and accurate words to clearly express ideas.
- Use compound and complex sentences.
- Favor third person pronouns (he, she, it, they) over first (I, we) or second (you) person.
- Utilize the passive voice where appropriate to focus on the action.
- Maintain a neutral tone throughout the text.
- Write out full words instead of contractions (e.g., "do not" instead of "don't"). And don't use slang.
- Ensure consistency in terms of formatting, punctuation, and referencing styles.

Keep in mind that there are some words or sentences that shouldnt be changed because they are the name of something
being explained in the piece of text. For example, if a text is talking about how to identify spam comments the word
"spam comments" shouldnt be paraphrased because otherwise the reader wouldnt understand what we're talking about.
So make sure to read thoroughly the input text understand what its about to identify the key parts which should be 
paraphrased.

##Input
Text: ```{input}```

##Output
The output should only be the paraphrased new text and nothing else.
"""

Expand = """
##Task
You are an expert in the English Language. Your task is to expand and paraphrase a piece of text that I will 
provide you in the Input section delimited between triple backticks. You should change up some words, the sentence 
structure, add figurative language, and most importantly expand the piece of text and make it longer. However, 
it is extremely important you do not change the original meaning and significance of the text.

In regard to the style you should use when expanding the text, keep it simple and straight to the point and make sure you 
dont use any complex vocabulary. Plus, use the same style used in the input text and the same level of formality 
in the use of words.

Keep in mind that there are some words or sentences that shouldnt be changed because they are the name of something
being explained in the piece of text. For example, if a text is talking about how to identify spam comments the word
"spam comments" shouldnt be paraphrased because otherwise the reader wouldnt understand what we're talking about.
So make sure to read thoroughly the input text understand what its about to identify the key parts which should be 
paraphrased.

And, finally dont forget that the main purpose is to expand the piece of text, and while expanding you paraphrase
some words and phrases

##Input
Text: ```{input}```

##Output
The output should only be the paraphrased new text and nothing else.
"""

Shorten = """
##Task
You are an expert in the English Language. Your task is to shorten paraphrase a piece of text that I will provide 
you in the Input section delimited between triple backticks. You should change up the words, the sentence structure, 
add or remove figurative language, and most importantly shorten the piece of text by removing some unnessary
words or phrases. However, it is extremely important you do not change the original meaning and keep the idea that
the text is trying to convey intact.

In regard to the style you should use when shortening the text, keep it simple and straight to the point and make sure you 
dont use any complex vocabulary. Plus, use the same style used in the input text and the same level of formality 
in the use of words.

Keep in mind that there are some words or sentences that shouldnt be changed because they are the name of something
being explained in the piece of text. For example, if a text is talking about how to identify spam comments the word
"spam comments" shouldnt be paraphrased because otherwise the reader wouldnt understand what we're talking about.
So make sure to read thoroughly the input text understand what its about to identify the key parts which should be 
paraphrased.

And, finally dont forget that the main purpose is to shorten the piece of text, and while expanding you paraphrase
some words and phrases

##Input
Text: ```{input}```

##Output
The output should only be the paraphrased new text and nothing else.
"""

Creative = """
##Task
You are an expert in the English Language. Your task is to paraphrase a piece of text to make it more creative.
I'll provide you with the text in the Input section delimited between triple backticks. You should change 
up the words, the sentence structure, use a lot of figurative language, and change anything necessary in order 
to make its content more creative. However, it is extremely important you do not change the original meaning 
and significance of the text.

In regard to the style you should use when paraphrasing, here are some characteristics of a creative text:
- Use vivid, sensory language to paint mental pictures.
- Incorporate metaphors and similes specifically to draw interesting connections.
- Unique word choices and varied sentence structures.
- Integrate rhythmic elements like alliteration and assonance.
- Employ a distinctive voice that stands out.
- Use of humor or irony when necessary.
- Doesn't contain a lot of complex vocabulary

Keep in mind that there are some words or sentences that shouldnt be changed because they are the name of something
being explained in the piece of text. For example, if a text is explaining what quantum physics is, you should write
this term and next to it simply explain it in kid language using maximum a sentence. So make sure to read 
thoroughly the input text understand what its about to identify the key parts which should be paraphrased.

##Input
Text: ```{input}```

##Output
The output should only be the paraphrased new text and nothing else.
"""