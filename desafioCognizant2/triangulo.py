lados = [float(x) for x in input().split()]

a = lados[0];
b = lados[1];
c = lados[2];

if a + b > c and a + c > b and b + c > a:

    Perimetro = a + b + c
    print(f"Perimetro = {(a + b + c):.1f}")
else:

    areaTrapezio = ((a + b) * c) / 2
    print(f"Area = {areaTrapezio:.1f}")