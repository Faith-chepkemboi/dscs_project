DSCS - PesaPal Distributed Source Control System

DSCS (Distributed Source Control System) is a type of version control system that allows multiple developers to work on the same codebase simultaneously.
Features

    Initialize a Repository: Set up a new DSCS repository in the current directory.
    Staging and Committing Files: Track changes by adding files to the staging area and committing them.
    Branching: Create and switch between branches to manage different versions of your project.
    Merging: Integrate changes from one branch into another with basic conflict detection.
    Cloning: Duplicate the repository to a new location.
    View Commit History: Display a list of past commits with metadata.
    Ignore Files: Use a .ignore file to exclude files from being staged.



   # Clone this repository (if necessary):

      git clone https://github.com/yourusername/dscs-project.git
       cd dscs-project

   # Run the DSCS program using Python 3:
     python3 main.py

 #Expected Results   (screen shot)

 ![Screenshot from 2024-12-05 08-49-02](https://github.com/user-attachments/assets/ad56738b-1520-432d-bead-5f6ac384174a)


 #Expected Results   (screen output)



 Repository already initialized.
File 'pesapaldoc1.txt' added to staging area.
Commit '7475d1edf67f4d6382972593361cd671e22f32b2' created successfully.
Branch 'PesaPal2024SourceControlSystem' already exists.
Switched to branch 'PesaPal2024SourceControlSystem'.
File 'pesapaldoc2.txt' added to staging area.
Commit 'ee3b0b73ca1ee02c19beea72749ff80cef07f020' created successfully.
Switched to branch 'master'.
Conflicts detected in the following files:
  pesapalRegdoc1.txt
  pesapalRegdoc2.txt
The directory new_cloned_repo already exists. Cannot clone here.
Commit history for branch 'master':

Commit 7475d1edf67f4d6382972593361cd671e22f32b2:
  Message: First commit of pesapaldoc1.txt
  Timestamp: 1733377262
  Parent: 91311d003bd30fc22c7f0e0bd406b84dd84c239b
  Files:
    files:


Commit 91311d003bd30fc22c7f0e0bd406b84dd84c239b:
  Message: First commit of pesapaldoc1.txt
  Timestamp: 1733220052
  Parent: 2b6fd282430ee8c76c7c958256246bdca39509c1
  Files:
    files:


Commit 2b6fd282430ee8c76c7c958256246bdca39509c1:
  Message: First commit of pesapaldoc1.txt
  Timestamp: 1733220038
  Parent: 85b4a2e4ab59475092a3d207aac6e2b327199d5d
  Files:
    files:


Commit 85b4a2e4ab59475092a3d207aac6e2b327199d5d:
  Message: First commit of pesapaldoc1.txt
  Timestamp: 1733219542
  Parent: adba0cd8c011fc87631a471172c7736c67b43145
  Files:
    files:


Commit adba0cd8c011fc87631a471172c7736c67b43145:
  Message: First commit of pesapaldoc1.txt
  Timestamp: 1733219414
  Parent: 067fd07e07019998248acfa6ff9e03080f4e1d73
  Files:
    files:


Commit 067fd07e07019998248acfa6ff9e03080f4e1d73:
  Message: First commit of pesapaldoc1.txt
  Timestamp: 1733219162
  Parent: 3b9694ffca37355e25d27bbae644db1db4dfae2d
  Files:
    files:


Commit 3b9694ffca37355e25d27bbae644db1db4dfae2d:
  Message: First commit of pesapaldoc1.txt
  Timestamp: 1733218982
  Parent: 8a9a39116baecb0f4b0b5677d72976530eab52b6
  Files:
    files:


Commit 8a9a39116baecb0f4b0b5677d72976530eab52b6:
  Message: First commit of pesapaldoc1.txt
  Timestamp: 1733218909
  Parent: 5c868c4b0c7485d4737586b44d23f63f6ecfe371
  Files:
    files:


Commit 5c868c4b0c7485d4737586b44d23f63f6ecfe371:
  Message: First commit of testfile1.txt
  Timestamp: 1733218656
  Parent: d5cd9cf3f9c0d9a58336aba489d326c3a3400a97
  Files:
    files:


Commit d5cd9cf3f9c0d9a58336aba489d326c3a3400a97:
  Message: First commit of testfile1.txt
  Timestamp: 1733218632
  Parent: 10c5b504c9ae421eb0f6a24a6e81017c603aa24a
  Files:
    files:


Commit 10c5b504c9ae421eb0f6a24a6e81017c603aa24a:
  Message: First commit of testfile1.txt
  Timestamp: 1733218574
  Parent: 762842d9e68b4b1aa3405412cda89e65d0ab4c65
  Files:
    files:


Commit 762842d9e68b4b1aa3405412cda89e65d0ab4c65:
  Message: First commit of testfile1.txt
  Timestamp: 1733218346
  Parent: 50011f08d0ea96ad9336a86c21369becd9db4166
  Files:
    files:


Commit 50011f08d0ea96ad9336a86c21369becd9db4166:
  Message: Second commit of testfile2.txt
  Timestamp: 1733217885
  Parent: ba207b0b7e71bd78b55305ee225d5e02108076fb
  Files:
    files:


Commit ba207b0b7e71bd78b55305ee225d5e02108076fb:
  Message: First commit of testfile1.txt
  Timestamp: 1733217885
  Parent: 3d9eb12f3f199a2636e23304f1ccf080b7afbff9
  Files:
    files:


Commit 3d9eb12f3f199a2636e23304f1ccf080b7afbff9:
  Message: Second commit of testfile2.txt
  Timestamp: 1733217815
  Parent: 98c7b07f5093fdba9c1b2677317d335637811493
  Files:
    files:


Commit 98c7b07f5093fdba9c1b2677317d335637811493:
  Message: First commit of testfile1.txt
  Timestamp: 1733217815
  Parent: ef6b1890d27b6434e1ce7618140e0f30d12d5a68
  Files:
    files:


Commit ef6b1890d27b6434e1ce7618140e0f30d12d5a68:
  Message: Initial commit of testfile.txt
  Timestamp: 1733217780
  Parent: 2342927c3655380705d790bae8c9bc6c9987f792
  Files:
    files:


Commit 2342927c3655380705d790bae8c9bc6c9987f792:
  Message: Second commit of testfile2.txt
  Timestamp: 1733211363
  Parent: 1be1ecd6fab94cf374b8c87ee0b5874ada9e31bc
  Files:
    files:


Commit 1be1ecd6fab94cf374b8c87ee0b5874ada9e31bc:
  Message: First commit of testfile1.txt
  Timestamp: 1733211363
  Parent: 6d4853e7d330c3d1780300742a4def66dec383c8
  Files:
    files:


Commit 6d4853e7d330c3d1780300742a4def66dec383c8:
  Message: Second commit of testfile2.txt
  Timestamp: 1733211116
  Parent: f874121d8fabb0aa10f9ea0e869072d67687e135
  Files:
    files:


Commit f874121d8fabb0aa10f9ea0e869072d67687e135:
  Message: First commit of testfile1.txt
  Timestamp: 1733211116
  Parent: 1001dd1dbdd88e8dc7a1621c453687a6be8b89b7
  Files:
    files:


Commit 1001dd1dbdd88e8dc7a1621c453687a6be8b89b7:
  Message: Initial commit of testfile.txt
  Timestamp: 1733211021
  Files:
    files:


