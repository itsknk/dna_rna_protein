from flask import Flask, render_template, request

app = Flask(__name__)

def transcribe_dna_to_rna(dna_sequence):
    return dna_sequence.replace('T', 'U')

def translate_rna_to_protein(rna_sequence):
    codon_table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    protein_sequence = ''
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        if len(codon) == 3:
            amino_acid = codon_table.get(codon, 'X')  # 'X' for unknown codons
            if amino_acid == '*':  # Stop codon
                break
            protein_sequence += amino_acid
    
    return protein_sequence

def translate_all_frames(rna_sequence):
    return {
        f"+{i+1}": translate_rna_to_protein(rna_sequence[i:])
        for i in range(3)
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    sequence_input = ''
    sequence_type = 'dna'
    all_frames = False
    rna_output = ''
    protein_output = {}
    
    if request.method == 'POST':
        sequence_input = request.form['sequence_input'].upper()
        sequence_type = request.form['sequence_type']
        all_frames = 'all_frames' in request.form
        
        if sequence_type == 'dna':
            rna_output = transcribe_dna_to_rna(sequence_input)
        else:
            rna_output = sequence_input
        
        if all_frames:
            protein_output = translate_all_frames(rna_output)
        else:
            protein_output = {"+1": translate_rna_to_protein(rna_output)}
    
    return render_template('index.html', 
                           sequence_input=sequence_input,
                           sequence_type=sequence_type,
                           all_frames=all_frames,
                           rna_output=rna_output,
                           protein_output=protein_output)

if __name__ == '__main__':
    app.run(debug=True)
