class Solution:
    def minRepeats(self, A, B):
        for i in B:
            if i not in A:
                return -1
        list = []
        for j in range(len(A)):
            if A[j] == B[0]:
                list.append(j)
        while True:
            ftr = True
            for i in range(len(B)):
                if B[i] != A[list[0]]:
                    list.pop(0)
                    ftr = False
                    break
                list[0] = list[0] + 1
                if list[0] > len(A) - 1:
                    list[0] = 0

            if ftr == True:
                break
            else:
                if bool(list) == False:
                    return -1
        repeat = 1
        stn = A
        tm = False
        while stn.find(B) < 0:
            tm = True
            stn += A
            repeat += 1
        return repeat

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        A = input()
        B = input()

        ob = Solution()
        print(ob.minRepeats(A,B))
# t = 3
# A = abcd
# B = cdabcdab