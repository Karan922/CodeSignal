def karan(n):
    loop = True
    while loop:
        p = [n]
        arr1 = []
        arr2 = []
        try:
            for i in p:
                v = i.split('.')
                arr1.append(v)
            if arr1[0][0] == '':
                arr1[0].remove('')
        except ValueError:
            return False
            loop = False

        for i in arr1[0]:
            f = 'False'
            t = 'True'
            try:
                if int(i) > 255:
                    arr2.append(f)
                elif len(arr1[0]) < 4:
                    arr2.append(f)
                elif i == '00':
                    arr2.append(f)
                elif len(arr1[0]) > 4:
                    arr2.append(f)
                elif i == '01':
                    arr2.append(f)
                else:
                    arr2.append(t)
            except ValueError:
                k = 'False'
                arr2.append(k)
                loop = False

        if 'False' in arr2:
            return False
        else:
            return True
        loop = False
