import pandas as pd
from openpyxl.styles import Font, PatternFill
from openpyxl import load_workbook 
import os

def create_and_uodate_student_records():
    """
    Create an Excel File and Update 10 records into it
    """
    try:
        headers = ["Roll No.", "Name" , "Age" , "Email", "Phone", "Subject", "Marks", "Grade", "Status", "Remark"]

        students_data = [
            [1, "Pranav Dhote" , 17 , "pranavtdhote@gmail.com" , "8446432484" , "STQA" , 99 , "O" , "Pass", "Excellent"],
            [2, "Om Patil", 20, "aditishuckla@email.com", "9876543211", "Physics", 85, "A", "Pass", "Good"],
            [3, "Chetan Yadav", 21, "chetan.yadav@email.com", "9876543212", "Chemistry", 78, "B+", "Pass", "Good"],
            [4, "Deepa Singh", 20, "deepa.singh@email.com", "9876543213", "Biology", 88, "A", "Pass", "Very Good"],
            [5, "Esha Verma", 21, "esha.verma@email.com", "9876543214", "English", 91, "A+", "Pass", "Excellent"],
            [6, "Faisal Ahmed", 20, "faisal.ahmed@email.com", "9876543215", "History", 75, "B", "Pass", "Satisfactory"],
            [7, "Hemant Kaur", 20, "hemant.kaur@email.com", "9876543216", "Geography", 82, "A", "Pass", "Good"],
            [8, "Harsh Gupta", 21, "harsh.gupta@email.com", "9876543217", "Computer Science", 95, "A+", "Pass", "Excellent"],
            [9, "Ishita Das", 20, "ishita.das@email.com", "9876543218", "Economics", 87, "A", "Pass", "Very Good"],
            [10, "Sneha Roy", 20, "sneha.roy@email.com", "9876543219", "Statistics", 79, "B+", "Pass", "Good"]
        ]

        df = pd.DataFrame(students_data,columns = headers)

        file_path = os.path.join(os.path.dirname(__file__), "student_records.xlsx")
        df.to_excel(file_path, index=False, sheet_name="Student Records")

        wb = load_workbook(file_path)
        ws = wb.active
        header_fill = PatternFill(start_color="4472C4", end_color="447C2",fill_type = "solid")
        header_font = Font(bold = "True", color= "FFFFFF")

        for cell in ws[1]:
            cell.fill=header_fill
            cell.font=header_font

        column_widths = [10, 16, 8, 25, 15, 18, 8, 8, 8, 15]
        for col_num, width in enumerate(column_widths, 1):
            ws.column_dimensions[chr(64 + col_num)].width = width

        wb.save(file_path)
        print("Excel file created successfully at: {file_path}")

        print("\n"+"="*100)
        print("STUDENT RECORDS - VERIFICATION")
        print("="*100)
        verify_df = pd.read_excel(file_path)
        print(verify_df.to_string(index=False))

        print("\n" + "="*100)
        print(f"✓ Total records inserted: {len(verify_df)}")
        print("✓ Test PASSED - All student records updated successfully!")
        
    except Exception as e:
        print(f"✗ Error occurred: {str(e)}")
        print("✗ Test FAILED")

    if __name__ == "__main__":
        create_and_update_student_records()




