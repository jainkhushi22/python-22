from ATMMENU import ATMMENU
from atmoperations import *
from atmexcep import *
while(True):
    ATMMENU()
    ch = int(input("enter any choice "))

    match (ch):
        case 1:
            try:
                deposit()
            except ValueError:
                print("don't write alumns,symbols")
            except depositError:
                print("don't write -ve or zero value")
        case 2:
            try:
                withdraw()
            except withdrawError:
                print("don't write -ve or zero value")
            except ValueError:
                print("don't write alumns,symbols")
            except insufficientfundError:
                print("you have insuffiecient balance")

        case 3:
            checkbal()
        case 4:
            print("thanks for using the program")
            break
        case _:
            print("ur selection is wrong")

