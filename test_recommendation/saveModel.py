from sklearn.linear_model import SGDClassifier
import pickle as p
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import (TfidfTransformer, CountVectorizer)
from sklearn.model_selection import GridSearchCV
from stop_words import get_stop_words

biologia = [
    "A vida, em relação às células, é estudada pela biologia celular, biologia molecular, bioquímica e genética molecular.",
    "Biologia é a ciência que estuda a vida e os organismos vivos.",
    "O termo 'biologia' significa basicamente 'estudo da vida'.",
    "Os 5 reinos dos seres vivos: reino monera, reino protista ou protoctista, reino Fungi, reino Plantae e reino Animalia",
    "A biologia é atualmente dividida em várias subdivisões, ramos, ou subdisciplinas, todas voltadas ao estudo das particularidades da ciência.",
    "Elas são conhecidas no meio acadêmico por ciências biológicas.",
    "A biologia tornou-se um campo de investigação tão vasto que geralmente não é estudada como uma única disciplina, mas antes dividida em várias disciplinas subordinadas;",
    "A fisiologia estuda os processos mecânicos, físicos e bioquímicos dos organismos vivos, tentando compreender como as várias estruturas funcionam como um todo.",
    "A biologia evolutiva ocupa-se da origem e descendência de entidades biológicas (espécies, populações ou mesmo genes), bem como da sua modificação ao longo do tempo, ou seja, da sua evolução. É uma área heterogénea onde trabalham investigadores oriundos das mais variadas disciplinas taxonómicas, tais como a mamalogia, a ornitologia e a herpetologia, que usam o seu conhecimento sobre esses organismos para responder a questões gerais de evolução. Inclui ainda os paleontólogos que estudam fósseis[37] para responder a questões acerca do modo e do tempo da evolução,[38] e teóricos de áreas como a genética populacional[39] e a teoria evolutiva. Na década de 1990, a biologia do desenvolvimento recuperou o seu papel na biologia evolutiva após a sua exclusão inicial da síntese moderna. Áreas como a filogenia, a sistemática e a taxonomia estão relacionadas com a biologia evolutiva e são por vezes consideradas parte desta.",
    "As duas grandes disciplinas da taxonomia são a botânica e a zoologia.",
    "A classificação dos seres vivos é parte da sistemática, ciência que estuda as relações entre organismos, e que inclui a coleta, preservação e estudo de espécimes, e a análise dos dados vindos de várias áreas de pesquisa biológica.",
    "A partir de Darwin a evolução passou a ser considerada como paradigma central da Biologia, e com isso evidências da paleontologia sobre formas ancestrais, e da embriologia sobre semelhanças nos primeiros estágios de vida. No século XX, a genética e a fisiologia tornaram-se importantes na classificação, como o uso recente da genética molecular na comparação de códigos genéticos.",
    "Os investigadores e pesquisadores da divisão celular mitótica ficam profundamente impressionados com a ordenada complexidade deste processo. Entre todas as complexas manobras que ocorrem na célula durante a mitose, a função biológica consiste em conseguir realizar divisão e duplicação precisas no conteúdo de cada cromossomo do núcleo de uma célula-mãe e distribui-los nas duas células filhas.",
    "A reprodução sexuada dos organismos pluricelulares ocorre com a formação de células haploides - gametas - produzidos a partir das células diploides, no interior das gônadas: testículos (produzindo espermatozoides) e ovários (produzindo óvulos), para os animais. A redução do número cromossômico à metade acontece através de um tipo especial de divisão celular: a meiose.",
    "Charles Darwin (1809-1882), naturalista inglês, desenvolveu uma teoria evolutiva que é a base da moderna teoria sintética: a teoria da seleção natural.",
    "Segundo Darwin, os organismos mais bem adaptados ao meio têm maiores chances de sobrevivência do que os menos adaptados, deixando um número maior de descendentes."
]
matematica = [
    "A matemática é a ciência do raciocínio lógico e abstrato, que estuda quantidades, medidas, espaços, estruturas, variações e estatísticas.",
    "A matemática desenvolveu-se principalmente na Mesopotâmia, no Egito, na Grécia, na Índia e no Oriente Médio.",
    "Registros arqueológicos mostram que a matemática é tanto um fator cultural, quanto parte da história do desenvolvimento da nossa espécie.",
    "Há muito tempo, busca-se um consenso quanto à definição do que é a matemática. No entanto, nas últimas décadas do século XX, tomou forma uma definição que tem ampla aceitação entre os matemáticos: matemática é a ciência das regularidades (padrões). Segundo esta definição, o trabalho do matemático consiste em examinar padrões abstratos, tanto reais como imaginários, visuais ou mentais. Ou seja, os matemáticos procuram regularidades nos números, no espaço, na ciência e na imaginação e formulam teorias com as quais tentam explicar as relações observadas. Uma outra definição seria que matemática é a investigação de estruturas abstratas definidas axiomaticamente, usando a lógica formal como estrutura comum. As estruturas específicas geralmente têm sua origem nas ciências naturais, mais comumente na física, mas os matemáticos também definem e investigam estruturas por razões puramente internas à matemática (matemática pura), por exemplo, ao perceberem que as estruturas fornecem uma generalização unificante de vários subcampos ou uma ferramenta útil em cálculos comuns.",
    "As regras que governam as operações aritméticas são as da álgebra elementar, e as propriedades mais profundas dos números inteiros são estudadas na teoria dos números.",
    "A aritmética é o ramo da matemática que lida com números e com as operações possíveis entre eles.",
    "A pré-história da aritmética é limitada a um pequeno número de artefatos que podem indicar a concepção de adição e subtração, o mais conhecido sendo o osso de Ishango da África Central, que data de algum lugar entre 20.000 e 18.000 a.C., embora sua interpretação seja contestad",
    "A geometria é um ramo da matemática preocupado com questões de forma, tamanho e posição relativa de figuras e com as propriedades dos espaços",
    "A geometria surgiu independentemente em várias culturas antigas como um conjunto de conhecimentos práticos sobre comprimento, área e volume, sendo que o aparecimento de elementos de uma ciência matemática formal é no mínimo tão antigo quanto Tales (século VI a.C.).",
    "Com a introdução do plano cartesiano, muitos problemas de outras áreas da matemática, como álgebra, puderam ser transformados em problemas de geometria (e vice-versa), muitas vezes conduzindo à simplificação das soluções.",
    "A matemática surgiu de necessidades básicas, em especial da necessidade econômica de contabilizar diversos tipos de objetos. De forma semelhante, a origem da geometria (do grego geo =terra + metria= medida, ou seja, 'medir terra') está intimamente ligada à necessidade de melhorar o sistema de arrecadação de impostos de áreas rurais, e foram os antigos egípcios que deram os primeiros passos para o desenvolvimento da disciplina.",
    "No cálculo, a derivada em um ponto de uma função y=f(x) representa a taxa de variação instantânea de y em relação a x neste ponto",
    "A derivada de uma função pode, em princípio, ser calculado a partir da definição, considerando o quociente de diferença, e computar o seu limite. Na prática, uma vez que as derivadas de algumas funções simples são conhecidos, as derivadas de outras funções são mais facilmente calculado usando regras para a obtenção de derivadas de funções mais complicadas das mais simples.",
    "Uma das mais importantes aplicações da Análise à Física (senão a mais importante), é o conceito de derivada temporal — a taxa de mudança ao longo do tempo — que é necessária para a definição precisa de vários importantes conceitos. Em particular, as derivadas temporais da posição s de um objecto são importantes na física newtoniana",
    "Quando uma função depende de mais do que uma variável, podemos usar o conceito de derivada parcial. Podemos entender as derivadas parciais como a derivada de uma função para uma determinada variável, enquanto as outras se mantêm fixadas. No gráfico, é usada para determinar a variação da função em um determinado eixo.",
    "Regra da cadeia e derivada de funções inversas.",
    "Aulas sobre progressão aritmética(PA) e progressão geométrica(PG)."
]

#X -> features, y -> label
frases = biologia + matematica
assuntos = ['biologia'] * 16 + ['matematica'] * 17

text_clf_svm = Pipeline([('vect', CountVectorizer(stop_words=get_stop_words("portuguese"))),
                         ('tfidf', TfidfTransformer()),
                         ('clf', SGDClassifier(loss='log', penalty='l2', alpha=1e-3, max_iter=5, random_state=42))
                         ])

#Parametros
parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
              'tfidf__use_idf': (True, False),
              'clf__alpha': (1e-2, 1e-3),
              }

#Training a linear SVM classifier
if __name__ == '__main__':
        gs_clf_svm = GridSearchCV(text_clf_svm, parameters, n_jobs=-1)
        gs_clf_svm = gs_clf_svm.fit(frases, assuntos)
        with open('my_dumped_classifier.pkl', 'wb') as fid:
            gnb_loaded = p.dump(gs_clf_svm, fid)