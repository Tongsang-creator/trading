import ccxt
import pandas as pd

def loginx():
    return (ccxt.ftx({
    'FTX-SUBACCOUNT':'BuySide',
    'apiKey': '197k2kYpGvyHMy__2H0WGVoHU_TPNkuydWtiig0h',
    'secret': 'toncOlJhZfKO48jb6WLUJ59G67Z6-2EP2uVWCeWh',
    }))
"""
def loginx():
    return (ccxt.ftx({
    'apiKey': 'xiR4FvPEdkPpxWVxYrYYlmJFLpKl7NiSVhEF7IXx',
    'secret': 'FP3-k92SBMEMa-623lMNwoISkwVEqHTBvw6PovbV',
    }))
    """