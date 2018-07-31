def Towers(n,fr,to,spare):
    """
    :param n: number of disks (int)
    :param fr: move disks from tower 'fr' (str)
    :param to: move disks to tower 'to' (str)
    :param spare: using spare tower 'spare' (str)
    :return: moves required to move 'n' disks from tower 'fr' to tower 'to',
        using spare tower 'spare' (str)
    """

    def movedisk(fr,to):
        print('move disk from',fr,'to',to + '.')
    if n == 1:
        return movedisk(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr)

n = int(input('Enter number of disks: '))
fr = str(input('Enter Tower where disks are stacked: '))
to = str(input('Enter Tower where disks are to be moved: '))
spare = str(input('Enter spare tower: '))

Towers(n,fr,to,spare)

