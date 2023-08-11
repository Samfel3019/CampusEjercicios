class StudentManager:
    def _init_(self):
        self.students = []

    def add_student(self, code, name, partial_scores):
        student = {
            "code": code,
            "name": name,
            "partial_scores": partial_scores,
            "final_score": 0
        }
        self.students.append(student)

    def find_student(self, code):
        for student in self.students:
            if student["code"] == code:
                return student
        return None

    def update_student(self, code, name, partial_scores):
        student = self.find_student(code)
        if student:
            student["name"] = name
            student["partial_scores"] = partial_scores

    def delete_student(self, code):
        student = self.find_student(code)
        if student:
            self.students.remove(student)

    def calculate_final_scores(self):
        for student in self.students:
            final_score = sum(student["partial_scores"]) / len(student["partial_scores"])
            student["final_score"] = final_score

    def list_students(self):
        for student in self.students:
            print("Code:", student["code"])
            print("Name:", student["name"])
            print("Partial Scores:", student["partial_scores"])
            print("Final Score:", student["final_score"])
            print("-" * 30)

def main():
    student_manager = StudentManager()

    while True:
        print("MENÚ PRINCIPAL")
        print("1. Agregar un nuevo registro")
        print("2. Buscar un Estudiante")
        print("3. Actualizar datos del Estudiante")
        print("4. Borrar un estudiante")
        print("5. Calcular notas definitivas")
        print("6. Listar estudiantes con notas definitivas")
        choice = int(input("Seleccione una opción: "))

        if choice == 1:
            code = input("Código del Estudiante: ")
            name = input("Nombre Completo: ")
            partial_scores = [float(input(f"Nota Parcial {i + 1}: ")) for i in range(3)]
            student_manager.add_student(code, name, partial_scores)
        elif choice == 2:
            code = input("Ingrese el código del Estudiante: ")
            student = student_manager.find_student(code)
            if student:
                print("Código:", student["code"])
                print("Nombre:", student["name"])
                print("Notas Parciales:", student["partial_scores"])
            else:
                print("Estudiante no encontrado.")
        elif choice == 3:
            code = input("Ingrese el código del Estudiante: ")
            student = student_manager.find_student(code)
            if student:
                name = input("Nuevo Nombre Completo: ")
                partial_scores = [float(input(f"Nueva Nota Parcial {i + 1}: ")) for i in range(3)]
                student_manager.update_student(code, name, partial_scores)
            else:
                print("Estudiante no encontrado.")
        elif choice == 4:
            code = input("Ingrese el código del Estudiante a borrar: ")
            student_manager.delete_student(code)
        elif choice == 5:
            student_manager.calculate_final_scores()
        elif choice == 6:
            student_manager.list_students()
        else:
            print("Opción no válida.")

            if name == "_main_":
                main()