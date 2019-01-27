'''
this script creates a wordlist  , i know there's alot of them (as crunch)  but i wanted to make mine :3
'''
import counter


def welcomer():
 #   try:
    minimum = int(input("insert the minimum of the characters you want (only numbers): "))
    maximum = int(input("insert the maximum of the characters you want (only numbers): "))
    global characters, rep_req
    characters=str(input("insert the string of characters you want to use(can be anything, just avoid duplication "))
    rep_req = int(input("insert the maximum number of chars repitation allowed in the word: "))+1
    input('ok when ready press inter:')
    creater(minimum, maximum)
#    except :
 #       print("bad enteries, bad boi!! fix it now and enter only nums!")


#characters = "ABCD1234"



def creater(minimum, maximum):
    code = []
    for i in range(minimum):
        code.append(0)
    counter.bruter(code, maximum, len(characters) - 1)


def allowed_to_write(handler):
    if len(handler)==1:
        return True
    rep_c = 0
    for i in range(len(handler)):
        #print('i=' + str(i))
        for r in range(1, rep_req+1):

            try:
                #print('r+i=' + str(r + i))
                if handler[i] == handler[i + r]:
                    rep_c += 1
            except IndexError:
                pass
    if rep_c < rep_req:
        #print(rep_c)
        return True

###
def bruterhand(data):
    # data is a list given by bruter() in counter file 
    handler = data
    finalpass = ''
    allowed = allowed_to_write(handler)
    if allowed == True:
        for q in range(len(data)):
            finalpass = finalpass + characters[data[q]]
        write_on_file(finalpass)

counter.bruterhand = bruterhand
#counter file requires this assignement to use its output 


def write_on_file(catched):
    #edit this to generate a file or do whatever you want with the output
    print(catched)


if __name__ == '__main__':
    welcomer()
