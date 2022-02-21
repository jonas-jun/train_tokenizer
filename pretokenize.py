# mecab tokenize
from tokenizer_utils import mecab_tokenize
import argparse
import os

in_dir = 'processed'
out_dir = 'tokenized'
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', '-IN', type=str, default='test_written.txt')
    parser.add_argument('--outfile', '-OUT', type=str, default='tkd_test_written.txt')
    args = parser.parse_args()
    
    inf = os.path.join(in_dir, args.infile)
    outf = os.path.join(out_dir, args.outfile)
    print('>> file in')
    print(inf)
    print('>> file out')
    print(outf)

    mecab_tokenize(infile=inf, outfile=outf)