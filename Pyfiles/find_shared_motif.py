#!/usr/bin/env python3

import sys


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


def find_longest_shared_motif(sequences):
    """
    Find the longest shared motif i.e. longest common substring
    from a list of sequences. While avoiding doing as much unecessary
    work as possible.

    A suffix tree is the theoretically optimal way to do this but is
    probably excessive for a problem like this.

    Arguments:
        sequences -- list of sequences formatted as strings

    Return:
        shared_motif -- longest shared motif/substring between sequences
    """

    # we only want to look at the shortest first because
    # no shared motif can be longer than the shortest sequence
    sequences.sort(key=lambda s: len(s))
    shortest_seq = sequences.pop(0)

    longest_motif = ""
    for start_ix in range(len(shortest_seq)):
        # step backwards using negative 3rd argument in range
        for end_ix in range(len(shortest_seq), start_ix, -1):
            # only bother checking if we haven't already found something longer
            current_candidate = shortest_seq[start_ix: end_ix]
            if len(current_candidate) > len(longest_motif):
                share_motif = []
                for seq in sequences:
                    if current_candidate in seq:
                        share_motif.append(True)
                    # if any sequence doesn't have the motif then it isn't
                    # common so we can move straight onto the next candidate
                    # using break
                    else:
                        share_motif.append(False)
                        break
                # if everything shares the new longer candidate update the
                # longest found motif
                if all(share_motif):
                    longest_motif = current_candidate

    return longest_motif

if __name__ == '__main__':

    sequences = [seq[1] for seq in read_fasta(sys.argv[1])]
    longest_motif = find_longest_shared_motif(sequences)
    print(longest_motif)
