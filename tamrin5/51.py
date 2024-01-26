class MrKrabs:
    def __init__(self, dna):
        self.dna = dna

    def process_dna(self):
        reversed_dna = self.dna[:10][::1]
        self.dna = self.dna + reversed_dna
        result = self.dna.replace('tt', 'o')
        return result


class SpongeBob:
    def __init__(self, dna):
        self.dna = dna

    def process_dna(self):
        a = str(int(len(self.dna)))
        a  =  "".join(sorted(a))
        result = int(a) + 100 
        return result
        


class Squidward:
    def __init__(self, dna):
        self.dna = dna

    def linear_search_and_modify(self):
        new_dna = ""
        i = 0
        j = 0
        count = 0
        while i < len(self.dna):
            if self.dna[i] == 'x' and count == 0:
                j = i
                count += 1
            while (i + 3 < len(self.dna)) and (self.dna[i] == self.dna[i + 1]) and (self.dna[i] ==self.dna[i + 2]):
                new_dna += "(0_0)"
                i += 3
            else:
                new_dna += self.dna[i]
                i += 1
        if j != 0 :
            new_dna += str(j)
        self.dna = new_dna
        return self.dna
        
    def process_dna(self):
        squidward = Squidward(self.dna[0:])
        result = squidward.linear_search_and_modify()
        return result


def main():
    input_dna = input().strip()

    if input_dna.startswith('m'):
        character = MrKrabs(input_dna)
    elif input_dna.startswith('sb'):
        character = SpongeBob(input_dna)
    elif input_dna.startswith('s') and input_dna[1] != 'b':
        character = Squidward(input_dna)
    elif input_dna[len(input_dna) - 1] == 'm':
        input_dna = input_dna[::-1]
        character = MrKrabs(input_dna)
    elif (input_dna[len(input_dna) - 1] == 's') and (input_dna[len(input_dna) - 2] == 'b'):
        input_dna = input_dna[::-1]
        character = SpongeBob(input_dna)
    elif (input_dna[len(input_dna) - 1] == 's') and (input_dna[len(input_dna) - 2] != 'b'):
        input_dna = input_dna[::-1]
        character = Squidward(input_dna)
    else:
        print('invalid input')
        return
    
    result = character.process_dna()
    print(result)
if __name__ == "__main__":
    main()
