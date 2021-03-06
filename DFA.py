from ArtistConnections import Vertex, Edge
from SongLibrary import SongLibrary

class DFA:

    def __init__(self, s=None):
        self.start = s

    """
    Build the DFA graph from the figure in task 2

    """
    def build_DFA(self):
        # This is pretty straightforward... Create vertices, add edges, and set the acceptingState
        v0 = Vertex(0)
        self.start = v0
        v1 = Vertex(1)
        v2 = Vertex(2)
        v3 = Vertex(3)
        v4 = Vertex(4)
        v5 = Vertex(5)
        v6 = Vertex(6)
        v7 = Vertex(7)

        v7.setAcceptingState()

        v0.addEdge(Edge('A', v1))
        v1.addEdge(Edge('A', v1))
        v1.addEdge(Edge('C', v2))
        v2.addEdge(Edge('A', v3))
        v3.addEdge(Edge('T', v1))
        v3.addEdge(Edge('C', v4))
        v4.addEdge(Edge('A', v5))
        v5.addEdge(Edge('G', v6))
        v5.addEdge(Edge('C', v4))
        v5.addEdge(Edge('T', v1))
        v6.addEdge(Edge('A', v7))
        v7.addEdge(Edge('A', v1))
        v7.addEdge(Edge('C', v2))

        return



    """
    Test whether the input sequence seq will be accepted by the state machine
    return True if accept

    """
    def testMatch(self, seq):

        characters = list(seq) # Create a list with each character
        current = self.start # Set the start as the start vertex
        for i in range(len(characters)):
            # It will go into the next vertex only if its the right sequence, if it finds a character that is not in the
            # sequence, next will be None
            next = current.followEdge(characters[i])
            if next is None:
                return False
            else:
                current = next  # Sets the next vertex as the current.
        if current.isAcceptingState: # If the last vertex is an Accepting state it will return True
            return True
        return False

    """
    Test whether the one suffix of the input sequence seq will be accepted by the state machine
    return the index position if accept
    return -1 if not accept

    """
    def testAccept(self, seq):
        indx = -1
        characters = list(seq)
        for i in range(len(characters)):
            # Using the testMatch function with each subsequence of the sequence given each time starting at i to the end
            if self.testMatch(seq[i:]):
                return i
        return indx



    """
    For every song in the song library array, test whether they will be accepted by the state machine
    Store the match index or -1 into the matchIndx array.
    Please make sure the order of songs in the songlibrary is the same as the input file

    """
    def testSongLibrary(self, song_lib):
        matchIndx = [] # Creating list to store the indices for the songs
        for song in song_lib.songArray: # Iterating through all the songs
            # Using the testAccept function to get the index at which the subsequence will be accepted
            indx = self.testAccept(song.DNA)
            # Appends it to the matchIndx list
            matchIndx.append(indx)
        return matchIndx


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':

    dfa = DFA()
    dfa.build_DFA()
    song_lib = SongLibrary()   # Creating a new songLibrary object
    song_lib.loadLibrary()   # Loading the library
    print(dfa.testAccept('AACACATCACAGA'))     # Testing a sequence
    # print(dfa.testAccept('CGTAGTCTAGAGCACACTAAATGAGACATCTTAGAGGAGATAGGCGTAGATCCGGTTACAACACATCACAGA'))
    print(dfa.testSongLibrary(song_lib))  # Testing song library
    print("finish")
