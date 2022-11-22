#!/usr/bin/env python
# coding: utf-8

from json import *

def est_base(car):
    return car=="A" or car=="T" or car=="G" or car=="C"


def est_adn(ch):
    i=0
    while i<len(ch):
        if est_base(ch[i])==False:
            return False
        i+=1
    return True


def arn(seq_adn):
    if est_adn(seq_adn)==False:
        return None
    return seq_adn.replace("T","U")


def arn_to_codons(seq_arn):
    tab=[]
    i=0
    j=0
    while i<len(seq_arn)//3:
        compteur=0
        codon=""
        while compteur<3:
            codon+=seq_arn[j]
            j+=1
            compteur+=1
        tab.append(codon)
        i+=1
    return tab


def load_dico_codons_aa(fichier_json):
    fichier = open(fichier_json,"r")
    json = fichier.read()
    fichier.close()
    codon_json = loads(json)
    return codon_json 


def codons_stop(dico_codons):
    tab=[]
    car_codon="AUGC"
    for car_1 in car_codon:
        codon = car_1 
        for car_2 in car_codon:
            codon += car_2
            for car_3 in car_codon:
                codon += car_3
                if len(codon) == 3 and codon not in list(dico_codons):
                    tab.append(codon)
    return tab


def codons_to_aa(tab_codon, dico_codons):
    tab=[]
    i=0
    while i<len(tab_codon):
        if tab_codon[i] not in list(dico_codons):
            return tab
        tab.append(dico_codons[tab_codon[i]])
        i+=1
    return tab




def nextIndice(tab, ind, elements):
    pass


def decoupe_sequence(seq, start, stop):
    pass


def codons_to_seq_codantes(codons, dico):
    pass


def seq_codantes_to_seq_aas(seq_codantes, dico):
    pass


def adn_encode_molecule(adn, dico, molecule):
    pass
