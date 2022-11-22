#!/usr/bin/env python
# coding: utf-8

from biology import est_base, est_adn, arn, arn_to_codons, load_dico_codons_aa, codons_stop, codons_to_aa

def test_est_base():
    assert est_base("A")
    assert est_base("z")==False
    print("test_est_base = ok")
    
def test_est_adn():
    assert est_adn("ATGTCAAA")
    assert est_adn("ATBOAATG")==False
    print("test_est_adn = ok")
    
def test_arn():
    assert arn("ATGTCAAA")=="AUGUCAAA"
    assert arn("ATBOAATG")==None
    print("test_arn = ok")
    
def test_arn_to_codons():
    assert arn_to_codons("CGUUAGGGG")==["CGU", "UAG", "GGG"]
    assert arn_to_codons("CGUAAU")==arn_to_codons("CGUAAUGC")
    print("test_arn_to_codons = ok")
    
def test_codons_stop():
    assert codons_stop(load_dico_codons_aa("./data/codons_aa.json"))==["UAA"]
    print("test_codons_stop = ok")
    
def test_codons_to_aa():
    assert codons_to_aa(["CGU", "AAU", "UAA", "GGG", "CGU"],
                        (load_dico_codons_aa("./data/codons_aa.json")))==['Arginine', 'Asparagine']
    assert codons_to_aa(["CGU", "AAU", "GGG", "CGU"],
                        (load_dico_codons_aa("./data/codons_aa.json")))==['Arginine', 'Asparagine', 'Glycine', 'Arginine']
    print("test_codons_to_aa = ok")