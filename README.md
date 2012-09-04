This script uses Cameron Neylon's [chemspipy.py](https://github.com/cameronneylon/ChemSpiPy) and Matt Swain's [CIRpy](https://github.com/mcs07/CIRpy) to convert a compound name into a chemical identifier.

The script operates in three steps:
* CIRpy to query the [NCI structure resolver](http://cactus.nci.nih.gov/chemical/structure/documentation)
* chemspipy.py to queryChemspider
* CIRpy to query the NCI resolver with pattern matching enabled

The first successful match is returned as the first part of tuple, the second part indicating the matching step ['NCI', 'ChemSpi', 'NCI-pattern-match']. Needless to mention that the confidence for matches labelled 'NCI-pattern-match' is a bit lower compared to 'NCI' and 'ChemSpi'.

For the script to work, you need a token from Chemspider, stored as a plain-text string in the file 'chemsp_token' in your working directory. If you don't have a token you can omit the chemspider tab by commenting out the lines 22-29 in names2ids.py.

 

