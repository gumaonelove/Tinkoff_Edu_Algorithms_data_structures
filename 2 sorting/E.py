'''
А еще дан массив размера n, состоящий из нулей. Все 0 по очереди превращаются в 1, в порядке, заданном в тесте.
От вас требуется после каждой замены говорить, сколько внешних циклов сделаем алгоритм сортировки (до вызова break),
если его запустить на массиве.

Заметьте, что вы не должны сортировать, вы должны только сказать, сколько итераций понадобилось бы на сортировку.
'''


n = int(input())
all = input().split()
a = set()
len_a = 0
n_ = n
ans = [1]
for i in range (n):
    a.add(all[i])
    len_a += 1
    while str(n_) in a:
        a.remove(str(n_))
        len_a -= 1
        n_ -= 1
    ans.append(len_a + 1)

print(*ans)