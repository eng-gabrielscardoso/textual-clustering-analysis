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

## Clustering the inverted indexes

> Under development

## (Cluster) Textual Analysis

> Under development

## Chart plotting

## Compressing the inverted indexes
