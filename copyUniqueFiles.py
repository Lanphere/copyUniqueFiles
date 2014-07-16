


def copyUniqueFiles (source1, source2, result):

    """
    assuming copyUniqueFiles.py is in the parent directory, copies files from
    child directory 'source1' and child directory 'source2', into the child
    directory 'result' while eliminating any duplicates (files common to both dir's).

    requires all 3 directories to exist prior to running.
    """

    import os
    import shutil

    dictA = {}
    dictB = {}

    for file in os.listdir(source1):
        dictA[file] = source1

    for file in os.listdir(source2):
        dictB[file] = source2

    # dictComb is a unique dictionary "set" (eliminates duplicates)
    dictComb = dictA.copy()
    dictComb.update(dictB)

    for k in dictComb:
        shutil.copy2('{0}/{1}'.format(str(dictComb[k]),str(k)), result)




#example--add your directory names in quotes
copyUniqueFiles ('someFolder', 'someFolder2', 'resultFolder')

