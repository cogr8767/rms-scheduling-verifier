# rms-scheduling-verifier

  This algorithm takes periods and execution times for multiple tasks and determines if the task set is schedulable with RMS. The algorithm makes multiple assumptions about
  the data that its given, so I provided two files to package it up nicely.

alg_project_adjustable_vars.py    is the algorithm meant to be used by adjusting the values in the source code. This python code also sorts the tasks based on period and
                                    checks for over- or under-utilization, allowing for the answer to be caught before the algorithm is run in some cases. Values can be 
                                    customized on lines 17 and 18. To check the validity of the values, simply run the file. It should be noted that the index of each 
                                    list is meant to refer to the same task.
                                  
alg_project_plus_ui.py            is the algorithm with a simple terminal UI. This python code also sorts the tasks based on period and checks for over- or under-utilization. 
                                    To use this file, run it and simply choose from the menus and input the task values as needed.
