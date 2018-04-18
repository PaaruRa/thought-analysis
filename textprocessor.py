#!/usr/bin/env python3


import re

def reduce_whitespaces(text):
    return re.sub(r"[\s\n]+", " ", text)

def remove_punctuations(text):
    text = re.sub(r"[()-_:;!,]+", "", text)
    return re.sub(u'[—]+', '', text)

def process_text(text):
    text = text.lower()
    text = reduce_whitespaces(text)
    text = remove_punctuations(text)
    return text

def remove_urls(text):
    pass

def process_documents(documents):
    return list(map(process_text, documents))

def remove_stopwords(tokens, stopwords):
    res = []
    for token in tokens:
        if not token in stopwords:
            res.append(token)
    return res


def main():
    documents = ["hello! world. how are you?", "i am nishan"]
    # print(process_documents(documents))
    remove_stoprwords(['i', 'am'])

if __name__ == "__main__":
    main()
