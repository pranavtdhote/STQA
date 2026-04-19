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

// import java.util.*;

// class Student {
//     String name;
//     int[] marks;

//     Student(String name, int[] marks) {
//         this.name = name;
//         this.marks = marks;
//     }
// }

// public class StudentResult {

//     // Any one subject > 60
//     public static int countAny(List<Student> students) {
//         int count = 0;

//         for (Student s : students) {
//             for (int m : s.marks) {
//                 if (m > 60) {
//                     count++;
//                     break;
//                 }
//             }
//         }
//         return count;
//     }

//     // All subjects > 60
//     public static int countAll(List<Student> students) {
//         int count = 0;

//         for (Student s : students) {
//             boolean allAbove = true;

//             for (int m : s.marks) {
//                 if (m <= 60) {
//                     allAbove = false;
//                     break;
//                 }
//             }

//             if (allAbove) count++;
//         }
//         return count;
//     }

//     public static void main(String[] args) {

//         List<Student> students = new ArrayList<>();

//         students.add(new Student("Amit", new int[]{70, 40}));
//         students.add(new Student("Rahul", new int[]{80, 75}));
//         students.add(new Student("Sneha", new int[]{55, 65}));
//         students.add(new Student("Priya", new int[]{90, 88}));

//         int anyCount = countAny(students);
//         int allCount = countAll(students);

//         System.out.println("Students with >60 in ANY subject: " + anyCount);
//         System.out.println("Students with >60 in ALL subjects: " + allCount);
//     }
// }
