# Architecture

The architecture is based in a pseudo-data structure called [Inverted Index](https://en.wikipedia.org/wiki/Inverted_index), taught during the discipline of Data Structures II.

## Creating the inverted indexes

The inverted index structure is created using the [`InvertedIndex`](src/app/inverted_index.py) class. The constructor takes the sanitised content from documents as list and returns a dictionary that contains the following structure:

```python
{
  "word": {
    "count": 10, # integer that represents the number of times the word appears on document
  }
  # ...
}
```

## Sanitisation

The sanitisation of the documents occurs in the [`Sanitisation`](src/utils/sanitisation.py) class. The most important thing to understand is that in this class there's a static method called `sanitise` which is responsible for return a list of words contained in the document. This is necessary because during the clustering/textual analysis process stuff like special characters or ASCII characters and more sanitisation before clustering.

## (Cluster) Textual Analysis

Essentially, the clustering is done using the [`TextualAnalysis`](src/app/textual_analysis.py) class. The most important thing to understand is that in this class most of the operations are use the inverted indexes or raw files to cluster the data based on pattern matching.

## Chart plotting

To plot the charts we use the library [MatplotLib](https://matplotlib.org/).

## Compressing the inverted indexes

To compress the files we use the Huffman algorithm as approach.
