Yutong Wang and Joshua Wang

Bugs: 
Not that we can think of.

How to run the program:
1. Run the indexer by typing in terminal "python3 index.py '.xml file' titles.txt documents.txt words.txt"
Keep in mind that '.xml file' should be replaced by whatever .xml you want to index. Additionally, if this does not work, replace 'python3' with 'py'

2. Run the querier by typing in terminal either 
"python3 query.py --pagerank titles.txt documents.txt words.txt" if you want to run with pagerank or 
"python3 query.py titles.txt documents.txt words.txt" if you want to run withOUT pagerank 

3. At this point in time, enter whatever keywords you would like into terminal and it will return a rank of links of relevance

4. Repeat step 3 as many times as you would like

5. Enter ":quit" to exit the program

Description of how all pieces of your program fit together:
index.py fills in the titles, documents, and words files with various methods:
processing_text essentially parses, tokenizes, removes stop words, and stems in all the titles text of the pages of the xml file into data structures with titles, links, ids, etc. 
calculate_term_relevances generates the relevances of each title to its frequency of appearances into a dictionary
dict_to_weight_mat() creates a list of weights of pages from the XML file is connected to that is used in pagerank() to rank every page from the XML file in a list
Calling on these these methods allow for the generation of the titles file through write_title_file(), the words file through write_words_file(), and the documents file through write_docs_file() from fil_io.py

Having created the titles, documents, and words files, query.py repeatedly inquires the user to input a particular keyword and outputs a ranking of relevant links with various methods:
read() calls on read_title_file(), read_words_file(), and read_docs_file() which fills data structures based on the files and are used in later methods
parsing_query() is called on parses the query for instances of the user's input
With the parsed query generated, it is used to create dictionary representing the sum of the relevances of each word using or not using pagerank in the run() method
The indices of the top ten most relevant items are recorded using the get_top_ten() method which is then accessed to print the titles of the ranked results in order

Description of features you failed to implement, as well as any extra features you implemented:
We implemented every required feature, and we didn't implement any extra features.

Description of how you tested your program:

We used 2pageWiki.xml to test basic parsing of inputs and certain fields in the constructor. There are many edge cases in 2pageWiki, for example pages with no text, duplicate words, stop words, all-caps words, and links. 
The resulting title_list is [‘a’, ‘b’]
The resulting pageid_to_text is {0: ['a'], 1: ['b', 'anoth', 'sentenc', 'sentenc', 'hello']}.
The resulting title_to_links is {'a': [], 'b': []}.
The resulting pagecount is 2.

We also kept track of system tests with run time in a testing log (see attached pdf) as we gradually optimized our code. Initially we used a matrix to store the values of relevances, and even loading smallwiki takes more than 6 minutes. We also moved certain variables, methods and fields around to reduce the space required to store large data structures, duplicate calculations, and the number of times we access data structures. Our run time significantly improved after we changed the data structure to store page relevances from a matrix to a nested dictionary  (so that we don’t need to store all the 0s) and rounded some numbers in calculations. Eventually, our record to load SmallWiki, MedWiki, BigWiki are 1.7s, 27.6s, and 3min15s respectively.

We wrote unit tests in test.py.

System tests for: Testing SmallWiki.xml, MedWiki.xml, BigWiki.xml.

SmallWiki.xml with PageRank
Carthage
1 History of Carthage
2 Saint Louis Cathedral, Carthage
3 Ancient Carthage
4 Carthage National Museum
5 Carthago delenda est
6 Shofet
7 Hundred and Four
8 Carthage Paleo-Christian Museum
9 Carthaginian Iberia
10 The Seven Hills

Work
1 Ash heap of history
2 Psychohistory
3 Anachronism
4 United States
5 Chronology
6 Intellectual history
7 Glossary of history
8 Memory hole
9 Philosophy of war
10 Sinecure

SmallWiki.xml without PageRank
The
No result is found, please try something else:

important
1 Macro-historical
2 Motya
3 Elegant decay
4 Transformation of culture
5 Kerkouane
6 Nationalization of history
7 Theater (warfare)
8 Rome
9 Intellectual history
10 Military history

stuff
1 Anachronism

MedWiki.xml with PageRank
watch 
1 Fahrenheit 451
2 Luanda
3 Shock site
4 Nail (fastener)
5 Joseph Stalin
6 Martin Waldseem?ller
7 Franklin D. Roosevelt
8 Enter the Dragon
9 Meher Baba
10 G?tterd?mmerung

United States
1 Federated States of Micronesia
2 Government
3 Illinois
4 Franklin D. Roosevelt
5 Imperial units
6 Michigan
7 International Criminal Court
8 Louisiana
9 Guam
10 Ohio

the
1 Pakistan
2 Netherlands
3 Neolithic
4 Hinduism
5 Portugal
6 Nazi Germany
7 Planet
8 Hong Kong
9 Norway
10 Monarch

MedWiki.xml without PageRank
united
1 Enjambment
2 Imperial units
3 Gauss (unit)
4 Joule
5 FSB
6 Mercury
7 Imperialism in Asia
8 Harvard (disambiguation)
9 Hub
10 Politics of Grenada

pope
1 Pope Gregory VIII
2 Pope Eugene II
3 Pope Alexander IV
4 Pope
5 Pope Gregory V
6 Pope Benedict III
7 Pope Formosus
8 Pope Gregory XIV
9 Pope Clement III
10 Pope Alexander VII

search
1 Isa (disambiguation)
2 Eth
3 Earle Page
4 Kaluza?Klein theory
5 Earless seal
6 Geocaching
7 EFTPOS
8 Lorisidae
9 Gopher (protocol)
10 Empress Suiko

BigWiki.xml with PageRank
hello
1 Hello world program
2 Java (programming language)
3 Law of averages
4 Foobar
5 Forth (programming language)
6 Objective-C
7 Hungarian language
8 Enjambment
9 Grammatical case
10 Metasyntactic variable

Goods
1 Gross domestic product
2 Factors of production
3 Industrial Revolution
4 Free market
5 John Locke
6 Monopoly
7 Friedrich Nietzsche
8 Plato
9 Macroeconomics
10 Epicurus

Brown
1 Gordon Brown
2 Empress K?gyoku
3 Mesopotamia
4 Empress Jit?
5 Emperor Tenji
6 Empress Suiko
7 Emperor Mommu
8 Emperor Sh?mu
9 Funk
10 Ford Madox Brown

BigWiki.xml with PageRank
hello
1 Hello world program
2 Java (programming language)
3 Law of averages
4 Enjambment
5 Metasyntactic variable
6 Foobar
7 Pigeonhole sort
8 Michel Tremblay
9 Forth (programming language)
10 MUMPS

search
1 Google Search
2 Linear search
3 Military of Hong Kong
4 Genetic
5 Gomoku
6 Ivory-billed Woodpecker
7 Keyword
8 Erinyes
9 Isa (disambiguation)
10 Optimization (disambiguation)

models
1 European Centre for Medium-Range Weather Forecasts
2 Keyboard send receive
3 GIA
4 Model
5 Model organism
6 Rail transport modelling
7 Mathematical model
8 Model theory
9 Futurama (New York World's Fair)
10 Econometrics
