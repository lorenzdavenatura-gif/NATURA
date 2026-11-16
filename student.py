class Student:
   
    def __init__(self, name, studentId, grade):
        self.__name = name
        self.__studentId = studentId
        self.__grade = grade

   
    def getName(self):
        return self.__name

    def getStudentId(self):
        return self.__studentId

    def getGrade(self):
        return self.__grade

    
    def setGrade(self, grade):
        self.__grade = grade

    
    def displayInfo(self):
        print("Name:", self.__name,
              "| ID:", self.__studentId,
              "| Grade:", self.__grade)



def main():
    
    student1 = Student("MALOU WANG", "241-0995-1", 90.0)
    student2 = Student("BERTO WANG", "241-0996-1", 88.5)

    
    student1.setGrade(92.0)

    
    student1.displayInfo()
    student2.displayInfo()

if __name__ == "__main__":
    main()