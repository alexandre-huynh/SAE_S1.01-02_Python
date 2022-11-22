from json import *


def est_base(c):
    return len(c) == 1 and c in "ATGC"


def est_adn(s):
    i = 0
    while i < len(s) and est_base(s[i]):
        i += 1
    return i >= len(s)


def arn(adn):
    if not est_adn(adn):
        return None
    s = ""
    i = 0
    while i < len(adn):
        if adn[i] == "T":
            s += "U"
        else:
            s += adn[i]
        i += 1
    return s


def arn_to_codons(arn):
    codons = []
    i = 0
    while i < len(arn) - 2:
        codons.append(arn[i] + arn[i + 1] + arn[i + 2])
        i += 3
    return codons


def load_dico_codons_aa(filename):
    fichier = open(filename, "r")
    strjson = fichier.read()
    fichier.close()
    return loads(strjson)


def codons_stop(dico):
    stop = []
    bases = "AUGC"
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            k = 0
            while k < 4:
                if bases[i] + bases[j] + bases[k] not in dico:
                    stop.append(bases[i] + bases[j] + bases[k])
                k += 1
            j += 1
        i += 1
    return stop


def codons_to_aa(codons, dico):
    aa = []
    i = 0
    while i < len(codons) and codons[i] in dico:
        aa.append(dico[codons[i]])
        i += 1
    return aa

def nextIndice(tab, ind, elements):
    i=ind
    while i<len(tab):
        j=0
        while j<len(elements):
            if elements[j]==tab[i]:
                return tab.index(elements[j])
            j+=1
        i+=1
    return len(tab)


def decoupe_sequence(seq,start,stop):
    tab=[]
    i=0
    while i<len(seq):
        tab_seq=[]
        if seq[i] in start:
            j=i+1
            while seq[j] not in stop:
                tab_seq.append(seq[j])
                j+=1
            if len(tab_seq)>0:
                tab.append(tab_seq)
            i=j
        else:
            i+=1
    return tab


def codons_to_seq_codantes(codons,dico):
    return decoupe_sequence(codons,["AUG"],codons_stop(dico))


def seq_codantes_to_seq_aas(seq_codantes, dico):
    tab=[]
    i=0
    while i<len(seq_codantes):
        seq_aas=[]
        j=0
        while j<len(seq_codantes[i]):
            seq_aas.append(dico[seq_codantes[i][j]])
            j+=1
        tab.append(seq_aas)
        i+=1
    return tab


def adn_encode_molecule(adn, dico, molecule):
    final=seq_codantes_to_seq_aas(codons_to_seq_codantes(arn_to_codons(arn(adn)),dico),dico)
    i=0
    while i<len(final):
        if final[i]==molecule:
            return True
        i+=1
    return False
