#Given the names and grades for each student in a Physics class of N students, 
#store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
#The first line contains an integer,N, the number of students.
#The 2N subsequent lines describe each student over 2 lines; 
#the first line contains a student's name, and the second line contains their grade.
#Print the name(s) of any student(s) having the second lowest grade in Physics;
#if there are multiple students, order their names alphabetically and print each one on a new line.


def main():
    cantEstudiante = int(input())
    estudiantes = []
    notas = set()

    for i in range(cantEstudiante):
        estudiante = input()
        nota = float(input())
        notas.add(nota)
        estudiantes.append([estudiante, nota])

    segundo_nota = sorted(notas)[1]
    segundo_estudiante = sorted([estudiante[0] for estudiante in estudiantes if estudiante[1] == segundo_nota])
    for estudiante in segundo_estudiante:
        print(estudiante)


if __name__ == '__main__':
   main()
