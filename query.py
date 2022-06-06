import re
import xml.etree.ElementTree as et
import sys
import file_io
from nltk.corpus import stopwords
STOP_WORDS = set(stopwords.words("english"))
from nltk.stem import PorterStemmer
nltk_test = PorterStemmer()

class query:
    def __init__(self, pagerank: bool, titleindex: str, documentindex: str, wordindex: str):
        """Initializes various global variables and inquires the user to input something into terminal

		Parameters: 
		pagerank -- whether or not pagerank will be used
		titleindex --- the titles.txt file that will be read
		documenindex -- the documents.txt file that will be read
		wordsindex -- the words.txt file tha will be read

		Returns:
		N/A

		Throws:
		N/A
		"""

        #Global variables
        #pagerank True represents using pagerank, False represents not using
        self.pagerank = pagerank
        self.title_file = titleindex
        self.document_file = documentindex
        self.word_file = wordindex
        self.title_dict = {}
        self.words_dict = {}
        self.documents_dict = {}

        #REPL to repeatedly inquire the user to input something into terminal
        print("Search> ")
        x = input()

        #When the user inputs ":quit", it will exit
        while(x != ":quit"):
            self.print_results(self.parsing_query(x))
            print("Search> ")
            x = input()

    def read(self):
        """Reads the title, words, and documents files

		Parameters: 
		N/A

		Returns:
		N/A

		Throws:
		N/A
		"""
        file_io.read_title_file(self.title_file, self.title_dict)
        file_io.read_words_file(self.word_file, self.words_dict)
        file_io.read_docs_file(self.document_file, self.documents_dict)

    def parsing_query(self, query: str):
        """Parses to the query for the instances of the input of the user

		Parameters: 
		query -- the input of the user into temrinal

		Returns:
		processed_query which represents the instances of the input of the user

		Throws:
		N/A
		"""
        regex = '''[a-zA-Z0-9]+'[a-zA-Z0-9]+|[a-zA-Z0-9]+'''
        words_in_query = [n.lower() for n in re.findall(regex, query)]
        #Ensure query does not consider stop words
        processed_query = [nltk_test.stem(n) for n in words_in_query if n not in STOP_WORDS]
        return processed_query

    def run(self, processed_query):
        """Generates the dictionary that holds the relevance of each page, with and without consideration to pagerank

		Parameters: 
		processed_query -- the list that was generated from parsing_query()

		Returns:
		pageid_to_relevance_sum which is a dictionary representing the sum of relevances of each page

		Throws:
		N/A
		"""
        page_indices = list(self.title_dict.keys())
        pageid_to_relevance_sum = {}
        #Fill in pageid_to_relevance which each title
        for i in range(len(self.title_dict)):
            for word in processed_query:
                pageid = page_indices[i]
                try:
                    #Obtain the relevance add the current page_id
                    pageid_to_relevance = self.words_dict[word]
                    relevance = pageid_to_relevance[pageid]
                    #Add the relevance to the to total relevance for that pageid
                    try:
                        pageid_to_relevance_sum[pageid] += relevance
                    except KeyError:
                        pageid_to_relevance_sum[pageid] = relevance
                except KeyError:
                    pass
        #Incorporate pagerank depending on the pagerank flag
        if self.pagerank:
            sorted_pagerank = sorted(self.documents_dict.items(), key=lambda x: x[1], reverse = True)
            for key, value in pageid_to_relevance_sum.items():
                new_value = self.documents_dict[key] * value * 100000000000
                pageid_to_relevance_sum[key] = new_value
            for i in range(10):
                page_id = sorted_pagerank[i][0]
                pagerank = sorted_pagerank[i][1]
                pageid_to_relevance_sum[page_id] = pagerank
            return pageid_to_relevance_sum
        else:
            return pageid_to_relevance_sum

    def get_top_ten(self, dict):
        """Returns the indices of the top ten items

		Parameters: 
		dict -- the ddictionary of the sum of relevances of words

		Returns:
		N/A

		Throws:
		N/A
		"""
        sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse = True)
        indices = []
        n = 0
        while n < 10:
            try:
                indices.append(sorted_dict[n][0])
                n += 1
            #If there are less than 10 items, then just return the items existing
            except IndexError:
                return indices        
        return indices


    def print_results(self, processed_query : list[str]):
        """Prints the results of the top ten most relevant items

		Parameters: 
		processed_query -- the list query generated by getting items with the user's input in them

		Returns:
		N/A

		Throws:
		N/A
		"""
        self.read()
        sum_of_relevances = self.run(processed_query)
        indices_of_top_ten = self.get_top_ten(sum_of_relevances)
        #If no indices exist for a query, then return this message
        if indices_of_top_ten == []:
            print("No result is found, please try something else:")
        #Print the ordered results in correct format
        else:
            for i in range(1, len(indices_of_top_ten) + 1):
                index = indices_of_top_ten[i - 1]
                title = self.title_dict[index]
                print(str(i) + " " + title)

if __name__ == "__main__":
    """Main method that inquires the user to input a word

    Parameters: 
    N/A

	Returns:
    N/A

	Throws:
	N/A
	"""
    #Depending on the size of the user's input, a query will or will not be created
    if(len(sys.argv) == 4):
        query(False, sys.argv[1], sys.argv[2], sys.argv[3])
    elif(len(sys.argv) == 5):
        if sys.argv[1] == "--pagerank":
            query(True, sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            print("Retry! Bad input.")
    else:
        print("Retry! Bad input.")