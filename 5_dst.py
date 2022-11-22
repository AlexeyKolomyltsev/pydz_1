A = [int(input(f"Введите {i} коррдинаты точки А: ")) for i in [1,2]]
B = [int(input(f"Введите {i} коррдинаты точки B: ")) for i in [1,2]]
q_dst = 0
for i in range(len(A)):
    q_dst += (A[i] - B[i])**2
dst = round(q_dst ** 0.5 , 2)
print(f'Расстояние между точками А и В = {dst}')