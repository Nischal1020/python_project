|**Test Case ID**|||||
| :-: | :- | :- | :- | :- |
|Test Case ID|Software Feature|Steps|Expected||
|Tc 001|log  in as admin|1\. Launch the application.|The application should be launched successfully.||
|||2\. Choose the operation: Are you a Doctor, Patient, or Admin?|The operation menu should be displayed.||
|||3\. Choose 'admin' operation.|System should ask admin for login details||
||||If  user\_name and password are correct admin can login in system||
||||1\. " Login successful " message should be displayed 2.  The operation menu should be displayed.||



|Tc 002|Register Doctor|log  in as admin|1\. " Login successful " message should be displayed 2.  The operation menu should be displayed.|
| :-: | - | - | - |
|||Choose the operation:   1- Register/view/update/delete doctor|Enter the operation (register/view/update/delete) should be display|
|||Choose 'Register' operation.|The system should ask for doctor details.|
|||Enter the doctor's first name, surname, and specialty.|The doctor should be registered successfully. And ' Doctor registered successfully.' messsage should be display|



|Tc 003|View Doctor|1\. log  in as admin|1\. " Login successful " message should be displayed 2.  The operation menu should be displayed.|
| - | - | - | - |
|||Choose the operation:   1- Register/view/update/delete doctor|Enter the operation (register/view/update/delete) should be display|
|||Choose 'view' operation.|All the doctor's full names and specialties should be  displayed including newly added doctors|
|Tc 004|Update Doctor|log  in as admin|1\. " Login successful " message should be displayed 2.  The operation menu should be displayed.|



|||Choose the operation:   1- Register/view/update/delete doctor|Enter the operation (register/view/update/delete) should be display|
| - | - | - | - |
|||Choose 'update' operation.|1\. All the doctor's full names and specialties should be  displayed  2. "Enter the index of the doctor to update: " message should be display|
|||Write the proper index number of the doctor that you want to update|1\. Current information should be display 2. "Enter the new specialty: " message should be display|
|||Enter the new specialty|1\. Message "Doctor information updated successfully." should be display 2. Doctor information should be successfully updated|



|Tc 005|Delete Doctor|log  in as admin|1\. " Login successful " message should be displayed 2.  The operation menu should be displayed.|
| - | - | - | - |
|||Choose the operation:   1- Register/view/update/delete doctor|Enter the operation (register/view/update/delete) should be display|
|||Choose 'Delete' operation.|1\. All the doctor's full names and specialties should be  displayed  2. "Enter the index of the doctor to delete:" message should be displayed|
|||Write the proper index number of the doctor that you want to delete|1\. Message "Doctor deleted successfully." should be displayed 2. Doctor in that index should be deleted|



|Tc 005|View patient|log  in as admin|1\. " Login successful " message should be displayed 2.  The operation menu should be displayed.|
| - | - | - | - |
|||Choose the operation:   2- Register/view/update/delete patient|Enter the operation (register/view/update/delete) should be display|
|||Choose 'View' operation.|All the Patient's full names and and other details should be displayed|
|Tc 006|Assign doctor to a patient|1\. log  in as admin|1\. " Login successful " message should be displayed 2.  The operation menu should be displayed.|



|||Choose the operation:    5- Assign doctor to a patient|1\. All the Patient's full names and and other details should be displayed 2. Message "Enter the index of the patient to assign a doctor: "should be display|
| - | - | - | - |
||||1\. All the doctor's full names and specialties should be  displayed  2. "Enter the index of the doctor to assign the patient:" message should be displayed|
|||Write the proper index number of the doctor and the patient to assign|1\. Doctor should be assign to patient  2. Proper success message should be displayed|
|Tc 007|Discharge patient|log  in as admin|1\. " Login successful " message should be displayed 2.  The operation menu should be displayed.|



|||Choose the operation:     3- Discharge patient|1\. All the Patient's full names and and other details should be displayed 2. Message "Enter the index of the patient to discharge:  "should be display|
| - | - | - | - |
|||Write the proper index number of the patient to discharge|1\. Patient should discharged successfully. 2. Message "Patient discharged successfully." should be displayed|
|Tc 008|View discharged patients|log  in as admin|1\. " Login successful " message should be displayed 2.  The operation menu should be displayed.|
|||Choose the operation:     4- View discharged patients|All the discharged patients should be displayed with details|



|Tc 009|Update admin information (name, password, and address)|log  in as admin|1\. " Login successful " message should be displayed 2.  The operation menu should be displayed.|
| - | - | - | - |
|||Choose the operation:      6- update admin details|The system should ask for new details to update|
||||New details should be update|
|Tc 010|Check patients details (names, symptoms,etc.)|log  in as admin|1\. " Login successful " message should be displayed 2.  The operation menu should be displayed.|
|||Choose the operation:   2- Register/view/update/delete patient|Enter the operation (register/view/update/delete) should be display|



|||Choose 'View' operation.|All the Patient's full names and and other details should be displayed|
| - | - | - | - |
|Tc 011|Group patients of same family together by admin|log  in as admin|1\. " Login successful " message should be displayed 2.  The operation menu should be displayed.|
|||Choose the operation:      8- view/update group of patient of the same family:|Enter your option (view/update) should be display|
|||Choose 'update' operation.|1\. All the Patient's full names and and other details should be displayed  2. Message "Enter the index of the patient to group "should be display|



||||1\. All the doctor's full names and specialties should be  displayed  2."Enter the index of the doctor to group:" message should be displayed|
| - | - | - | - |
||||A proper success message should be displayed|
|Tc 012|Relocating patients from one doctor to another|log  in as admin|1\. " Login successful " message should be displayed 2.  The operation menu should be displayed.|
|||Choose the operation:     9- Relocate patient|1\. All the Patient's full names and and other details should be displayed 2. Message "Enter the index of the patient to relocate"should be display|



||||All doctor should be displayed with details message "Enter the index of the new doctor to assign the patient" should be shown|
| - | - | - | - |
||||Proper message should be displayed patient should be relocated|
|Tc 013|Load all patients into a file|log  in as admin|1\. " Login successful " message should be displayed 2.  The operation menu should be displayed.|
|||Choose the operation:   2- Register/view/update/delete patient|Enter the operation (register/view/update/delete) should be display|
|||Choose 'Register' operation.|The system should ask for Patient details.|



|||Enter the details ask by system|The patient should be registered successfully in text file. And ' Data saved to patient\_data.txt..' messsage should be display|
| - | - | - | - |
|Tc 014|Load all the patients data from file|log  in as admin|1\. " Login successful " message should be displayed 2.  The operation menu should be displayed.|
|||Choose the operation:   2- Register/view/update/delete patient|Enter the operation (register/view/update/delete) should be display|
|||Choose 'View' operation.|All the Patient's full names and and other details should be displayed|



|Tc 015|View total number of doctors in the system|log  in as admin|1\. " Login successful " message should be displayed 2.  The operation menu should be displayed.|
| - | - | - | - |
|||Choose the operation:   1- Register/view/update/delete doctor|Enter the operation (register/view/update/delete) should be display|
|||Choose 'View' operation.|All the Patient's full names and and other details should be displayed|
||||Total number of doctors should be shown in index|
|Tc 016|View total number of patients per doctor|Firstly, assign doctor to patient as admin||
|||Than, choose the operation:   7- View patient as per doctor assign|Total number of patients per doctor should be shown|

