# Log analysis

Python console application for database log analytics. 

This is a project with academic purposes for [Fullstack Web Developer Nanodegree by Udacity](https://br.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

# Before you run this exercise:
- Install Python 3;
- Install Vagrant and VirtualBox;
- Download FSDN-Virtual-Machine (inside the exercise);
 
# Installing our Python dependencies

**psycopg2** - PostgreSQL driver for Python.
```bash
pip install psycopg2
```

# Running the program

## Before running the .py file:

- It's interesting to clone this repository (or simply move the entire folder) inside the `vagrant` folder, which is inside the VM's root folder.
- Run `vagrant up` to initialize the VM;
- Then, run `vagrant ssh` to access the VM's command-line interface;
- Inside the VM, run `psql -d news -f newsdata.sql` to load the content inside `newsdata.sql` file to the database;

## Everything is ready to go?

Then, inside the project's root folder simply run the `.py` file.
```bash
python3 program.py
```
