# inverted_index
## That is document search engine.
### For now we created reader for CRANFIELD http://ir.dcs.gla.ac.uk/resources/test_collections/cran/, which provides a set of documents and corresponding queries, as well as ranking of queries.
### Preprocessing class provides methods for tokenizing and stemming of both queries and documents, as well as removing stop-words from them.
### There's implementation of Vector Space Model with TF-IDF space and Language Model with 1-gram query likelyhood. 
### Note: VectorSpaceModel provides methods write_inverted_file read_inverted_file to write and read inverted file from memory, but our search machine appears to be really fast and efficient on chosen dataset so we are not using it.
