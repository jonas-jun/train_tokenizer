# Tokenizer Trainer
the program to train Korean WordPiece tokenizers with Mecab and BertTokenizer(HF)

# How to use?
1. pre-tokenize with Mecab (KoNLPy)
    - 코스트코에서 늘 사서 쓰던 제품이에요
    - 코스트코 에서 늘 사 서 쓰 던 제품 이 에요
    python3 pretokenize.py -IN test_written.txt -OUT tkd_test_written.txt

2. train WordPiece tokenizer with BertTokenizer (huggingface transformer)
@arguements
- files: files to train, ['aaa.txt', 'bbb.txt']
- vocab_size: number of words in vocab
- min_freq: contain words whose frequency is over min_freq
- limit_alphabet: ㄱ, ㄴ, ㄷ, ㄹㄱ, chinese, ... number of alphabets
- num_unused: the number of [unused00]
- name: {name}_{vocab size}_freq{min freq}_limit{limit alphabet}.txt
- dir: directory to save

# Result
tokenizer_28323.txt  
- news, kowiki, written, reviews