import json

import jieba
import jieba.analyse
from tqdm import tqdm

from database import *


def main():
    all_text = []
    for i in db.session.query(zhihu_answer.content).all():
        all_text.append(i[0])
    for i in db.session.query(zhihu_article.title, zhihu_article.content).all():
        all_text.append(i[0])
        all_text.append(i[1])
    for i in db.session.query(zhihu_comment.content).all():
        all_text.append(i[0])
    for i in db.session.query(zhihu_question.title).all():
        all_text.append(i[0])

    all_text = set(all_text)

    jieba.load_userdict('./data/userdict.txt')
    jieba.analyse.set_stop_words('./data/stop_words.txt')

    res_dict = {}

    bar = tqdm(all_text)
    for text in bar:
        for word in jieba.analyse.extract_tags(text):
            res_dict[word] = res_dict.get(word, 0) + 1

        for word in jieba.analyse.textrank(text):
            res_dict[word] = res_dict.get(word, 0) + 1

    res_dict = {k: v for k, v in sorted(res_dict.items(), key=lambda item: item[1], reverse=True) if v >= 100}

    with open('./data/word_freq_textrank.json', 'w', encoding='utf-8') as f:
        json.dump(res_dict, f, ensure_ascii=False, indent=4)


def load_data():
    with open('./data/word_freq_textrank.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    insert = []
    for key, value in data.items():
        insert.append(word_freq(name=key, value=value))
    db.inserts(insert)


if __name__ == '__main__':
    db = Database('mysql+pymysql://root:20131114@localhost:3306/env?charset=utf8mb4')
    # main()
    db.create_all_table()
    load_data()
    pass
