def print_in_backward(sentence):
    sentence_splitted = sentence.split(' ')
    backward_sentence_splitted = []
    for i in range(1,len(sentence_splitted)+1):
        
        backward_sentence_splitted.append(sentence_splitted[-i])
    backward_sentence = ' '.join(backward_sentence_splitted)
    print(backward_sentence)
    return backward_sentence

sentence = input('write the sentence you want to print backwards\n')

print_in_backward(sentence)