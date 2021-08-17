class BitapSearch:
    '''
    fuzzy search by bitap algorithm

    usage:
        sentence = 'abcdefghijklmn'
        search_word = 'fghi'

        search = BitapSearch(sentence)
        search.find(search_word);
    '''

    def __init__(self, sentence):
        self.sentence = sentence
        self.sentence_chars = list(self.sentence)
        self.uniq_sentence_chars = list(set(self.sentence_chars))

    def find(self, search_word, distance = 1):
        search_chars = list(search_word)
        finish = 1 << len(search_chars) - 1

        # make mask
        mask = {}
        for c in self.uniq_sentence_chars:
            mask[c] = 0;
        for sc in search_chars:
            for m in mask.keys():
                mask[m] >>= 1
                if sc == m:
                    mask[m] |= finish

        state = [0] * (distance + 1)
        ret = [[]] * (distance + 1)
        for i,c in enumerate(self.sentence_chars):
            rstr_mask = 0
            for j in range(len(state)):
                next_mask = state[j]
                state[j] = (state[j] << 1 | 1)
                next_mask |= state[j]
                state[j] &= mask[c]
                state[j] |= rstr_mask
                next_mask |= state[j] << 1 | 1
                rstr_mask = next_mask
                if (state[j] & finish) == finish:
                    ret[j].append(i)
        return ret

