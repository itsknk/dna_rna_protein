## DNA/RNA/Protein Translator

This project is a web-based application that translates DNA sequences to RNA sequences and subsequently translates RNA sequences to protein sequences. It allows users to input either DNA or RNA sequences, choose to translate in one or all reading frames, and displays the results.

### Biological Background

#### DNA

DNA (Deoxyribonucleic Acid) is the molecule that carries genetic instructions in all living organisms. It consists of two long chains of nucleotides twisted into a double helix. The sequence of the bases (Adenine [A], Thymine [T], Cytosine [C], and Guanine [G]) encodes genetic information.

#### RNA

RNA (Ribonucleic Acid) is a single-stranded molecule involved in protein synthesis. Its nucleotides include Adenine (A), Uracil (U), Cytosine (C), and Guanine (G). RNA carries genetic information from DNA to the ribosomes for protein synthesis.

#### Protein

Proteins are complex molecules made up of amino acids. They perform many critical functions in living organisms. The sequence of amino acids in a protein is determined by the sequence of nucleotides in the RNA.

#### Transcription: DNA to RNA

Transcription is the process of copying a segment of DNA into RNA. RNA polymerase reads the DNA strand and synthesizes a complementary RNA strand, where Adenine (A) pairs with Uracil (U) instead of Thymine (T).

#### Translation: RNA to Protein

Translation is the process of decoding the RNA sequence into a sequence of amino acids, resulting in a protein. This occurs in the ribosomes. Each set of three RNA bases (codon) corresponds to a specific amino acid or a stop signal in the genetic code.

### Features

- Input DNA or RNA sequences
- Transcribe DNA to RNA
- Translate RNA to proteins
- Option to translate all reading frames or just one
- User-friendly web interface

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/itsknk/dna_rna_protein.git
    cd dna_rna_protein
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Run the Flask app:

    ```bash
    python app.py
    ```

5. Open your browser and go to `http://127.0.0.1:5000/` to use the application.

## Usage

1. Open the application in your web browser.
2. Select the input type (DNA or RNA).
3. Enter your sequence in the provided textarea.
4. (Optional) Check the box to translate all reading frames.
5. Click the "Translate" button to see the RNA transcription and protein translation results.

## Code Overview

### index.html

This file sets up the web interface using HTML and Jinja2 templating. It includes:

- A form for sequence input, type selection, and translation options.
- Display sections for RNA transcription and protein translation results.

### app.py

This is the main Flask application file. It includes:

- `transcribe_dna_to_rna(dna_sequence)`: Converts DNA sequences to RNA.
- `translate_rna_to_protein(rna_sequence)`: Translates RNA sequences to protein sequences using a codon table.
- `translate_all_frames(rna_sequence)`: Translates RNA sequences in all three possible reading frames.
- Route `/`: Handles form submissions, processes the input, and renders the results.

### License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/itsknk/dna_rna_protein/blob/master/LICENSE) file for details.

### To do
- Add comments to the code.
