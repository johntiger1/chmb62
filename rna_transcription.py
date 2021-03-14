
def generate_coding_strand(rna_input_seq):
    '''
    Generates the DNA coding strand for a given RNA input seq
    :param rna_input_seq:
    :return:
    '''
    return

def generate_template_strand(rna_input_seq):
    '''
    Generates the DNA template strand for a given RNA input seq
    :param rna_input_seq:
    :return:
    '''
    RNA_TO_DNA_MAPPING = {

        "A": "T",
        "C": "G",
        "G": "C",
        "U": "A"
    }
    DNA_seq = []
    for char in rna_input_seq:
        DNA_seq.append(RNA_TO_DNA_MAPPING[char])
    RNA_seq = reversed(DNA_seq)
    return "".join(RNA_seq)



if __name__ == "__main__":
    print(generate_template_strand("AUGCCCAACAGCAAGAGUGGUGCCCUGUCGAAGGAG"))