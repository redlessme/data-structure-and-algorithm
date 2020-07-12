with open("bigger_dictionary.txt", 'rb') as f:
    line = f.readlines()

alist = []

for x in line:
    line = x.decode('utf8').strip()
    sline = line.split(": ")
    if sline != ['']:
        alist.append(sline)
wordList = []
freqList = []
defList = []
for i in range(len(alist)):
    if alist[i][0] == "word":
        wordList.append(alist[i][1])
    elif alist[i][0] == "frequency":
        freqList.append(alist[i][1])
    elif alist[i][0] == "definition":
        defList.append(alist[i][1])


class Information:
    def __init__(self, word, frequency,id):  # definition,
        self.word = word
        self.frequency = frequency
        self.id = id

class Trie(object):
    def __init__(self):
        self.trie_root = [None] * 28
        self.trie_root.append(0)

    def insert(self, Information):
        word = Information.word
        freq = Information.frequency
        id=Information.id
        trie = self.trie_root
        for c in word:
            if trie[ord(c) - ord('a')] is None:  # if current node doesnt have a child c,pointer..., else,move to the node.
                trie[ord(c) - ord('a')] = [None] * 28
                trie[ord(c) - ord('a')].append(0)
            if trie[-2] is None:
                trie[-2]=freq
                trie[-3]=id
            elif int(freq)>int(trie[-2]):
                trie[-2]=freq
                trie[-3]=id
            elif int(freq)==int(trie[-2]):
                if word<wordList[trie[-3]]:
                    trie[-3]=id
            trie[-1] += 1 #count
            trie = trie[ord(c) - ord('a')] #move to next node

        trie[-3]=id
        trie[-1] = 1

    def autoComplete(self, prefix):
        trie = self.trie_root
        for c in prefix:
            if trie[ord(c) - ord('a')] is None:
                return "There is no2 word in the dictionary that has "+'"'+prefix+'"'+" as a prefix."
            trie = trie[ord(c) - ord('a')]
        result = "Auto-complete suggestion:{}\nDefinition: {}\nThere are {} words in the dictionary that have ".format(wordList[trie[-3]], defList[trie[-3]],trie[-1])+'"'+prefix+'"'+" as a prefix."
        return result

if __name__ == '__main__':
    trie = Trie()
    for i in range(len(wordList)):
        info=Information(wordList[i],freqList[i],i)
        trie.insert(info)
    while True:
        prefixInput = input("Please enter a prefix:")
        if prefixInput=="***":
            print("Bye Alice!")
            break
        print(trie.autoComplete(prefixInput)+"\n")