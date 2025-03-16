from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import re

def Baca_file(file_path):

    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line.strip()]

def stopword(stopword_file):

    try:
        with open(stopword_file, 'r', encoding='utf-8') as file:
            return set(line.strip().lower() for line in file if line.strip())
    except FileNotFoundError:
        print("File stopwords tidak ditemukan, menggunakan stopwords default saja.")
        return set()

def preprocess(text, extra_stopwords):


    stemmer = StemmerFactory().create_stemmer()
    stopword_factory = StopWordRemoverFactory()
    default_stopwords = set(stopword_factory.get_stop_words())
    all_stopwords = default_stopwords | extra_stopwords
    
    # Tokenisasi 
    tokens = re.findall(r'\b\w+\b', text.lower())
    
    # Filtering 
    filtered = [word for word in tokens if word not in all_stopwords]
    
    # Stemming
    stemmed = [stemmer.stem(word) for word in filtered]
    
    return tokens, filtered, stemmed

def proses_output(input_file, output_file, stopword_file):

    sentences = Baca_file(input_file)
    extra_stopwords = stopword(stopword_file)
    result = ""
    
    for idx, sentence in enumerate(sentences, start=1):
        tokens, filtered, stemmed_tokens = preprocess(sentence, extra_stopwords)
        
        result += f"""
        Doc {idx}:
        Isi Dokumen: {sentence}
        
        Hasil Tokenisasi:{' '.join(tokens)}
        
        Hasil Filtering:{' '.join(filtered)}
        
        Hasil Stemming: {' '.join(stemmed_tokens)}
        
        ================================================================================================================================================================================================================================================
        """
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(result)
    
    print(f'Proses selesai. Hasil disimpan di {output_file}')

if __name__ == "__main__":
    input = "input.txt"  
    output = "output.txt"
    stopword_tambahan = "stopwords_id_satya.txt" 
    proses_output(input, output, stopword_tambahan)
output
stopword_tambahan