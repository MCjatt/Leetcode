class Solution(object):
    def reverseWords(self, s):
        letter = []
        i = 0
        mylist = s.split()
        mylist.reverse()
        new = " ".join(mylist)
        return new