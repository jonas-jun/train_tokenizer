from konlpy.tag import Mecab
import os, json
from tokenizers import Tokenizer
from tokenizers.models import WordPiece
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.trainers import WordPieceTrainer
from tokenizers.processors import TemplateProcessing
from tokenizers.normalizers import BertNormalizer
from typing import List

def mecab_tokenize(infile='test.txt', outfile='tokenized_mecab.txt', check_by=1000000):
    m = Mecab()
    i = 0
    print('Start to tokenize {}'.format(infile))
    fout = open(outfile, 'w', encoding='utf-8')
    with open(infile, 'r', encoding='utf-8') as fin:
        for line in fin:
            try:
                line = ' '.join(m.morphs(line))
            except: continue
            fout.write(line+'\n')
            i += 1
            if i%check_by == 0:
                print('{:,} tokenized'.format(i))
    fout.close()
    print('Finish tokenizing by Mecab')

def build_tokenizer_wp(files: List[str]=None, vocab_size=12000, min_freq=100, limit_alphabet=3000, num_unused=100,
                        initial_alphabet=False, get_text=True, name='mix', dir='tokenizers'):
    tokenizer = Tokenizer(WordPiece())
    tokenizer.pre_tokenizer = Whitespace()
    # tokenizer.normalizer = normalizers.Sequence([NFD(), StripAccents()])
    tokenizer.normalizer = BertNormalizer(strip_accents=False, lowercase=False)
    tokenizer.post_processor = TemplateProcessing(single='[CLS] $A [SEP]',
                                                    pair='[CLS] $A [SEP] $B:1 [SEP]:1',
                                                    special_tokens=[('[CLS]',1), ('[SEP]',2)])
    special_tokens = ['[PAD]', '[CLS]', '[SEP]', '[UNK]', '[MASK]']
    unused_tokens = ['[unused{:02d}]'.format(i) for i in range(1, num_unused+1)]
    special_tokens += unused_tokens
    if not initial_alphabet: initial_alphabet = list()
    trainer = WordPieceTrainer(vocab_size=vocab_size,
                            min_frequency=min_freq,
                            limit_alphabet=limit_alphabet,
                            initial_alphabet=initial_alphabet,
                            special_tokens=special_tokens)
    print('Start to train tokenizer, vocab_size={:,} | min_freq={:,}'.format(vocab_size, min_freq))
    tokenizer.train(files, trainer)
    print('Finish tokenizing')
    f_json = '{}_{}_freq{}_limit{}.json'.format(name, vocab_size, min_freq, limit_alphabet)
    f_json = os.path.join(dir, f_json)
    tokenizer.save(f_json)
    print('Vocab file exported: {}'.format(f_json))

    if get_text:
        f_text = '{}_{}_freq{}_limit{}.txt'.format(name, vocab_size, min_freq, limit_alphabet)
        f_text = os.path.join(dir, f_text)
        json_to_txt(f_json, f_text)
        print('Vocab txt file exported: {}'.format(f_text))

def json_to_txt(json_path, txt_path):
    f = open(txt_path, 'w')
    with open(json_path, 'r') as json_file:
        json_data = json.load(json_file)
        for item in json_data['model']['vocab']:
            f.write(item+'\n')
    f.close()


    



