# Libraries
import csv, random, time
import urllib.request, json

# Functions
def dictKeysToList(dictA):
    keys = []
    for k in dictA:
        keys.append(k)
    return keys

def dictValuesToList(dictA):
    values = []
    for k in dictA:
        values.append(dictA[k])
    return values

def extractFromJSON(urlInput):
    with urllib.request.urlopen(urlInput) as url:
        data = json.loads(url.read().decode())
    return data

def printNice(lista, endParam):
    for e in lista:
        if(type(e))==float:
            print("%.7E"%e, end = endParam)
        else:
            print(e, end = endParam)
    print()

def writeCSVHeaderFromJSON(urlInput, outputFile, jsonParam):
    data = extractFromJSON(urlInput)
    eData = data[jsonParam]
    fieldnames = dictKeysToList(eData)
    with open(outputFile, 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
    return fieldnames

def writeCSVRowFromJSON(urlInput, outputFile, jsonParam):
    data = extractFromJSON(urlInput)
    eData = data[jsonParam]
    fieldnames = dictKeysToList(eData)
    values = dictValuesToList(eData)
    with open(outputFile, 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writerow(eData)
    return values

# Constants
urlInput = 'https://api.tidex.com/api/3/ticker/eth_btc'
outputFile = 'data.csv'
jsonParam = 'eth_btc'

# Write header in csv file
fieldnames = writeCSVHeaderFromJSON(urlInput, outputFile, jsonParam)
printNice(fieldnames, '\t\t')

# Write data in csv file
while True:
    values = writeCSVRowFromJSON(urlInput, outputFile, jsonParam)
    printNice(values, '\t')
    time.sleep(0.5)