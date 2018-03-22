#!/usr/bin/env python3

def read_fasta(filepath):
    """
    Generator to read multiline fasta found at the filepath
    as required.
    Yields a tuple containing the (accession, sequence)

    Arguments:
        filepath -- string containing path to Fasta formatted file

    Return:
        (accession, sequence) -- tuple containing two strings, first with the
                                 accession and second with sequence
    """

    with open(filepath) as filehandle:
        accession = None
        sequence = ""
        for line in filehandle:
            # removes newline character from the end of the line
            line = line.strip()
            if line.startswith(">"):
                # will be True if accession==None
                if accession:
                    """
                    yield is similar to return but works for generators
                    the next iteration the function will return after
                    the yield command until the generator is exhausted
                    i.e. all the file has been read in this case
                    https://wiki.python.org/moin/Generators
                    """
                    yield (accession, sequence)
                accession = line
                sequence = ""
            else:
                sequence += line
        if accession:
            yield (accession, sequence)

