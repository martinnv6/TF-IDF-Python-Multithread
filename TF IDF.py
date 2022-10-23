if __name__ == '__main__':
    # import multiprocessing
    # print(multiprocessing.cpu_count())
    from MultiprocessingMapReduce import SimpleMapReduce
    from MultiprocessingWordCount import *


    import operator
    import glob
    # import os

    # os.chdir('c:/mydir')
    # input_files = glob.glob('C:/Users/martin_navarrete/Downloads/DcoumentosTarea2/Docs1/*.txt')
    input_files = glob.glob('C:/Users/martin_navarrete/OneDrive - Dell Technologies/Documents/Maestria/Tetra 3/3. Datos Masivos/Tarea 2/*.txt')

    mapper = SimpleMapReduce(file_to_words, count_words)
    word_counts = mapper(input_files)
    word_counts.sort(key=operator.itemgetter(1))
    word_counts.reverse()

    print('\nTOP 20 WORDS BY FREQUENCY\n')
    # top20 = word_counts[:20]
    # longest = max(len(word) for word, count in top20)
    # for word, count in top20:
    #     print('{word:<{len}}: {count:5}'.format(
    #         len=longest + 1,
    #         word=word,
    #         count=count)
    #     )
    for word, count in word_counts:
            
            print('{word:<{len}}: {count:5}'.format(
                len=len(word) + 1,
                word=word,
                count=count)
            )