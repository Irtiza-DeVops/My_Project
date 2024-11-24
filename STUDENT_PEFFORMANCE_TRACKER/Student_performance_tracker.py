class Student:
    def _init_(self, name, scores):
        self.name = name
        self.scores = scores
        self.subjects = ['Math 🧮', 'Science 🔬', 'English 📚']
    
    def calculate_average(self):
        return sum(self.scores) / len(self.scores)
    
    
    def is_passing(self):
                                          
        return all(score >= 40 for score in self.scores)
    
    def failing_subjects(self):
        c=[]

        for i,s in enumerate(self.scores):
            if s<40:
                c.append(self.subjects[i])
        return c
    def passing_subjects(self):
        d=[]
        for x,y in enumerate(self.scores):

            if y>40:
              d.append(self.subjects[x])
        return d


class PerformanceTracker:
    def _init_(self):
        self.students = {}
    
    def add_student(self, name, scores):
        
            
        student = Student(name, scores)
        self.students[name] = student
       
            
    
    def calculate_class_average(self):
        total = sum(student.calculate_average() for student in self.students.values())
        return total / len(self.students)
    
    def display_student_performance(self):
        print("\n" + "="*40)
        print("🎓 Student Performance Report 🎓")
        print("="*40)
        for student in self.students.values():
            avg = student.calculate_average()
            pass_fail = "✅ Passing" if student.is_passing() else "❌ Failing"
            status_color = "\033[32m" if student.is_passing() else "\033[31m" 
            reset_color = "\033[0m"  
            print(f"👩‍🏫 Student: {student.name}")
            print(f"  📊 Average: {avg:.2f}")
            print(f"  Status: {status_color}{pass_fail}{reset_color}")
            if student.is_passing():
                passing_subjects=student.passing_subjects()
                print(f"  🚨 Passing Subjects: {', '.join(passing_subjects)}")
            print("-" * 40)

            
            
            if not student.is_passing():
                failing_subjects = student.failing_subjects()
                print(f"  🚨 Failing Subjects: {', '.join(failing_subjects)}")
            
            print("-" * 40)




tracker = PerformanceTracker()

print("="*40)
print("✨ Welcome to the Student Performance Tracker ✨")
print("="*40)

while True:
   

    name = input("\n🔑 Enter student's name (for break write stop): ")
    if name.lower() == 'stop':
           break
    if not name.isalpha():
       
        print("❌ Invalid name. Please enter a name containing only alphabetic characters.")
        continue
              
    


    scores = []
    for subject in ['Math 🧮', 'Science 🔬', 'English 📚']:
        while True:
            try:
                score = int(input(f"Enter {subject} score for {name}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("❗ Please enter a score between 0 and 100.")
            except ValueError:
                print("❌ Invalid input. Please enter a valid number for the score.")
    
    tracker.add_student(name, scores)

tracker.display_student_performance()
print(f"\n💡 Class Average: {tracker.calculate_class_average():.2f}")
print("="*40)