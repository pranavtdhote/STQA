import java.util.*;

class Student {
    String name;
    int marks;

    // Constructor
    Student(String name, int marks) {
        this.name = name;
        this.marks = marks;
    }
}

public class StudentMarks {

    // Method to count students with marks > 60
    public static int countHighScorers(List<Student> students) {
        int count = 0;

        for (Student s : students) {
            if (s.marks > 60) {
                count++;
            }
        }
        return count;
    }

    // Method to get students with marks > 60
    public static List<Student> getHighScorers(List<Student> students) {
        List<Student> result = new ArrayList<>();

        for (Student s : students) {
            if (s.marks > 60) {
                result.add(s);
            }
        }
        return result;
    }

    public static void main(String[] args) {

        // Creating student list with names and marks
        List<Student> students = new ArrayList<>();

        students.add(new Student("Amit", 45));
        students.add(new Student("Rahul", 78));
        students.add(new Student("Sneha", 62));
        students.add(new Student("Priya", 90));
        students.add(new Student("Karan", 55));
        students.add(new Student("Neha", 61));
        students.add(new Student("Rohit", 88));
        students.add(new Student("Anjali", 59));

        // Processing
        int count = countHighScorers(students);
        List<Student> highScorers = getHighScorers(students);

        // Output
        System.out.println("Total Students: " + students.size());
        System.out.println("Students scoring > 60: " + count);

        System.out.println("\nStudents with marks > 60:");
        for (Student s : highScorers) {
            System.out.println(s.name + " - " + s.marks);
        }
    }
}