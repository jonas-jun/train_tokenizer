from tokenizer_utils import build_tokenizer_wp
import argparse
import os

in_dir = 'tokenized'
out_dir = 'tokenizers'
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--infiles', '-IN', type=str, default='tkd_test_written.txt') # many files
    parser.add_argument('--vocab_size', '-V', type=int, default=12000)
    parser.add_argument('--freq', '-F', type=int, default=100)
    parser.add_argument('--alphabet', '-A', type=int, default=3000)
    parser.add_argument('--unused', '-U', type=int, default=100)
    parser.add_argument('--outfile', '-OUT', type=str, default='test')
    parser.add_argument('--initial', '-INIT', type=str, default='initial_alphabet.txt')
    args = parser.parse_args()

    infiles = list(map(lambda x: os.path.join(in_dir, x), args.infiles.split(',')))
    print('>> files in')
    print(infiles)
    
    initial_alphabet = False
    if args.initial:
        with open(args.initial, 'r', encoding='utf-8') as f:
            initial_alphabet = list(map(lambda x: x.strip(), f.readlines()))

    build_tokenizer_wp(files=infiles, vocab_size=args.vocab_size, min_freq=args.freq, limit_alphabet=args.alphabet,
                        initial_alphabet=initial_alphabet, num_unused=args.unused, name=args.outfile, dir=out_dir)

# for insert mode