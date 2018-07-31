def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            print('[0] test of finally-block execution')
#            raise Exception("1st error in finally block")
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
            print('[1] test of finally-block execution')
    except Exception as ex:
        print(ex)
        print(ex.args)

fancy_divide([0,2, 4], 0)

fancy_divide([0,2, 4], 1)

fancy_divide([0,2, 4], 3)
