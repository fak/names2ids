"""
Function: names2id.py

This script uses Cameron Neylon's chemspipy.py https://github.com/cameronneylon/ChemSpiPy and Matt Swain's CIRpy to convert compound names to chemical identifiers. 

  --------------
momo.sander@googlemail.com
"""


def name2id(name, outformat):

  import cirpy
  import chemspipy
  import queryDevice  


  idDict = {}
  
  idstring = None
  source = None

  if idstring is None:
    idstring = cirpy.resolve(name, outformat)
    source = 'NCI'
  if idstring is None:
    chemspid = chemspipy.find_one(name)
    try:
      smiles = chemspid.smiles
      idstring = cirpy.resolve(smiles, outformat)
    except AttributeError:
      pass
    source = 'ChemSpi'
  if idstring is None:
    idstring = cirpy.resolve(name, outformat,['name_pattern'])
    source = 'NCI-pattern-match'
  if idstring is None:
    source = None
    idstring = str(idstring)
  try: 
    idstring = (idstring.rstrip(),source)
  except AttributeError:
    idstring  = (idstring[0].rstrip(),source)
    print 'There were multiple results for: ', name, ' using: ', idString[0], '\n', idstring 

            

  return idstring
