from sklearn.feature_extraction.text import CountVectorizer
from settings import *
import pandas as pd
import random
import numpy


class DocumentCollection:
    feature_set = {}
    document_map = {}
    training_set = {}
    test_set = {}

    def __init__(self):
        pass

    def populate_map(self):
        """
        Populate a document map to store the collection of data for referencing
        :return: Populated collection hash table
        """
        # Declare constants for CSV parsing
        header =["id", "author", "date", "content", "class"]

        # Read data into document map
        for filename in os.listdir(DATA_ROOT):
            # Ensure the file is a CSV file
            if filename.endswith(".csv"):
                # Create path and key for hash table
                file_path = DATA_ROOT+"/"+filename
                file_key = os.path.splitext(filename)[0]
                self.document_map[file_key] = pd.read_csv(file_path, sep=',', names=header, skiprows=1)

    def print_collection(self):
        """
        Pretty print the collection of data
        :return: Pretty print to stdout
        """
        for key, value in self.document_map.iteritems():
            print "\nComment Collection for: ", key
            print value.to_string()

    def leave_one_out(self):
        """
        Select a random data frame and use that for testing
        :return:
        """
        rand_set = random.choice(self.document_map.keys())
        print self.document_map[rand_set]

    def extract_features(self):
        """
        Extract features using a count vectorizer to store word frequencies
        :return:
        """
        count_vectorizer = CountVectorizer()
        for key, value in self.document_map.iteritems():
            self.feature_set[key] = count_vectorizer.fit_transform(value['content'].values)
