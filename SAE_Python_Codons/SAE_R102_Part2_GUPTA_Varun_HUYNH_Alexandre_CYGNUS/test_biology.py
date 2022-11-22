#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from biology import *

def test_nextIndice():
    assert nextIndice(["bonjour", "hello", "buongiorno", "ciao", "bye"], 1, ["hello", "bye"])==1
    assert nextIndice(["bonjour", "halo", "buongiorno", "ciao", "bye"], 1, ["hello", "bye"])==4
    assert nextIndice(["bonjour", "halo", "buongiorno", "ciao", "b"], 1, ["hello", "bye"])==5
    assert nextIndice(["bonjour", "hello", "buongiorno", "ciao", "bye"], 3, ["hello", "bye"])==4
    print("test_nextIndice() = ok")
    
def test_decoupe_sequence():
    assert decoupe_sequence(["val1", "début", "val2", "val3", "end", "val4", "fin", "begin", "val5", "fin", "val6"],
                            ["début", "begin"],
                            ["fin", "end"])==[["val2", "val3"],["val5"]]
    assert decoupe_sequence(["val1", "début", "end", "val4", "fin", "begin", "val5", "fin", "val6"],
                            ["début", "begin"],
                            ["fin", "end"])==[["val5"]]
    assert decoupe_sequence(["val1", "début", "end", "val4", "fin", "begin", "fin", "val6"],
                            ["début", "begin"],
                            ["fin", "end"])==[]
    print("test_decoupe_sequence() = ok")
    
def test_codons_to_seq_codantes():
    dico=load_dico_codons_aa("./data/codons_aa.json")
    assert codons_to_seq_codantes(["CGU", "UUU", "AUG", "CGU", "AUG", "AAU", "UAA", "AUG", "GGG", "CCC", "CGU", "UAG", "GGG"],
                                  dico)==[['CGU', 'AUG', 'AAU'], ['GGG', 'CCC', 'CGU']]
    assert codons_to_seq_codantes(["CGU", "UUU", "AUG", "UAA", "AUG", "GGG", "CCC",  "CGU", "UAG", "GGG"],
                                  dico)==[['GGG', 'CCC', 'CGU']]
    assert codons_to_seq_codantes(["CGU", "UUU", "AUG", "UAA", "AUG", "UAG", "GGG"],
                                  dico)==[]
    print("test_codons_to_seq_codantes() = ok")
    
def test_seq_codantes_to_seq_aas():
    assert seq_codantes_to_seq_aas(codons_to_seq_codantes(["CGU", "UUU", "AUG", "CGU", "AUG", 
                                                           "AAU", "UAA", "AUG", "GGG", "CCC", 
                                                           "CGU", "UAG", "GGG"],
                                                          load_dico_codons_aa("./data/codons_aa.json")),
                                   load_dico_codons_aa("./data/codons_aa.json"))==[['Arginine', 'Methionine', 'Asparagine'], 
                                                                                   ['Glycine', 'Proline', 'Arginine']]
    print("test_seq_codantes_to_seq_aas() = ok")
    
def test_adn_encode_molecule():
    assert adn_encode_molecule("CGTTTTATGCGTATGAATTAAATGGGGCCCCGTTAGGGG",
                               load_dico_codons_aa("./data/codons_aa.json"),
                               ["Glycine", "Proline", "Arginine"])
    assert not adn_encode_molecule("TGCTTTATGCGTATGAATTAAATAAAGCCCCGTTAGTTT",
                                   load_dico_codons_aa("./data/codons_aa.json"),
                                   ["Glycine", "Proline", "Arginine"])
    print("test_adn_encode_molecule() = ok")