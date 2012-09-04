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
  
  idstring = None
  source = None

  if idstring is None:
    source = 'NCI'
    idstring = cirpy.resolve(name, outformat)
  if idstring is None:
    source = 'ChemSpi'
    chemspid = chemspipy.find_one(name)
    try:
      smiles = chemspid.smiles
      idstring = cirpy.resolve(smiles, outformat)
    except AttributeError:
      idstring = None
  if idstring is None:
    source = 'NCI-pattern-match'
    idstring = cirpy.resolve(name, outformat,['name_pattern'])
  if idstring is None:
    source = None
    idstring = str(idstring)
  try: 
    idstring = (idstring.rstrip(),source)
  except AttributeError:
    idstring  = (idstring[0].rstrip(),source)
    print 'There were multiple results for: ', name, ' using: ', idstring[0], '\n', idstring 

  return idstring

""" Convert SMILES to stdinchikey using the NCI resolver."""
def smiles2stdinchikey(smiles):

  import cirpy
  import queryDevice

  idstring = None
  source = None

  if idstring is None:
    idstring = cirpy.resolve(smiles, 'stdinchikey')
    source = 'NCI'
  try:
    idstring = (idstring.rstrip(),source)
  except AttributeError:
    idstring  = (idstring[0].rstrip(),source)
    print 'There were multiple results for: ', name, ' using: ', idString[0], '\n', idstring

  return idstring

