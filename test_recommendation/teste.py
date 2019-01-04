import pickle as p

if __name__ == "__main__":
    with open('my_dumped_classifier.pkl', 'rb') as fid:
        gnb_loaded = p.load(fid)
    while True:
        STRING_INPUT_USUARIO = input("Digite a descricao: ")
        if (STRING_INPUT_USUARIO == 'exit'):
            break
        svm_predictions = gnb_loaded.predict([STRING_INPUT_USUARIO])
        print(svm_predictions)