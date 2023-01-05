class YieldCallback:
    links = [['aa', 'bb', 'cc', ['11', '22', '33']],
             ['aaa', 'bbb', 'ccc', ['111', '222', '333']],
             ['aaaa', 'bbbb', 'cccc', ['1111', '2222', '3333']]
        , ['aaaaa', 'bbbbb', 'ccccc', ['11111', '22222', '33333']]]

    attrs = [['aa1', 'bb1', 'cc1', ['11a', '22a', '33a']], ['aaa1', 'bbb1', 'ccc1', ['111a', '222a', '333a']],
             ['aaaa1', 'bbbb1', 'cccc1', ['1111a', '2222a', '3333a']]
        , ['aaaaa1', 'bbbbb1', 'ccccc1', ['11111a', '22222a', '33333a']]]

    # def dopa(self):

    def dopa(self, arr ,dic):
        # if which == "link":
        print('########### parse begin #################')
        for link in arr:
            yield {
                'name': link[0],
                'age': link[1],
                'degree': link[2]
            }
        # else:
        #     for link in self.attrs:
        #         yield {
        #             'name': link[0],
        #             'age': link[1],
        #             'degree': link[2]
        #         }
        print('???????????????????????????????????')
        next = 0
        if dic:
            next = dic['inx']
        print('###########next:  %d', next)
        yield self.dopa(self.attrs, {"inx": next + 1})

if __name__ == "__main__":
    yy = YieldCallback()
    dp = yy.dopa(yy.links, {"inx": 0})
    print(next(dp))
    print(next(dp))
    print(next(dp))
    print(next(dp))

    dpp = next(dp)
    print(next(dpp))
    print(next(dpp))
    print(next(dpp))
    print(next(dpp))
    # print(next(dpp))

    dppp = next(dpp)
    print(next(dppp))
    print(next(dppp))
    print(next(dppp))
    print(next(dppp))
    # print(next(dppp))

    dpppaaaa = next(dppp)
    print(next(dpppaaaa))
    print(next(dpppaaaa))
    print(next(dpppaaaa))
    print(next(dpppaaaa))

    # print(next(dpp))
    # print(next(dpp))

    # print(next(next(dp)))
    # print(next(dp))
    # print(next(dp))

