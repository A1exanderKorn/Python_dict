# --------------------------------------------№5  ИВБО-01-21  Вариант 39-------------------------------------------------
# https://kispython.ru/docs/4/%D0%98%D0%92%D0%91%D0%9E-01-21.html#%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82-39

# import math
#
# def main(x, z):
#     ans = 0
#     n = len(x)
#     for i in range(1, n+1):
#         a1 = z[math.ceil(i / 4)-1] + x[n + 1 - math.ceil(i / 4)-1] ** 2 + 15 * z[math.ceil(i / 4)-1] ** 3
#         a2 = math.log(a1) ** 7
#         ans += a2
#     return ans
#
#
# print(main([0.24, 0.07, 0.66, 0.29], [0.47, 0.52, -0.73, 0.12]))
# print(main([-0.87, -0.04, -0.18, -0.36], [0.91, 0.09, 0.61, -0.55]))
# print(main([0.96, 0.53, -0.78, 0.82], [0.88, 0.0, -0.51, -0.01]))
# print(main([-0.77, -0.66, -0.41, -0.87], [0.16, -0.68, 0.46, -0.89]))
# print(main([0.25, 0.34, -0.69, 0.21], [0.97, 0.75, -0.7, 0.08]))










# --------------------------------------------№6  ИВБО-01-21  Вариант 40-------------------------------------------------
# https://kispython.ru/docs/5/%D0%98%D0%92%D0%91%D0%9E-01-21.html#%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82-40
#
# class Tree:
#     def __init__(self, num):
#         self.num=num
#         self.child = {}
#
#     def add(self, name, tree):
#         self.child[name] = tree
#
#
# def createTree():
#     tree2 = Tree(2)
#     tree2.add(2000, Tree(0))
#     tree2.add(2011, Tree(1))
#     tree2.add(1982, Tree(2))
#
#     tree0 = Tree(0)
#     tree0.add('COQ', Tree(4))
#     tree0.add('URWEB', Tree(5))
#
#     tree3 = Tree(3)
#     tree3.add(2015, tree2)
#     tree3.add(1961, Tree(3))
#     tree3.add(1967, tree0)
#
#     tree0 = Tree(0)
#     tree0.add('COQ', Tree(7))
#     tree0.add('URWEB', Tree(8))
#
#     tree2 = Tree(2)
#     tree2.add(2000, Tree(6))
#     tree2.add(2011, tree0)
#     tree2.add(1982, Tree(9))
#
#     tree = Tree(1)
#     tree.add('TEA', tree3)
#     tree.add('SHELL', tree2)
#
#     return tree
#
# def main(arr):
#     ind = 1
#     t = createTree()
#     while len(t.child)!=0:
#         t = t.child[arr[ind]]
#         ind = t.num
#
#     return t.num
#
#
# print(main(['URWEB', 'SHELL', 2000, 2015])) # 6
# print(main(['URWEB', 'SHELL', 1982, 2015])) # 9
# print(main(['COQ', 'TEA', 2011, 1961])) # 3
# print(main(['COQ', 'TEA', 1982, 1967])) # 4
# print(main(['COQ', 'TEA', 2011, 2015])) # 1

















# --------------------------------------------№7  ИВБО-01-21  Вариант 38-------------------------------------------------
# https://kispython.ru/docs/6/%D0%98%D0%92%D0%91%D0%9E-01-21.html#%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82-38
#
# def main(data):
#     ans = 0
#
#     ans += data['U1'] & 0b1111
#     ans += (data['U2'] & 0b111111111) << 4
#     ans += (data['U3'] & 0b111111) << 13
#     ans += (data['U4'] & 0b111111) << 19
#     ans += (data['U5'] & 0b111) << 25
#
#     return ans
#
# print(main({'U1': 13, 'U2': 110, 'U3': 50, 'U4': 13, 'U5': 7}))
# print(main({'U1': 2, 'U2': 161, 'U3': 26, 'U4': 38, 'U5': 1}))

# --------------------------------------------№7  ИВБО-01-21  Вариант 39-------------------------------------------------
# https://kispython.ru/docs/6/%D0%98%D0%92%D0%91%D0%9E-01-21.html#%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82-39
#
# def main(data):
#     data = int(data, 16)
#
#     p1 = data & 0b11
#     p2 = data >> 2 & 0b111
#     p3 = data >> 5 & 0b111111111
#     p4 = data >> 14 & 0b1111
#
#     return tuple([p1, p2, p3, p4])
#
# print(main('0xfcbc'))
# print(main('0x1c875'))
# print(main('0x1bd19'))
# print(main('0x1e89d'))

# --------------------------------------------№7  ИВБО-01-21  Вариант 40-------------------------------------------------
# https://kispython.ru/docs/6/%D0%98%D0%92%D0%91%D0%9E-01-21.html#%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82-40
#
# def main(data):
#     data = int(data, 16)
#
#     d1 = data & 0b11
#     d3 = data >> 4 & 0b11111
#     d4 = data >> 9 & 0b11111
#     d5 = data >> 14 & 0b11
#
#     ans = d3
#     ans += d4 << 5
#     ans += d1 << 10
#     ans += d5 << 12
#
#     return hex(ans)
#
# print(main('0xf010')) # 0x3301
# print(main('0xd554')) # 0x3155
# print(main('0xfe8d')) # 0x37e8
# print(main('0x9d9a')) # 0x29d9



















# --------------------------------------------№8  ИВБО-01-21  Вариант 40-------------------------------------------------
# https://kispython.ru/docs/7/%D0%98%D0%92%D0%91%D0%9E-01-21.html#%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82-40
# import re
#
# def main(s):
#     #s = re.sub(r'\\', '', s)
#     s = s.replace('\n', ' ')
#     s = s.replace('\begin', '\n')
#     s = s.replace('\end', '\n')
#
#     a = re.findall(r'auto q\((.+)\) ?is', s)
#     b = re.findall(r'\{.+}', s)
#     for i in range(len(b)):
#         b[i] = re.findall(r'(-?\d+)', b[i])
#
#     ans = []
#     for i in range(len(a)):
#         c = tuple([a[i], b[i]])
#         ans.append(c)
#
#     return ans
#
# print(main('''<block> \begin auto q(reesre_330)is {-5661 -2094 -496 -1540}\end
# \begin auto q(leriri_953) is{ 8700 6893 } \end \begin auto
# q(esonle_621) is {8277 -875 -3326 601 } \end \begin auto q(enti)is {
# 293 -3706} \end </block>'''))
#
# print(main('''<block> \begin auto q(ribi_153) is { -8179 6118 -6047 } \end \begin
# auto q(sosoat) is {-2594 7691 6058 }\end\begin auto q(edri) is{ -4328
# 4361}\end\begin auto q(cein_838) is { -3380 4079 5076 } \end </block>'''))



























# --------------------------------------------№10  ИВБО-01-21  Вариант 40------------------------------------------------
# https://kispython.ru/docs/9/%D0%98%D0%92%D0%91%D0%9E-01-21.html#%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82-40
# class MealyError(Exception):
#     pass
#
#
# class Mealy:
#
#     def __init__(self):
#         self.pos = 'A'
#         self.dict = {'A' : {'cull' : ['A', 1], 'crush' : ['B', 0]},
#                      'B' : {'cull' : ['E', 3], 'crush' : ['C', 2]},
#                      'C' : {'cull' : ['D', 4], 'crush' : ['E', 5]},
#                      'D' : {                   'crush' : ['E', 6]},
#                      'E' : {'cull' : ['F', 7], 'crush' : ['E', 8]},
#                      'F' : {'cull' : ['G', 9]                    },
#                      'G' : {'cull' : ['E', 11], 'crush' : ['H', 10]},
#                      'H' : {                                     }}
#
#     def cull(self):
#         if ('cull' in self.dict[self.pos].keys()):
#             data = self.dict[self.pos]['cull']
#             self.pos = data[0]
#             return data[1]
#         else:
#             raise MealyError('cull')
#
#     def crush(self):
#         if ('crush' in self.dict[self.pos].keys()):
#             data = self.dict[self.pos]['crush']
#             self.pos = data[0]
#             return data[1]
#         else:
#             raise MealyError('crush')
#
# def main():
#     return Mealy()
#
# def test():
#     m = main()
#     assert m.cull() == 1
#     assert m.crush() == 0
#     assert m.crush() == 2
#     assert m.crush() == 5
#     assert m.crush() == 8
#     assert m.cull() == 7
#     assert m.cull() == 9
#     assert m.cull() == 11
#     assert m.cull() == 7
#     try:
#         a = m.crush()
#     except Exception as e:
#         assert type(e) == MealyError
#     assert m.cull() == 9
#     assert m.crush() == 10
#     try:
#         a = m.cull()
#     except Exception as e:
#         assert type(e) == MealyError
#     try:
#         a = m.crush()
#     except Exception as e:
#         assert type(e) == MealyError
#
#     m = main()
#     assert m.crush() == 0
#     assert m.cull() == 3
#
#     m = main()
#     assert m.crush() == 0
#     assert m.crush() == 2
#     assert m.cull() == 4
#     try:
#         a = m.cull()
#     except Exception as e:
#         assert type(e) == MealyError
#     assert m.cull() == 6
