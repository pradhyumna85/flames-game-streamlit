import pandas as pd

def flames_game(name1: str,name2: str):
    if not (len(name1) and len(name2)):
        raise ValueError('Provide valid inputs for parameters name1 and name2!')

    ## preprocess/clean input -> remove spaces, convert to lowercase
    name1 = name1.replace(' ','').lower()
    name2 = name2.replace(' ','').lower()

    ## counts of each characters in the names
    name1_cts = pd.Series(list(name1)).value_counts().to_dict()
    name2_cts = pd.Series(list(name2)).value_counts().to_dict()

    ## Cross characters comparing both names
    for char in name1:
        if char in name2_cts:
            if name2_cts[char]!=0:
                name2_cts[char] -= 1
                if name1_cts[char]!=0:
                    name1_cts[char] -= 1

    ## exclude 0 count/deleted characters
    name2_cts = {key:value for key,value in name2_cts.items() if value!=0}
    name1_cts = {key:value for key,value in name1_cts.items() if value!=0}

    ## number of uncrossed characters left
    num_left = sum(name1_cts.values()) + sum(name2_cts.values())

    ## actual flames sequence using the number of characters left
    flames = 'flames'
    while len(flames)!=1:
        if num_left <= len(flames):
            if len(flames)==num_left:
                cut_ind = len(flames)-1
            else:
                cut_ind = num_left
        else: ## num_left > len(flames)
            if num_left%len(flames)==0:
                cut_ind = len(flames)-1
            else:
                cut_ind = (num_left%len(flames)) - 1

        if cut_ind==len(flames)-1:
            flames = flames[:-1]
        elif cut_ind == 0:
            flames = flames[1:]
        else:
            flames = flames[cut_ind+1:] + flames[:cut_ind]

    flame_dict = {'f':'Friends','l':'Love','a':'Affection','m':'Marriage','e':'Enemy','s':'Brother/Sister'}

    return flame_dict[flames]

if __name__ == '__main__':
    print(flames_game('sanidhi prakash','prakhar prateek'))