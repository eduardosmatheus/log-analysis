# Log analysis

Python console application for database log analytics. 

This is a project with academic purposes for [Fullstack Web Developer Nanodegree by Udacity](https://br.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

# Before you run this exercise:
- Install Python 3;
- Install Vagrant and VirtualBox;
- Download FSDN-Virtual-Machine (inside the exercise);
  - Run `vagrant up` to initialize the VM, then run `vagrant ssh` to acces the VM's command-line interface;
  - Then, run `psql -d news -f newsdata.sql` to load newsdata.sql data inside the database;
 
# Installing our Python dependencies

**psycopg2** - PostgreSQL driver for Python.
```bash
pip install psycopg2
```

# Running the program

Inside the project root folder:

```bash
python3 program.py
```
