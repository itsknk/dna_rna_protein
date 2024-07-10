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

### Why Transcribe DNA to RNA and Translate RNA to Protein?

#### The Central Dogma of Molecular Biology

The central dogma of molecular biology describes the flow of genetic information within a biological system. It is often summarized as:
- **DNA → RNA → Protein**

This flow involves two key processes:
1. **Transcription:** The process of converting DNA into RNA.
2. **Translation:** The process of converting RNA into protein.

#### Why Transcribe DNA to RNA?

1. **Separation of Information Storage and Usage:**
   - **DNA Stability:** DNA is a stable, double-stranded molecule that stores genetic information in the nucleus (in eukaryotes). Its stability is crucial for the long-term preservation of genetic information.
   - **RNA Flexibility:** RNA is a more flexible, single-stranded molecule that can travel from the nucleus to the cytoplasm. This allows the genetic information to be used without compromising the stability of the original DNA.

2. **Regulation of Gene Expression:**
   - **Control Mechanism:** Transcription allows for precise regulation of gene expression. Cells can control which genes are transcribed and how much RNA is produced, enabling a dynamic response to environmental signals and internal needs.
   - **Temporal and Spatial Control:** Different cell types can transcribe different sets of genes based on their function and stage of development. This allows for specialization and complex multicellular organization.

3. **Multiple Copies for Amplification:**
   - **Gene Amplification:** Transcription can produce many copies of RNA from a single gene, allowing for the amplification of the genetic message. This is necessary for producing enough protein to meet the cell’s demands.

#### Why Translate RNA to Protein?

1. **Functional Molecules:**
   - **Proteins as Workhorses:** Proteins are the primary functional molecules within cells. They act as enzymes, structural components, signaling molecules, and transporters, among other roles. The diverse functions of proteins are essential for the cell's structure and activities.
   - **Diverse Functions:** The 20 different amino acids can be arranged in countless sequences to create proteins with a wide variety of shapes and functions, enabling the complexity of life.

2. **Efficiency and Accuracy:**
   - **Ribosomes and Translation:** Ribosomes, the molecular machines that carry out translation, ensure that proteins are synthesized accurately and efficiently. The process of translation decodes the genetic information in mRNA into the specific sequence of amino acids in a protein.
   - **Codon-Anticodon Matching:** The genetic code ensures that each codon (a sequence of three RNA bases) corresponds to a specific amino acid or a stop signal, guiding the correct assembly of proteins.

3. **Modularity and Versatility:**
   - **Modular Design:** By separating the storage of genetic information (DNA) from its functional expression (proteins), cells can maintain a modular design. This allows for the reuse and recombination of genetic elements to create new proteins and functions.
   - **Adaptability:** The modularity of transcription and translation systems allows organisms to adapt and evolve by altering gene regulation and protein synthesis without changing the core genetic material.

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
