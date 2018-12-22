from ArtistConnections import Vertex, Edge
from SongLibrary import SongLibrary

class DFA:

    def __init__(self, s=None):
        self.start = s

    """
    Build the DFA graph from the figure in task 2

    """
    def build_DFA(self):
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

        characters = list(seq)
        current = self.start
        for i in range(len(characters)):
            next = current.followEdge(characters[i])
            if next is None:
                return False
            else:
                current = next
        if current.isAcceptingState:
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
            if self.testMatch(seq[i:]):
                return i
        return indx



    """
    For every song in the song library array, test whether they will be accepted by the state machine
    Store the match index or -1 into the matchIndx array.
    Please make sure the order of songs in the songlibrary is the same as the input file

    """
    def testSongLibrary(self, song_lib):
        matchIndx = []
        for song in song_lib.songArray:
            indx = self.testAccept(song.DNA)
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
