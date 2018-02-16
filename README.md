# p3sbc Python3 simple bin crawler

## 1.Quick description

This script is a program manager of security correctives multi-platforms (Windows, GNU/Linux, BSD & MacOsX).
Test passed for GNU/linux
## 2.Project state
#### **In progress**

**Part. 1 - Update Database (-u)**
*100% - Complete*
-----
**Part. 2 - Check Vulnerabilities (-c)**
*100% - Complete
----
**Part. 3 - List Vulnerabilities (-l)**
*100% - Complete
----------
## 3.Description
This script is a program manager of security correctives on all different systems (Windows, GNU/Linux, BSD & MacOsX).
He supports all file types (a.out, ELF, PE, COFF etc...).
The system is probed to assess arch , bin type , version ...
We use a database to avoid some searches on each execution.
The project will be in three parts :
## 3b.Set up, quick configuration
### Create virtual environment
To use our **the Crawler**, you have to create a virtual environment with Virtualenv.
```sh
sudo apt update
sudo apt install python3.6 && sudo apt install python3-venv
sudo https://github.com/antares667367/crawler.git
cd crawler
sudo python3.6 -m venv virtual_env
sudo virtual_env/bin/pip install requirements.txt
sudo virtual_env/bin/python3.6 checksyscve.py -h
```
## 4.Usage
##### Update Database of local binary files
```bash
[real or virt py version] checksyscve.py -u <--updatedatabase> [-f database_filepath]
```
On first time, the program takes a fingerprint of the running environment to know the type of binary files.
Then, he browses all files on the system and register path's file, hash's file and version's file on Tiny Database.
##### Check vulnerabilities
```bash
[real or virt py version] checksyscve.py -c <--checkvuln> [-f binary_filepath]
```
Browse all path's binary file on database, identify versions and check vulnerabilities nearby CVE (Common Vulnerabilities and Exposures).
##### Display vulnerabilities
```bash
[real or virt py version] checksyscve.py -l <--listvuln> [-f binary_filepath]
```
Give history of all binary files vulnerable found with CVE
```bash
 [real or virt py version] checksyscve.py --q <--listvuln> [-f binary_filepath]
```
## 5.Licences
Open Source
## 6.Documentation
### API used
#### 1.TinyDB
>TinyDB is a lightweight document oriented database optimized for your happiness :)
>It's written in pure Python and has no external dependencies.
>The target are small apps that would be blown away by a SQL-DB or an external database server.
[Git Documentation](https://github.com/msiemens/tinydb)
#### 2.  API dev by RICO Kevin
>This API recovers in local the actual CVE online.
[No doc]()
### Modules used
##### Platform
>The platform module in Python is used to access the underlying platform’s data,
>such as, hardware, operating system, and interpreter version information.
>The platform module includes tools to see the platform’s hardware, operating
>system, and interpreter version information where the program is running.
[Platform Documentation](https://docs.platform.sh/)
##### Magic
>python-magic is a python interface to the libmagic file type identification library.
>libmagic identifies file types by checking their headers according to a predefined list of file types.
>This functionality is exposed to the command line by the Unix command file.
[Git documentation](https://github.com/ahupp/python-magic)
##### GetOpt
>This module helps scripts to parse the command line arguments in sys.argv.
>It supports the same conventions as the Unix getopt() function (including the special meanings of arguments of the form '-' and '--').
>Long options similar to those supported by GNU software may be used as well via an optional third argument.
[Git documentation](https://github.com/python/cpython/blob/master/Lib/getopt.py)
##### Fnmatch
>The fnmatch module is used to compare filenames against glob-style patterns such as used by Unix shells.
[Pymotw documentation](https://pymotw.com/2/fnmatch/)
##### Beautiful Soup
>Beautiful Soup is a Python library for pulling data out of HTML and XML files.
>It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.
>It commonly saves programmers hours or days of work.
[Documentation](http://beautiful-soup-4.readthedocs.io/en/latest/)
## 7. Authors
__ESD 13__ - Aston Project
@antares667367 : Aldeguer Thomas
@tonyESD : Tony Hasbroucq
@bnoncleben : Pruvost Benjamin
## 8.Contributing
Whether reporting bugs, discussing improvements and new ideas or writing extensions.
## 9.Changelog
#### v1.0.0 (2018-02-16)
