import Methods

# Czytamy zbiór z pliku
testList = Methods.readFromFile("C:/Users/Dominik/testList.txt")

# Bierzemy słownik, który ma w sobie atrybuty decyzyjne i ich liczności, a także wartości prawdopodobieństw ustawione
# na 1
mainAttributeDict = Methods.getDictOfAtrributes(testList)
print("Witaj w klasyfikatorze naiwny Bayes!")

while True:
    attributeToTest = input("Wpisz obserwacje do zaklasyfikowania, poszczególne atrybuty oddzielone ';'\n")

    # Lista atrybutów do przetestowania
    attributeList = attributeToTest.split(';')

    if len(attributeList) != len(testList[0]) - 1:
        print('Niepoprawna liczba argumentów!!!')
        continue

    # Dla każdego atrybutu obliczamy prawdopodobieństwo
    for decisiveAttribute in mainAttributeDict.keys():

        # bierzemy wystąpenia
        totalOccurences = mainAttributeDict[decisiveAttribute]["occurences"]

        for index in range(0, len(attributeList)):

            # liczymy interesujące nas rekordy testowe
            numerator = Methods.countAttributeWithDecision(testList, attributeList[index], decisiveAttribute, index)
            denominator = totalOccurences

            # jeżeli nic nie znajdziemy, stosujemy wygładzanie Laplace'a
            if numerator == 0:
                numerator = 1
                denominator += Methods.countUnique(testList, index)

            mainAttributeDict[decisiveAttribute]["likelihood"] *= (numerator / denominator)

        mainAttributeDict[decisiveAttribute]["likelihood"] *= (totalOccurences / len(testList))


    for decisiveAttribute in mainAttributeDict.keys():
        print(f'{decisiveAttribute} == {mainAttributeDict[decisiveAttribute]["likelihood"]}')

    # Znajdujemy najwyższe prawdopodobieństwo wśród atrybutów
    finalVerdict = list(mainAttributeDict.keys())[0]

    for decisiveAttribute in mainAttributeDict.keys():
        if mainAttributeDict[decisiveAttribute]["likelihood"] > mainAttributeDict[finalVerdict]["likelihood"]:
            finalVerdict = decisiveAttribute

    print(f'PLAY for {attributeToTest} == {finalVerdict}\n')

    print("Jeśli chcesz sprawdzić inne dane, wpisz |continue|. Jeśli chcesz wyjść, wpisz |end|")

    while True:
        command = input("Wprowadz komende:\n")
        if command == 'continue':
            print('Ok, zaczynam testowanie')
            break
        elif command == 'end':
            print('Ok, koncze dzialanie')
            exit()
        else:
            print('Niepoprawna komenda!!!')

    # Resetujemy prawdopodobieństwa jeśli idziemy dalej
    for decisiveAttribute in mainAttributeDict.keys():
        mainAttributeDict[decisiveAttribute]["likelihood"] = 1
